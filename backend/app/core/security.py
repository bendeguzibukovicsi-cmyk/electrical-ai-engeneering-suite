"""
Security utilities.
"""

from datetime import datetime, timedelta
from typing import Any, Union, Optional

from jose import jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.core.config import settings
from app.db.session import get_db
from app.db.models.user import User

# Import UserRepository if available
try:
    from app.db.repositories.user import UserRepository
except Exception:
    UserRepository = None


# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password against its hash."""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """Hash a password."""
    return pwd_context.hash(password)


def authenticate_user(db: Session, email: str, password: str) -> Optional[User]:
    """Authenticate a user using the UserRepository if available."""
    if UserRepository is None:
        # Repository not available; cannot authenticate
        return None

    repo = UserRepository(db)

    # Prefer a repository-provided authenticate method
    if hasattr(repo, "authenticate"):
        try:
            user = repo.authenticate(email=email, password=password)
            return user
        except Exception:
            return None

    # Fallback to fetching by email and verifying password
    if hasattr(repo, "get_by_email"):
        user = repo.get_by_email(email=email)
        if not user:
            return None
        # Assume user has attribute `hashed_password` or `password`
        hashed = getattr(user, "hashed_password", None) or getattr(user, "password", None)
        if hashed and verify_password(password, hashed):
            return user
    return None


def create_access_token(
    subject: Union[str, Any], expires_delta: timedelta = None
) -> str:
    """Create a JWT access token."""
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


# OAuth2 scheme: point tokenUrl to the auth login endpoint
oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_STR}/auth/login")


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """Get the current user from the token and load it from the DB.

    This implementation attempts to use UserRepository to fetch the user by id.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except Exception:
        raise credentials_exception

    # If repository is available, try to load the user
    if UserRepository is not None:
        try:
            repo = UserRepository(db)
            # Try common getter names
            user = None
            for getter in ("get", "get_by_id", "get_by_pk", "get_by_email"):
                if hasattr(repo, getter):
                    try:
                        if getter == "get_by_email":
                            # Not an id-based getter, skip
                            continue
                        user = getattr(repo, getter)(int(user_id))
                        break
                    except Exception:
                        continue
            if user is None:
                # As a last resort, try authenticate with a token-less flow if supported
                user = None
        except Exception:
            user = None
    else:
        user = None

    if user is None:
        raise credentials_exception

    return user


def get_current_active_user(
    current_user: User = Depends(get_current_user),
):
    """Get the current active user."""
    if not getattr(current_user, "is_active", True):
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
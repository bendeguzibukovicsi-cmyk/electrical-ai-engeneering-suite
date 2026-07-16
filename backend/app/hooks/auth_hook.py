"""Auth API Hook
"""

from typing import Optional
from app.schemas.user import UserRead

class AuthHook:
    """Hook for authentication operations"""
    
    async def on_user_created(self, user: UserRead) -> None:
        """Called after user creation"""
        print(f"User created: {user.email}")
    
    async def on_user_login(self, user: UserRead) -> None:
        """Called after successful login"""
        print(f"User logged in: {user.email}")
    
    async def on_user_logout(self, user: UserRead) -> None:
        """Called after user logout"""
        print(f"User logged out: {user.email}")
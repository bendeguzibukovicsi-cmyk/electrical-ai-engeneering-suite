"""
API router for version 1.
"""

from fastapi import APIRouter

from app.api.v1.endpoints import auth, circuits

api_router = APIRouter()

# Include only available routers
api_router.include_router(auth.router, prefix="/auth", tags=["authentication"])
api_router.include_router(circuits.router, prefix="/circuits", tags=["circuits"])

"""
API router for version 1.
"""

from fastapi import APIRouter

from app.api.v1.endpoints import auth, circuits, projects, chat, simulation, pcb, firmware, datasheet, bom, documentation

api_router = APIRouter()

# Include all routers
api_router.include_router(auth.router, prefix="/auth", tags=["authentication"])
api_router.include_router(projects.router, prefix="/projects", tags=["projects"])
api_router.include_router(chat.router, prefix="/chat", tags=["chat"])
api_router.include_router(circuits.router, prefix="/circuits", tags=["circuits"])
api_router.include_router(simulation.router, prefix="/simulation", tags=["simulation"])
api_router.include_router(pcb.router, prefix="/pcb", tags=["pcb"])
api_router.include_router(firmware.router, prefix="/firmware", tags=["firmware"])
api_router.include_router(datasheet.router, prefix="/datasheet", tags=["datasheet"])
api_router.include_router(bom.router, prefix="/bom", tags=["bom"])
api_router.include_router(documentation.router, prefix="/documentation", tags=["documentation"])
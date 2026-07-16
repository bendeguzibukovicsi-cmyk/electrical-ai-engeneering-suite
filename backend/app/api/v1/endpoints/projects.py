"""
Projects endpoints.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Dict, Any, List

from app.db.session import get_db

router = APIRouter()


@router.get("/", response_model=List[Dict[str, Any]])
def list_projects(db: Session = Depends(get_db)):
    """
    List all projects.
    """
    # TODO: Implement project listing
    return []


@router.post("/", response_model=Dict[str, Any])
def create_project(
    name: str,
    description: str = None,
    db: Session = Depends(get_db)
):
    """
    Create a new project.
    """
    # TODO: Implement project creation
    return {"name": name, "description": description}


@router.get("/{project_id}", response_model=Dict[str, Any])
def get_project(project_id: int, db: Session = Depends(get_db)):
    """
    Get a specific project.
    """
    # TODO: Implement project retrieval
    return {}


@router.put("/{project_id}", response_model=Dict[str, Any])
def update_project(
    project_id: int,
    name: str = None,
    description: str = None,
    db: Session = Depends(get_db)
):
    """
    Update a project.
    """
    # TODO: Implement project update
    return {}


@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_project(project_id: int, db: Session = Depends(get_db)):
    """
    Delete a project.
    """
    # TODO: Implement project deletion
    pass
"""
Simulation endpoints.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Dict, Any

from app.db.session import get_db

router = APIRouter()


@router.post("/run", response_model=Dict[str, Any])
def run_simulation(
    circuit_data: Dict[str, Any],
    parameters: Dict[str, Any] = None,
    db: Session = Depends(get_db)
):
    """
    Run a simulation.
    """
    # TODO: Implement simulation running
    return {"status": "running"}


@router.get("/{simulation_id}/results", response_model=Dict[str, Any])
def get_simulation_results(simulation_id: int, db: Session = Depends(get_db)):
    """
    Get simulation results.
    """
    # TODO: Implement results retrieval
    return {}


@router.post("/{simulation_id}/stop", response_model=Dict[str, Any])
def stop_simulation(simulation_id: int, db: Session = Depends(get_db)):
    """
    Stop a running simulation.
    """
    # TODO: Implement simulation stopping
    return {"status": "stopped"}
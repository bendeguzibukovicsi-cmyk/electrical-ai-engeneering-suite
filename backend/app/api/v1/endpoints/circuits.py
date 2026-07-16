"""
Circuit-related endpoints.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Dict, Any, Optional, List

from app.db.session import get_db
from app.agents.electrical_engineering import ElectricalEngineeringAgent

router = APIRouter()


@router.post("/design", response_model=Dict[str, Any])
async def design_circuit(
    requirements: str,
    constraints: Optional[Dict[str, Any]] = None,
    db: Session = Depends(get_db)
):
    """
    Design a circuit based on requirements.
    """
    agent = ElectricalEngineeringAgent()
    try:
        result = await agent.design_circuit(requirements, constraints)
        return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to design circuit: {str(e)}"
        )


@router.post("/analyze", response_model=Dict[str, Any])
async def analyze_circuit(
    circuit_data: Dict[str, Any],
    db: Session = Depends(get_db)
):
    """
    Analyze an existing circuit.
    """
    agent = ElectricalEngineeringAgent()
    try:
        result = await agent.analyze_circuit(circuit_data)
        return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to analyze circuit: {str(e)}"
        )


@router.post("/suggest-components", response_model=List[Dict[str, Any]])
async def suggest_components(
    requirements: Dict[str, Any],
    db: Session = Depends(get_db)
):
    """
    Suggest components based on requirements.
    """
    agent = ElectricalEngineeringAgent()
    try:
        result = await agent.suggest_components(requirements)
        return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to suggest components: {str(e)}"
        )

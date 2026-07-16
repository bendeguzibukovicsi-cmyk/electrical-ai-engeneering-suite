"""
Chat endpoints.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Dict, Any, List

from app.db.session import get_db

router = APIRouter()


@router.get("/", response_model=List[Dict[str, Any]])
def list_conversations(db: Session = Depends(get_db)):
    """
    List all chat conversations.
    """
    # TODO: Implement conversation listing
    return []


@router.post("/", response_model=Dict[str, Any])
def create_conversation(
    title: str = None,
    db: Session = Depends(get_db)
):
    """
    Start a new conversation.
    """
    # TODO: Implement conversation creation
    return {"title": title}


@router.get("/{conversation_id}", response_model=Dict[str, Any])
def get_conversation(conversation_id: int, db: Session = Depends(get_db)):
    """
    Get a specific conversation.
    """
    # TODO: Implement conversation retrieval
    return {}


@router.post("/{conversation_id}/message", response_model=Dict[str, Any])
def send_message(
    conversation_id: int,
    message: str,
    db: Session = Depends(get_db)
):
    """
    Send a message in a conversation.
    """
    # TODO: Implement message sending
    return {"message": message}
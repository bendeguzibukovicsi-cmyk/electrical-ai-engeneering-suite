"""Utils module
"""

from datetime import datetime


def get_current_timestamp() -> str:
    """Get current timestamp in ISO format."""
    return datetime.now().isoformat()


def format_timestamp(dt: datetime) -> str:
    """Format datetime to ISO format."""
    return dt.isoformat()

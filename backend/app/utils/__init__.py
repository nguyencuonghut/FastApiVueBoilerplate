"""Utility functions and helpers"""


def get_pagination_params(skip: int = 0, limit: int = 100) -> tuple:
    """Validate and return pagination parameters"""
    skip = max(0, skip)
    limit = min(max(1, limit), 1000)  # Limit between 1 and 1000
    return skip, limit


def format_datetime(dt):
    """Format datetime for API response"""
    if dt is None:
        return None
    return dt.isoformat()

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import Annotated
from app.database.database import get_db
from app.security.dependencies import get_current_user
from app.models import User

router = APIRouter(prefix="/dashboard", tags=["dashboard"])


@router.get("/stats")
async def get_dashboard_stats(
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)]
):
    """Get dashboard statistics (role-specific)"""
    if current_user.role.name == "admin":
        # Admin stats
        total_users = db.query(User).count()
        active_users = db.query(User).filter(User.is_active == True).count()
        
        return {
            "total_users": total_users,
            "active_users": active_users,
            "inactive_users": total_users - active_users,
            "server_status": "healthy",
            "cpu_usage": 45.2,
            "memory_usage": 62.5
        }
    else:
        # User stats
        return {
            "last_login": current_user.updated_at,
            "session_count": 1,
            "devices": ["Web Browser"],
            "server_status": "healthy"
        }


@router.get("/activity-log")
async def get_activity_log(
    current_user: Annotated[User, Depends(get_current_user)],
    limit: Annotated[int, Query(gt=0)] = 20
):
    """Get recent activity log"""
    # This is a placeholder - in production, you'd query an audit log table
    activities = [
        {"timestamp": "2024-02-16 10:45", "action": "Login", "user": current_user.username},
        {"timestamp": "2024-02-16 10:30", "action": "Profile Update", "user": current_user.username},
        {"timestamp": "2024-02-16 10:15", "action": "Data Export", "user": current_user.username},
    ]
    return {"activities": activities[:limit]}

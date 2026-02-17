from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from sqlalchemy import or_, func
from typing import List, Optional
from app.database.database import get_db
from app.schemas.user import UserResponse, UserCreate, RoleResponse, PermissionResponse
from app.security.dependencies import get_admin_user
from app.services.user import UserService
from app.models import User, Role, Permission

router = APIRouter(prefix="/admin", tags=["admin"])


@router.get("/users")
async def list_users(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    search: Optional[str] = Query(None),
    admin_user: User = Depends(get_admin_user),
    db: Session = Depends(get_db)
):
    """List users with pagination and search (admin only)"""
    query = db.query(User)
    
    # Apply search filter
    if search:
        search_filter = f"%{search}%"
        query = query.filter(
            or_(
                User.username.ilike(search_filter),
                User.email.ilike(search_filter),
                User.full_name.ilike(search_filter)
            )
        )
    
    # Get total count before pagination
    total = query.count()
    
    # Apply pagination
    users = query.offset(skip).limit(limit).all()
    
    return {
        "data": [UserResponse.model_validate(user) for user in users],
        "total": total,
        "skip": skip,
        "limit": limit
    }


@router.get("/users/{user_id}", response_model=UserResponse)
async def get_user(
    user_id: int,
    admin_user: User = Depends(get_admin_user),
    db: Session = Depends(get_db)
):
    """Get specific user (admin only)"""
    user = UserService.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user


@router.post("/users", response_model=UserResponse)
async def create_user(
    user: UserCreate,
    admin_user: User = Depends(get_admin_user),
    db: Session = Depends(get_db)
):
    """Create new user (admin only)"""
    # Check if user already exists
    if UserService.get_user_by_username(db, user.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists"
        )
    
    if UserService.get_user_by_email(db, user.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists"
        )
    
    new_user = UserService.create_user(db, user)
    return new_user


@router.delete("/users/{user_id}")
async def deactivate_user(
    user_id: int,
    admin_user: User = Depends(get_admin_user),
    db: Session = Depends(get_db)
):
    """Deactivate user (admin only)"""
    success = UserService.deactivate_user(db, user_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return {"message": "User deactivated successfully"}


@router.get("/roles", response_model=List[RoleResponse])
async def list_roles(
    admin_user: User = Depends(get_admin_user),
    db: Session = Depends(get_db)
):
    """List all roles (admin only)"""
    roles = db.query(Role).all()
    return roles


@router.get("/permissions", response_model=List[PermissionResponse])
async def list_permissions(
    admin_user: User = Depends(get_admin_user),
    db: Session = Depends(get_db)
):
    """List all permissions (admin only)"""
    permissions = db.query(Permission).all()
    return permissions

from sqlalchemy.orm import Session
from app.models import User, Role
from app.schemas.user import UserCreate, UserUpdate
from app.security.password import get_password_hash, verify_password
from typing import Optional


class UserService:
    @staticmethod
    def create_user(db: Session, user: UserCreate, role_id: int = None) -> User:
        """Create new user"""
        if role_id is None:
            # Default to User role if not specified
            role = db.query(Role).filter(Role.name == "user").first()
            role_id = role.id if role else None
        
        db_user = User(
            username=user.username,
            email=user.email,
            full_name=user.full_name,
            hashed_password=get_password_hash(user.password),
            role_id=role_id
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    
    @staticmethod
    def get_user_by_username(db: Session, username: str) -> Optional[User]:
        """Get user by username"""
        return db.query(User).filter(User.username == username).first()
    
    @staticmethod
    def get_user_by_email(db: Session, email: str) -> Optional[User]:
        """Get user by email"""
        return db.query(User).filter(User.email == email).first()
    
    @staticmethod
    def get_user_by_id(db: Session, user_id: int) -> Optional[User]:
        """Get user by ID"""
        return db.query(User).filter(User.id == user_id).first()
    
    @staticmethod
    def authenticate_user(db: Session, email: str, password: str) -> Optional[User]:
        """Authenticate user with email and password"""
        user = UserService.get_user_by_email(db, email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user
    
    @staticmethod
    def update_user(db: Session, user_id: int, user_update: UserUpdate) -> Optional[User]:
        """Update user information"""
        db_user = UserService.get_user_by_id(db, user_id)
        if not db_user:
            return None
        
        update_data = user_update.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_user, field, value)
        
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    
    @staticmethod
    def change_password(db: Session, user_id: int, new_password: str) -> bool:
        """Change user password"""
        db_user = UserService.get_user_by_id(db, user_id)
        if not db_user:
            return False
        
        db_user.hashed_password = get_password_hash(new_password)
        db.add(db_user)
        db.commit()
        return True
    
    @staticmethod
    def deactivate_user(db: Session, user_id: int) -> bool:
        """Deactivate user"""
        db_user = UserService.get_user_by_id(db, user_id)
        if not db_user:
            return False
        
        db_user.is_active = False
        db.add(db_user)
        db.commit()
        return True

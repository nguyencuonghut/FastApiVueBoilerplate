"""Initialize database with default roles and permissions"""

from sqlalchemy.orm import Session
from app.database.database import SessionLocal, engine, Base
from app.models import Role, Permission, User
from app.security.password import get_password_hash

def init_db():
    # Create tables
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    
    try:
        # Check if data already exists
        if db.query(Role).first():
            print("Database already initialized")
            return
        
        # Create permissions
        permissions_data = [
            {"name": "user:read", "description": "Read user data"},
            {"name": "user:create", "description": "Create user"},
            {"name": "user:update", "description": "Update user"},
            {"name": "user:delete", "description": "Delete user"},
            {"name": "role:read", "description": "Read roles"},
            {"name": "role:create", "description": "Create role"},
            {"name": "role:update", "description": "Update role"},
            {"name": "permission:read", "description": "Read permissions"},
            {"name": "report:read", "description": "View reports"},
            {"name": "system:config", "description": "System configuration"},
        ]
        
        permissions = []
        for perm_data in permissions_data:
            perm = Permission(**perm_data)
            permissions.append(perm)
            db.add(perm)
        
        db.flush()
        
        # Create roles with permissions
        admin_role = Role(name="admin", description="Administrator with full access")
        admin_role.permissions = permissions
        db.add(admin_role)
        
        user_role = Role(name="user", description="Regular user")
        user_perms = [p for p in permissions if "read" in p.name or "report:read" in p.name]
        user_role.permissions = user_perms
        db.add(user_role)
        
        db.flush()
        
        # Create demo users
        admin_user = User(
            username="admin",
            email="admin@example.com",
            full_name="Administrator",
            hashed_password=get_password_hash("admin123"),
            role_id=admin_role.id,
            is_active=True
        )
        db.add(admin_user)
        
        regular_user = User(
            username="user",
            email="user@example.com",
            full_name="Regular User",
            hashed_password=get_password_hash("user123"),
            role_id=user_role.id,
            is_active=True
        )
        db.add(regular_user)
        
        db.commit()
        print("Database initialized successfully")
        print("Demo Credentials:")
        print("  Admin: admin / admin123")
        print("  User: user / user123")
        
    except Exception as e:
        print(f"Error initializing database: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    init_db()

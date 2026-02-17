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
            {"name": "monitor:view", "description": "View monitoring dashboards"},
            {"name": "kiosk:access", "description": "Access kiosk displays"},
            {"name": "maintenance:manage", "description": "Manage maintenance tasks"},
            {"name": "security:manage", "description": "Manage security operations"},
        ]
        
        permissions = []
        for perm_data in permissions_data:
            perm = Permission(**perm_data)
            permissions.append(perm)
            db.add(perm)
        
        db.flush()
        
        # Create roles with permissions
        # SuperAdmin - Full access
        superadmin_role = Role(name="superadmin", description="Super Administrator with full system access")
        superadmin_role.permissions = permissions
        db.add(superadmin_role)
        
        # Admin - Most permissions
        admin_role = Role(name="admin", description="Administrator with full access")
        admin_perms = [p for p in permissions if p.name != "system:config"]
        admin_role.permissions = admin_perms
        db.add(admin_role)
        
        # IT - System configuration and monitoring
        it_role = Role(name="it", description="IT Staff - System administration")
        it_perms = [p for p in permissions if any(x in p.name for x in ["system:", "user:read", "monitor:", "role:read"])]
        it_role.permissions = it_perms
        db.add(it_role)
        
        # Bảo Trì - Maintenance monitoring
        bao_tri_role = Role(name="bao_tri", description="Bảo Trì - Maintenance staff")
        bao_tri_perms = [p for p in permissions if any(x in p.name for x in ["monitor:", "maintenance:", "report:read"])]
        bao_tri_role.permissions = bao_tri_perms
        db.add(bao_tri_role)
        
        # Bảo Vệ - Security guard kiosk access
        bao_ve_role = Role(name="bao_ve", description="Bảo Vệ - Security guard")
        bao_ve_perms = [p for p in permissions if any(x in p.name for x in ["kiosk:", "security:", "monitor:view"])]
        bao_ve_role.permissions = bao_ve_perms
        db.add(bao_ve_role)
        
        # Quản Lý Trại - Site manager kiosk access
        quan_ly_trai_role = Role(name="quan_ly_trai", description="Quản Lý Trại - Site manager")
        quan_ly_trai_perms = [p for p in permissions if any(x in p.name for x in ["kiosk:", "report:read", "monitor:view", "user:read"])]
        quan_ly_trai_role.permissions = quan_ly_trai_perms
        db.add(quan_ly_trai_role)
        
        # Regular User
        user_role = Role(name="user", description="Regular user")
        user_perms = [p for p in permissions if "read" in p.name]
        user_role.permissions = user_perms
        db.add(user_role)
        
        db.flush()
        
        # Create demo users
        superadmin_user = User(
            username="superadmin",
            email="superadmin@example.com",
            full_name="Super Administrator",
            hashed_password=get_password_hash("super123"),
            role_id=superadmin_role.id,
            is_active=True
        )
        db.add(superadmin_user)
        
        admin_user = User(
            username="admin",
            email="admin@example.com",
            full_name="Administrator",
            hashed_password=get_password_hash("admin123"),
            role_id=admin_role.id,
            is_active=True
        )
        db.add(admin_user)
        
        it_user = User(
            username="it_staff",
            email="it@example.com",
            full_name="IT Staff",
            hashed_password=get_password_hash("it123"),
            role_id=it_role.id,
            is_active=True
        )
        db.add(it_user)
        
        bao_tri_user = User(
            username="bao_tri",
            email="baotri@example.com",
            full_name="Nhân Viên Bảo Trì",
            hashed_password=get_password_hash("baotri123"),
            role_id=bao_tri_role.id,
            is_active=True
        )
        db.add(bao_tri_user)
        
        bao_ve_user = User(
            username="bao_ve",
            email="baove@example.com",
            full_name="Bảo Vệ",
            hashed_password=get_password_hash("baove123"),
            role_id=bao_ve_role.id,
            is_active=True
        )
        db.add(bao_ve_user)
        
        quan_ly_user = User(
            username="quan_ly",
            email="quanly@example.com",
            full_name="Quản Lý Trại",
            hashed_password=get_password_hash("quanly123"),
            role_id=quan_ly_trai_role.id,
            is_active=True
        )
        db.add(quan_ly_user)
        
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
        print("\nDemo Credentials:")
        print("  SuperAdmin: superadmin / super123")
        print("  Admin: admin / admin123")
        print("  IT Staff: it_staff / it123")
        print("  Bảo Trì: bao_tri / baotri123")
        print("  Bảo Vệ: bao_ve / baove123")
        print("  Quản Lý Trại: quan_ly / quanly123")
        print("  User: user / user123")
        
    except Exception as e:
        print(f"Error initializing database: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    init_db()

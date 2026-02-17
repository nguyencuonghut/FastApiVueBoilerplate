# Role-Based Access Control (RBAC) System

## Overview

The application implements a comprehensive RBAC system with 7 distinct roles, each with specific permissions and assigned layouts.

## Roles & Responsibilities

### 1. SuperAdmin
**Vietnamese**: Quản Trị Viên Tối Cao  
**Layout**: AdminLayout  
**Access Level**: Full system access

**Permissions**:
- All 14 permissions
- System configuration
- User management (CRUD)
- Role management (CRUD)
- Permission management
- Monitoring dashboards
- Kiosk access
- Maintenance management
- Security operations
- Report viewing

**Use Cases**:
- System-wide administration
- Critical configuration changes
- Emergency access
- Full audit capabilities

---

### 2. Admin
**Vietnamese**: Quản Trị Viên  
**Layout**: AdminLayout  
**Access Level**: High-level administration

**Permissions**:
- User management (CRUD)
- Role management (read/update)
- Permission viewing
- Report viewing
- Monitoring dashboards
- Kiosk access
- Maintenance management
- Security operations

**Use Cases**:
- Day-to-day administration
- User account management
- Role assignment
- Access control management

---

### 3. IT Staff
**Vietnamese**: Nhân Viên IT  
**Layout**: SystemLayout  
**Access Level**: Technical system management

**Permissions**:
- System configuration
- User read access
- Role viewing
- Monitoring dashboards

**Use Cases**:
- System maintenance
- Technical support
- Infrastructure monitoring
- Configuration management
- Log analysis

---

### 4. Bảo Trì (Maintenance)
**Vietnamese**: Nhân Viên Bảo Trì  
**Layout**: MonitorLayout  
**Access Level**: Maintenance operations

**Permissions**:
- Monitoring dashboards
- Maintenance management
- Report viewing

**Use Cases**:
- Equipment monitoring
- Preventive maintenance
- Work order management
- Asset tracking
- Maintenance reporting

---

### 5. Bảo Vệ (Security Guard)
**Vietnamese**: Bảo Vệ  
**Layout**: KioskLayout  
**Access Level**: Security operations

**Permissions**:
- Kiosk access
- Security management
- Monitoring view

**Use Cases**:
- Access control
- Security monitoring
- Visitor management
- Incident reporting
- Patrol logging

---

### 6. Quản Lý Trại (Site Manager)
**Vietnamese**: Quản Lý Trại  
**Layout**: KioskLayout  
**Access Level**: Site oversight

**Permissions**:
- Kiosk access
- Report viewing
- Monitoring view
- User read access

**Use Cases**:
- Site overview
- Staff monitoring
- Resource allocation
- Performance tracking
- Operational decisions

---

### 7. User
**Vietnamese**: Người Dùng  
**Layout**: MonitorLayout  
**Access Level**: Basic access

**Permissions**:
- Read-only access to most resources
- Report viewing
- Basic monitoring

**Use Cases**:
- General information viewing
- Report access
- Limited monitoring

---

## Permission Matrix

| Permission | SuperAdmin | Admin | IT | Bảo Trì | Bảo Vệ | Quản Lý | User |
|------------|:----------:|:-----:|:--:|:-------:|:------:|:-------:|:----:|
| user:read | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ |
| user:create | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| user:update | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| user:delete | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| role:read | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ |
| role:create | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| role:update | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| permission:read | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ |
| report:read | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ |
| system:config | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ |
| monitor:view | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| kiosk:access | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ❌ |
| maintenance:manage | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ |
| security:manage | ✅ | ✅ | ❌ | ❌ | ✅ | ❌ | ❌ |

## Layout Assignment

```
┌─────────────────┬──────────────────────┐
│ Role            │ Layout               │
├─────────────────┼──────────────────────┤
│ SuperAdmin      │ AdminLayout          │
│ Admin           │ AdminLayout          │
│ IT Staff        │ SystemLayout         │
│ Bảo Trì         │ MonitorLayout        │
│ Bảo Vệ          │ KioskLayout          │
│ Quản Lý Trại    │ KioskLayout          │
│ User            │ MonitorLayout        │
└─────────────────┴──────────────────────┘
```

## Access Control Flow

```
1. User logs in with credentials
   ↓
2. Backend validates credentials
   ↓
3. Returns user data with role and permissions
   ↓
4. Frontend stores tokens and user data
   ↓
5. Router checks user role
   ↓
6. Redirects to appropriate layout based on role
   ↓
7. Navigation guard validates access on each route
   ↓
8. Layout renders with role-specific features
```

## Security Features

### 1. Route Protection
- All routes require authentication except `/login`
- Role-specific route guards prevent unauthorized access
- Automatic redirect to appropriate layout on failed access

### 2. Permission Checking
```javascript
// Check if user has specific permission
authStore.hasPermission('user:create')

// Check user's role
authStore.getUserRole // Returns role name

// Role-specific checks
authStore.isAdmin
authStore.isIT
authStore.isBaoTri
authStore.isBaoVe
authStore.isQuanLyTrai
```

### 3. API Authorization
- JWT tokens required for all protected endpoints
- Backend validates user role and permissions
- Endpoints return 403 Forbidden for unauthorized access

## Demo Credentials

```bash
# SuperAdmin - Full system access
Username: superadmin
Password: super123
Layout: AdminLayout (/admin/dashboard)

# Admin - User/role management
Username: admin
Password: admin123
Layout: AdminLayout (/admin/dashboard)

# IT Staff - System administration
Username: it_staff
Password: it123
Layout: SystemLayout (/system/dashboard)

# Bảo Trì - Maintenance monitoring
Username: bao_tri
Password: baotri123
Layout: MonitorLayout (/monitor/dashboard)

# Bảo Vệ - Security guard kiosk
Username: bao_ve
Password: baove123
Layout: KioskLayout (/kiosk/display)

# Quản Lý Trại - Site manager kiosk
Username: quan_ly
Password: quanly123
Layout: KioskLayout (/kiosk/display)

# User - General access
Username: user
Password: user123
Layout: MonitorLayout (/monitor/dashboard)
```

## Adding New Roles

### Backend (init_db.py):

```python
# 1. Add new permissions if needed
{"name": "new:permission", "description": "Description"}

# 2. Create new role
new_role = Role(name="new_role", description="Description")
new_role.permissions = [selected_permissions]
db.add(new_role)

# 3. Create demo user
new_user = User(
    username="new_user",
    email="newuser@example.com",
    full_name="New User",
    hashed_password=get_password_hash("password"),
    role_id=new_role.id,
    is_active=True
)
db.add(new_user)
```

### Frontend (stores/auth.js):

```javascript
// Add role checker
const isNewRole = computed(() => {
  return getUserRole.value === 'new_role'
})

// Update getDefaultRoute()
if (role === 'new_role') {
  return '/new-layout/dashboard'
}
```

### Router (router/index.js):

```javascript
{
  path: '/new-layout',
  component: () => import('../layouts/NewLayout.vue'),
  meta: { requiresAuth: true, requiresRoles: ['new_role'] },
  children: [...]
}
```

## Best Practices

1. **Least Privilege Principle**
   - Grant only necessary permissions
   - Regular permission audits
   - Remove unused permissions

2. **Role Separation**
   - Keep roles focused and distinct
   - Avoid permission overlap unless necessary
   - Document role responsibilities

3. **Testing**
   - Test each role's access thoroughly
   - Verify permission enforcement
   - Check route protection

4. **Maintenance**
   - Regular role reviews
   - Update permissions as features evolve
   - Keep documentation current

## Troubleshooting

### User can't access expected pages
- Check user's role in database
- Verify role has required permissions
- Check route's `requiresRoles` meta

### Unauthorized access errors
- Verify JWT token is valid
- Check token expiration
- Ensure user is active (`is_active = true`)

### Wrong layout displayed
- Check `getDefaultRoute()` logic
- Verify router navigation guards
- Clear browser cache and localStorage

# Layout Architecture

## Overview

The application implements a **role-based layout system** where each user role is automatically assigned a specific layout based on their responsibilities. This ensures optimal user experience and interface appropriateness for each role.

## Role-to-Layout Mapping

| Role | Layout | Path | Purpose |
|------|--------|------|---------|
| **SuperAdmin** | AdminLayout | `/admin/*` | Full system administration |
| **Admin** | AdminLayout | `/admin/*` | User and role management |
| **IT Staff** | SystemLayout | `/system/*` | System configuration and monitoring |
| **Bảo Trì** | MonitorLayout | `/monitor/*` | Maintenance monitoring dashboard |
| **Bảo Vệ** | KioskLayout | `/kiosk/*` | Security guard kiosk display |
| **Quản Lý Trại** | KioskLayout | `/kiosk/*` | Site manager kiosk display |
| **User** | MonitorLayout | `/monitor/*` | General monitoring access |

## Available Layouts

### 1. **AdminLayout** (Sakai-inspired)
**Path**: `layouts/AdminLayout.vue`

**Assigned to**: SuperAdmin, Admin

**Purpose**: Full-featured administration panel with sidebar navigation

**Features**:
- Collapsible sidebar with menu groups
- Nested menu support
- User profile section
- Topbar with notifications and quick actions
- Responsive design
- Gradient color scheme (inspired by SakaiVue)

**Best for**:
- Admin users managing the system
- Complex workflows requiring multiple pages
- Full CRUD operations

**Routes**:
- `/admin/dashboard` - Admin overview
- `/admin/users` - User management
- `/admin/roles` - Role & permission management
- `/admin/settings` - System settings
- `/admin/logs` - System logs
- `/admin/analytics` - Analytics dashboard

**Color Scheme**: Dark gradient (2c3e50 → 34495e) with purple accents

---

### 2. **MonitorLayout** (TV Screen / Real-time Feed)
**Path**: `layouts/MonitorLayout.vue`

**Assigned to**: Bảo Trì (Maintenance), User

**Purpose**: Real-time monitoring dashboard optimized for large displays

**Features**:
- Fullwidth design with minimal chrome
- Live clock display
- Auto-refreshing content
- Minimal navigation
- High-contrast for visibility
- Status indicators

**Best for**:
- Regular users monitoring data
- TV/Large screen displays
- Control rooms
- Real-time data feeds
- KPI dashboards

**Routes**:
- `/monitor/dashboard` - Real-time monitoring dashboard
- `/monitor/profile` - User profile

**Color Scheme**: Blue gradient (1e3c72 → 2a5298) with glassmorphism effects

---

### 3. **SystemLayout** (Admin Variant)
**Path**: `layouts/SystemLayout.vue`

**Assigned to**: IT Staff

**Purpose**: System administration with deeper technical focus

**Features**:
- Similar to AdminLayout but with system-specific styling
- Service status monitoring
- System health metrics
- Log viewing
- Configuration management
- Notification badge system

**Best for**:
- System administrators
- DevOps teams
- Infrastructure management
- Service monitoring

**Routes**:
- `/system/dashboard` - System overview
- `/system/services` - Service management
- `/system/logs` - System logs
- `/system/settings` - System configuration

**Color Scheme**: Deep blue gradient (1a237e → 283593)

---

### 4. **KioskLayout** (Fullscreen)
**Path**: `layouts/KioskLayout.vue`

**Assigned to**: Bảo Vệ (Security Guard), Quản Lý Trại (Site Manager)

**Purpose**: Fullscreen kiosk mode for public displays or dedicated terminals

**Features**:
- Fullscreen toggle
- Minimal UI with auto-hide controls
- Mouse move to show controls
- Time display (auto-hide after 3 seconds)
- Clean, distraction-free interface
- Exit fullscreen capability

**Best for**:
- Public kiosks
- Information displays
- Trade show booths
- Retail displays
- Reception areas

**Routes**:
- `/kiosk/display` - Kiosk display mode

**Color Scheme**: Pure black background with minimal white UI

---

## Layout Selection Logic

### Automatic Role-Based Routing:

```javascript
// After login, user is automatically redirected based on role:

if (role === 'superadmin' || role === 'admin') {
  redirect to '/admin/dashboard'  // AdminLayout
}

if (role === 'it') {
  redirect to '/system/dashboard'  // SystemLayout
}

if (role === 'bao_tri') {
  redirect to '/monitor/dashboard'  // MonitorLayout
}

if (role === 'bao_ve' || role === 'quan_ly_trai') {
  redirect to '/kiosk/display'  // KioskLayout
}

// Default for other roles
redirect to '/monitor/dashboard'
```

### Access Control:

Routes are protected by role requirements. Users cannot access layouts they don't have permission for:

- `/admin/*` → AdminLayout (superadmin, admin only)
- `/system/*` → SystemLayout (it only)
- `/monitor/*` → MonitorLayout (bao_tri, user)
- `/kiosk/*` → KioskLayout (bao_ve, quan_ly_trai only)

## Usage Examples

### 1. SuperAdmin/Admin Login
```
User logs in with admin/superadmin role
→ Auto-redirect to /admin/dashboard
→ AdminLayout with full sidebar
→ Access to user/role management
→ Full CRUD operations
```

### 2. IT Staff Login
```
User logs in with IT role
→ Auto-redirect to /system/dashboard
→ SystemLayout with system focus
→ Access to system configuration
→ Service monitoring & logs
```

### 3. Bảo Trì (Maintenance) Login
```
User logs in with bao_tri role
→ Auto-redirect to /monitor/dashboard
→ MonitorLayout with real-time feed
→ Maintenance monitoring dashboard
→ Equipment status tracking
```

### 4. Bảo Vệ (Security Guard) Login
```
User logs in with bao_ve role
→ Auto-redirect to /kiosk/display
→ KioskLayout fullscreen mode
→ Security monitoring display
→ Access control interface
```

### 5. Quản Lý Trại (Site Manager) Login
```
User logs in with quan_ly_trai role
→ Auto-redirect to /kiosk/display
→ KioskLayout with management view
→ Site overview dashboard
→ Staff and resource monitoring
```

## Adding New Layouts

### Step 1: Create Layout Component
Create new file in `layouts/YourLayout.vue`:

```vue
<template>
  <div class="your-layout">
    <div class="your-header">
      <!-- Header content -->
    </div>
    <div class="your-content">
      <router-view />
    </div>
  </div>
</template>

<script setup>
// Layout logic
</script>

<style scoped>
/* Layout styles */
</style>
```

### Step 2: Add Routes
In `router/index.js`:

```javascript
{
  path: '/your-path',
  component: () => import('../layouts/YourLayout.vue'),
  meta: { requiresAuth: true },
  children: [
    {
      path: 'page1',
      name: 'YourPage1',
      component: () => import('../views/YourPage1.vue')
    }
  ]
}
```

### Step 3: Update Navigation Guards
Add any special logic in `router.beforeEach()` if needed.

## Layout Comparison

| Feature | AdminLayout | MonitorLayout | SystemLayout | KioskLayout |
|---------|-------------|---------------|--------------|-------------|
| Sidebar | ✅ Collapsible | ❌ No | ✅ Fixed | ❌ No |
| Topbar | ✅ Yes | ✅ Minimal | ✅ Full | ✅ Auto-hide |
| Fullscreen | ❌ No | ❌ No | ❌ No | ✅ Yes |
| Real-time | ⚠️ Partial | ✅ Yes | ⚠️ Metrics | ✅ Yes |
| Mobile | ✅ Responsive | ✅ Responsive | ✅ Responsive | ❌ Desktop only |
| User Profile | ✅ Yes | ✅ Minimal | ✅ Yes | ❌ No |
| Notifications | ✅ Badge | ⚠️ Tag | ✅ Badge | ❌ No |

## Best Practices

1. **Choose the right layout for the use case**
   - Admin tasks → AdminLayout
   - Monitoring → MonitorLayout
   - System ops → SystemLayout
   - Public display → KioskLayout

2. **Consistent navigation patterns**
   - Use `router.push()` for programmatic navigation
   - Let guards handle redirects
   - Respect `requiresAuth` and `requiresAdmin` meta

3. **Performance considerations**
   - MonitorLayout: Use intervals for real-time updates
   - KioskLayout: Minimize DOM updates
   - AdminLayout: Lazy load heavy components

4. **Accessibility**
   - Ensure keyboard navigation works
   - Proper ARIA labels
   - Color contrast ratios
   - Screen reader support

## Demo Accounts

Test each layout with these accounts:

| Username | Password | Role | Layout | Description |
|----------|----------|------|--------|-------------|
| `superadmin` | `super123` | SuperAdmin | AdminLayout | Full system access |
| `admin` | `admin123` | Admin | AdminLayout | User/role management |
| `it_staff` | `it123` | IT Staff | SystemLayout | System administration |
| `bao_tri` | `baotri123` | Bảo Trì | MonitorLayout | Maintenance monitoring |
| `bao_ve` | `baove123` | Bảo Vệ | KioskLayout | Security guard kiosk |
| `quan_ly` | `quanly123` | Quản Lý Trại | KioskLayout | Site manager kiosk |
| `user` | `user123` | User | MonitorLayout | General user access |

## Future Layout Ideas

- **MobileLayout**: Optimized for mobile devices
- **TabletLayout**: Touch-optimized for tablets
- **DashboardLayout**: Widget-based customizable dashboard
- **CompactLayout**: Minimal space for embedded views
- **PrintLayout**: Print-optimized views

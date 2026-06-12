import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '../stores/auth'

const routes = [
  {
    path: '/',
    redirect: () => {
      const authStore = useAuthStore()
      if (!authStore.isAuthenticated) return '/login'
      return authStore.getDefaultRoute()
    }
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/LoginView.vue'),
    meta: { layout: 'auth', requiresAuth: false }
  },
  // Admin Layout (for Admin & SuperAdmin roles)
  {
    path: '/admin',
    component: () => import('../layouts/AdminLayout.vue'),
    meta: { requiresAuth: true, requiresRoles: ['admin', 'superadmin'] },
    children: [
      {
        path: 'dashboard',
        name: 'AdminDashboard',
        component: () => import('../views/admin/AdminDashboardView.vue')
      },
      {
        path: 'users',
        name: 'UserManagement',
        component: () => import('../views/admin/UserManagementView.vue')
      },
      {
        path: 'roles',
        name: 'RoleManagement',
        component: () => import('../views/admin/RoleManagementView.vue')
      },
      {
        path: 'profile',
        name: 'AdminProfile',
        component: () => import('../views/ProfileView.vue')
      }
    ]
  },
  // System Layout (for IT role)
  {
    path: '/system',
    component: () => import('../layouts/SystemLayout.vue'),
    meta: { requiresAuth: true, requiresRoles: ['it'] },
    children: [
      {
        path: 'dashboard',
        name: 'SystemDashboard',
        component: () => import('../views/admin/AdminDashboardView.vue')
      }
    ]
  },
  // Monitor Layout (for Bảo Trì role)
  {
    path: '/monitor',
    component: () => import('../layouts/MonitorLayout.vue'),
    meta: { requiresAuth: true, requiresRoles: ['bao_tri'] },
    children: [
      {
        path: 'dashboard',
        name: 'MonitorDashboard',
        component: () => import('../views/DashboardView.vue')
      },
      {
        path: 'profile',
        name: 'UserProfile',
        component: () => import('../views/ProfileView.vue')
      }
    ]
  },
  // Kiosk Layout (for Bảo Vệ & Quản Lý Trại roles)
  {
    path: '/kiosk',
    component: () => import('../layouts/KioskLayout.vue'),
    meta: { requiresAuth: true, requiresRoles: ['bao_ve', 'quan_ly_trai'] },
    redirect: '/kiosk/dashboard',
    children: [
      {
        path: 'dashboard',
        name: 'KioskDashboard',
        component: () => import('../views/kiosk/KioskDashboard.vue')
      },
      {
        path: 'issue-card',
        name: 'KioskIssueCard',
        component: () => import('../views/kiosk/KioskIssueCard.vue')
      },
      {
        path: 'return-card',
        name: 'KioskReturnCard',
        component: () => import('../views/kiosk/KioskReturnCard.vue')
      },
      {
        path: 'report-lost',
        name: 'KioskReportLost',
        component: () => import('../views/kiosk/KioskReportLost.vue')
      },
      {
        path: 'search',
        name: 'KioskSearch',
        component: () => import('../views/kiosk/KioskSearch.vue')
      }
    ]
  },
  // Legacy redirects for backward compatibility
  {
    path: '/dashboard',
    redirect: () => {
      const authStore = useAuthStore()
      return authStore.getDefaultRoute()
    }
  },
  {
    path: '/profile',
    redirect: '/monitor/profile'
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: () => import('../views/NotFoundView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// Navigation guard
router.beforeEach((to, from, next) => {
  const authStore = useAuthStore()
  authStore.loadTokens()

  // Check authentication
  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    next({ name: 'Login', query: { redirect: to.fullPath } })
    return
  }

  // Check role-based access
  if (to.meta.requiresRoles && authStore.isAuthenticated) {
    const userRole = authStore.getUserRole
    const allowedRoles = to.meta.requiresRoles
    const defaultRoute = authStore.getDefaultRoute()

    if (!allowedRoles.includes(userRole)) {
      if (!userRole) {
        authStore.clearTokens()
        next({ name: 'Login', query: { redirect: to.fullPath } })
        return
      }

      if (to.path !== defaultRoute) {
        next(defaultRoute)
        return
      }

      next({ name: 'Login', query: { redirect: to.fullPath } })
      return
    }
  }

  // Redirect authenticated users away from login
  if (to.name === 'Login' && authStore.isAuthenticated) {
    next(authStore.getDefaultRoute())
    return
  }

  next()
})

export default router

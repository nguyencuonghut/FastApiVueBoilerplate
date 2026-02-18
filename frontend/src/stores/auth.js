import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useAuthStore = defineStore('auth', () => {
  const user = ref(null)
  const accessToken = ref(null)
  const refreshToken = ref(null)
  const isAuthenticated = computed(() => !!accessToken.value)

  // Load tokens from localStorage
  const loadTokens = () => {
    const storedAccessToken = localStorage.getItem('access_token')
    const storedRefreshToken = localStorage.getItem('refresh_token')
    const storedUser = localStorage.getItem('user')

    if (storedAccessToken) {
      accessToken.value = storedAccessToken
      refreshToken.value = storedRefreshToken
      user.value = JSON.parse(storedUser)
    }
  }

  // Store tokens in localStorage
  const storeTokens = (tokens) => {
    accessToken.value = tokens.access_token
    refreshToken.value = tokens.refresh_token
    user.value = tokens.user
    
    localStorage.setItem('access_token', tokens.access_token)
    localStorage.setItem('refresh_token', tokens.refresh_token)
    localStorage.setItem('user', JSON.stringify(tokens.user))
  }

  // Clear tokens
  const clearTokens = () => {
    user.value = null
    accessToken.value = null
    refreshToken.value = null
    
    localStorage.removeItem('access_token')
    localStorage.removeItem('refresh_token')
    localStorage.removeItem('user')
  }

  // Get user role
  const getUserRole = computed(() => {
    return user.value?.role?.name || null
  })

  // Check if user is admin or superadmin
  const isAdmin = computed(() => {
    const role = getUserRole.value
    return role === 'admin' || role === 'superadmin'
  })

  // Check if user is IT staff
  const isIT = computed(() => {
    return getUserRole.value === 'it'
  })

  // Check if user is Bảo Trì (Maintenance)
  const isBaoTri = computed(() => {
    return getUserRole.value === 'bao_tri'
  })

  // Check if user is Bảo Vệ (Security Guard)
  const isBaoVe = computed(() => {
    return getUserRole.value === 'bao_ve'
  })

  // Check if user is Quản Lý Trại (Site Manager)
  const isQuanLyTrai = computed(() => {
    return getUserRole.value === 'quan_ly_trai'
  })

  // Check if user should use Kiosk layout
  const useKioskLayout = computed(() => {
    const role = getUserRole.value
    return role === 'bao_ve' || role === 'quan_ly_trai'
  })

  // Get default route based on role
  const getDefaultRoute = () => {
    const role = getUserRole.value
    
    // Admin and SuperAdmin → AdminLayout
    if (role === 'admin' || role === 'superadmin') {
      return '/admin/dashboard'
    }
    
    // IT Staff → SystemLayout
    if (role === 'it') {
      return '/system/dashboard'
    }
    
    // Bảo Trì → MonitorLayout
    if (role === 'bao_tri') {
      return '/monitor/dashboard'
    }
    
    // Bảo Vệ & Quản Lý Trại → KioskLayout
    if (role === 'bao_ve' || role === 'quan_ly_trai') {
      return '/kiosk/dashboard'
    }
    
    // Default for other roles
    return '/monitor/dashboard'
  }

  // Check if user has permission
  const hasPermission = (permission) => {
    return user.value?.role?.permissions?.some(p => p.name === permission) || false
  }

  return {
    user,
    accessToken,
    refreshToken,
    isAuthenticated,
    loadTokens,
    storeTokens,
    clearTokens,
    getUserRole,
    isAdmin,
    isIT,
    isBaoTri,
    isBaoVe,
    isQuanLyTrai,
    useKioskLayout,
    getDefaultRoute,
    hasPermission
  }
})

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

  // Check if user is admin
  const isAdmin = computed(() => {
    return getUserRole.value === 'admin'
  })

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
    hasPermission
  }
})

import axios from 'axios'
import { useAuthStore } from '../stores/auth'

const rawApiUrl = import.meta.env.VITE_API_URL
const API_BASE_URL = typeof rawApiUrl === 'string' && rawApiUrl.startsWith('/') ? rawApiUrl : '/api'

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json'
  }
})

// Add interceptor to include auth token
apiClient.interceptors.request.use((config) => {
  const authStore = useAuthStore()
  if (authStore.accessToken) {
    config.headers.Authorization = `Bearer ${authStore.accessToken}`
  }
  return config
}, (error) => {
  return Promise.reject(error)
})

// Handle token refresh on 401
apiClient.interceptors.response.use(
  (response) => response,
  async (error) => {
    const authStore = useAuthStore()
    const originalRequest = error.config

    if (error.response?.status === 401 && authStore.refreshToken && !originalRequest._retry) {
      originalRequest._retry = true

      try {
        const response = await axios.post(`${API_BASE_URL}/auth/refresh`, {
          refresh_token: authStore.refreshToken
        })
        
        authStore.storeTokens(response.data)
        originalRequest.headers.Authorization = `Bearer ${response.data.access_token}`
        return apiClient(originalRequest)
      } catch (refreshError) {
        authStore.clearTokens()
        window.location.href = '/login'
        return Promise.reject(refreshError)
      }
    }

    return Promise.reject(error)
  }
)

export default apiClient

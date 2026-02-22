import apiClient from './api'

const AUTH_API = '/auth'
const USERS_API = '/users'
const ADMIN_API = '/admin'

export const authService = {
  // Login
  login: (email, password) => {
    return apiClient.post(`${AUTH_API}/login`, { email, password })
  },

  // Refresh token
  refreshToken: (refreshToken) => {
    return apiClient.post(`${AUTH_API}/refresh`, { refresh_token: refreshToken })
  }
}

export const userService = {
  // Get current user
  getCurrentUser: () => {
    return apiClient.get(`${USERS_API}/me`)
  },

  // Update current user
  updateProfile: (data) => {
    return apiClient.put(`${USERS_API}/me`, data)
  },

  // Change password
  changePassword: (currentPassword, newPassword) => {
    return apiClient.post(`${USERS_API}/change-password`, {
      current_password: currentPassword,
      new_password: newPassword
    })
  }
}

export const adminService = {
  // List all users with pagination and search
  listUsers: (skip = 0, limit = 10, search = '') => {
    return apiClient.get(`${ADMIN_API}/users`, {
      params: { skip, limit, search: search || undefined }
    })
  },

  // Get specific user
  getUser: (userId) => {
    return apiClient.get(`${ADMIN_API}/users/${userId}`)
  },

  // Create user
  createUser: (userData) => {
    return apiClient.post(`${ADMIN_API}/users`, userData)
  },

  // Delete/deactivate user
  deactivateUser: (userId) => {
    return apiClient.delete(`${ADMIN_API}/users/${userId}`)
  },

  // Restore user
  restoreUser: (userId) => {
    return apiClient.put(`${ADMIN_API}/users/${userId}/restore`)
  },

  // Delete user permanently
  deleteUserPermanently: (userId) => {
    return apiClient.delete(`${ADMIN_API}/users/${userId}/permanent`)
  },

  // List roles
  listRoles: () => {
    return apiClient.get(`${ADMIN_API}/roles`)
  },

  // List permissions
  listPermissions: () => {
    return apiClient.get(`${ADMIN_API}/permissions`)
  }
}

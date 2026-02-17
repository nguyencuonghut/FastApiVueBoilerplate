<template>
  <div class="admin-layout">
    <div class="admin-sidebar">
      <div class="sidebar-header">
        <h2>ADMIN PANEL</h2>
      </div>
      <nav class="sidebar-menu">
        <router-link
          v-for="item in menuItems"
          :key="item.path"
          :to="item.path"
          class="menu-item"
          :class="{ active: $route.path === item.path }"
        >
          <i :class="`pi ${item.icon}`"></i>
          <span>{{ item.label }}</span>
        </router-link>
      </nav>
      <div class="sidebar-footer">
        <Button
          icon="pi pi-sign-out"
          label="Logout"
          class="w-full p-button-danger"
          @click="handleLogout"
        />
      </div>
    </div>

    <div class="admin-content">
      <div class="admin-header">
        <h1>{{ getPageTitle() }}</h1>
        <div class="admin-user-info">
          <span>{{ authStore.user?.full_name || 'Admin' }}</span>
          <Avatar :image="authStore.user?.avatar_url" shape="circle" />
        </div>
      </div>
      <div class="admin-main">
        <router-view />
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter, useRoute } from 'vue-router'
import { useAuthStore } from '../stores/auth'
import Button from 'primevue/button'
import Avatar from 'primevue/avatar'

const router = useRouter()
const route = useRoute()
const authStore = useAuthStore()

const menuItems = [
  { path: '/admin/dashboard', label: 'Dashboard', icon: 'pi-home' },
  { path: '/admin/users', label: 'Users', icon: 'pi-users' },
  { path: '/admin/roles', label: 'Roles', icon: 'pi-shield' }
]

const handleLogout = () => {
  authStore.clearTokens()
  router.push('/login')
}

const getPageTitle = () => {
  const item = menuItems.find(m => m.path === route.path)
  return item?.label || 'Admin Panel'
}
</script>

<style scoped>
.admin-layout {
  display: flex;
  min-height: 100vh;
  background: #f5f7fa;
}

.admin-sidebar {
  width: 250px;
  background: #2c3e50;
  color: white;
  padding: 20px;
  position: fixed;
  height: 100vh;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
}

.sidebar-header {
  margin-bottom: 30px;
  text-align: center;
}

.sidebar-header h2 {
  margin: 0;
  font-size: 18px;
  font-weight: bold;
}

.sidebar-menu {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.menu-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 12px;
  border-radius: 4px;
  color: #ecf0f1;
  text-decoration: none;
  transition: all 0.2s;
}

.menu-item:hover,
.menu-item.active {
  background: #34495e;
  color: #3498db;
}

.menu-item i {
  font-size: 16px;
}

.sidebar-footer {
  margin-top: 20px;
  padding-top: 20px;
  border-top: 1px solid #34495e;
}

.admin-content {
  margin-left: 250px;
  flex: 1;
  display: flex;
  flex-direction: column;
}

.admin-header {
  background: white;
  padding: 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.admin-header h1 {
  margin: 0;
  font-size: 24px;
  color: #333;
}

.admin-user-info {
  display: flex;
  align-items: center;
  gap: 10px;
}

.admin-main {
  flex: 1;
  padding: 20px;
  overflow-y: auto;
}
</style>

<template>
  <div class="system-layout">
    <div class="system-sidebar">
      <div class="sidebar-header">
        <i class="pi pi-cog text-2xl"></i>
        <h2>SYSTEM ADMIN</h2>
      </div>
      
      <nav class="sidebar-menu">
        <router-link
          v-for="item in menuItems"
          :key="item.path"
          :to="item.path"
          class="menu-item"
          :class="{ active: isActiveRoute(item.path) }"
        >
          <i :class="`pi ${item.icon}`"></i>
          <span>{{ item.label }}</span>
        </router-link>
      </nav>
      
      <div class="sidebar-footer">
        <div class="user-info mb-3">
          <Avatar :label="authStore.user?.full_name?.charAt(0)" size="large" shape="circle" />
          <div class="ml-2">
            <p class="font-semibold m-0">{{ authStore.user?.full_name }}</p>
            <p class="text-sm m-0 opacity-70">{{ authStore.user?.email }}</p>
          </div>
        </div>
        <Button
          icon="pi pi-sign-out"
          label="Logout"
          class="w-full"
          severity="danger"
          outlined
          @click="handleLogout"
        />
      </div>
    </div>

    <div class="system-content">
      <div class="system-header">
        <div>
          <h1>{{ getPageTitle() }}</h1>
          <p class="text-sm text-secondary m-0">{{ getPageDescription() }}</p>
        </div>
        <div class="header-actions">
          <Button icon="pi pi-bell" text rounded :badge="notificationCount" badge-severity="danger" />
          <Button icon="pi pi-cog" text rounded />
        </div>
      </div>
      
      <div class="system-main">
        <router-view />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useAuthStore } from '../stores/auth'
import Button from 'primevue/button'
import Avatar from 'primevue/avatar'

const router = useRouter()
const route = useRoute()
const authStore = useAuthStore()

const notificationCount = ref('3')

const menuItems = [
  { 
    path: '/system/dashboard', 
    label: 'System Dashboard', 
    icon: 'pi-chart-line',
    description: 'System overview and metrics'
  }
]

const isActiveRoute = (path) => {
  // Check if current route path starts with menu item path
  // This supports nested routes
  return route.path === path || route.path.startsWith(path + '/')
}

const handleLogout = () => {
  authStore.clearTokens()
  router.push('/login')
}

const getPageTitle = () => {
  const item = menuItems.find(m => m.path === route.path)
  return item?.label || 'System Admin'
}

const getPageDescription = () => {
  const item = menuItems.find(m => m.path === route.path)
  return item?.description || 'System administration panel'
}
</script>

<style scoped>
.system-layout {
  display: flex;
  min-height: 100vh;
  background: #f8f9fa;
}

.system-sidebar {
  width: 280px;
  background: linear-gradient(180deg, #1a237e 0%, #283593 100%);
  color: white;
  padding: 1.5rem;
  position: fixed;
  height: 100vh;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  box-shadow: 4px 0 10px rgba(0, 0, 0, 0.1);
}

.sidebar-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 2rem;
  padding-bottom: 1.5rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.2);
}

.sidebar-header h2 {
  margin: 0;
  font-size: 1.25rem;
  font-weight: 700;
  letter-spacing: 0.05em;
}

.sidebar-menu {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.menu-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 0.875rem 1rem;
  border-radius: 8px;
  color: rgba(255, 255, 255, 0.8);
  text-decoration: none;
  transition: all 0.2s;
  font-weight: 500;
}

.menu-item:hover {
  background: rgba(255, 255, 255, 0.1);
  color: white;
  transform: translateX(4px);
}

.menu-item.active {
  background: rgba(255, 255, 255, 0.15);
  color: white;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
}

.menu-item i {
  font-size: 1.25rem;
}

.sidebar-footer {
  margin-top: auto;
  padding-top: 1.5rem;
  border-top: 1px solid rgba(255, 255, 255, 0.2);
}

.user-info {
  display: flex;
  align-items: center;
}

.system-content {
  margin-left: 280px;
  flex: 1;
  display: flex;
  flex-direction: column;
}

.system-header {
  background: white;
  padding: 1.5rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  z-index: 10;
}

.system-header h1 {
  margin: 0;
  font-size: 1.75rem;
  color: #1a237e;
  font-weight: 700;
}

.header-actions {
  display: flex;
  gap: 0.5rem;
}

.system-main {
  flex: 1;
  padding: 2rem;
  overflow-y: auto;
}

/* Responsive */
@media (max-width: 768px) {
  .system-sidebar {
    width: 240px;
  }
  
  .system-content {
    margin-left: 240px;
  }
}
</style>

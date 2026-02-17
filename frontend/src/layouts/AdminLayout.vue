<template>
  <div class="admin-layout">
    <!-- Sidebar -->
    <div class="admin-sidebar" :class="{ collapsed: sidebarCollapsed }">
      <div class="sidebar-header">
        <div class="logo">
          <i class="pi pi-prime text-3xl"></i>
          <h2 v-if="!sidebarCollapsed">SAKAI</h2>
        </div>
        <Button
          :icon="sidebarCollapsed ? 'pi pi-angle-right' : 'pi pi-angle-left'"
          text
          rounded
          class="collapse-btn"
          @click="toggleSidebar"
        />
      </div>

      <nav class="sidebar-menu">
        <template v-for="item in menuItems" :key="item.path">
          <!-- Menu with children -->
          <div v-if="item.children" class="menu-group">
            <div class="menu-item" @click="toggleMenuItem(item)">
              <div class="menu-item-content">
                <i :class="`pi ${item.icon}`"></i>
                <span v-if="!sidebarCollapsed">{{ item.label }}</span>
              </div>
              <i
                v-if="!sidebarCollapsed"
                :class="`pi ${item.expanded ? 'pi-angle-down' : 'pi-angle-right'}`"
                class="submenu-icon"
              ></i>
            </div>
            <div v-if="item.expanded && !sidebarCollapsed" class="submenu">
              <router-link
                v-for="child in item.children"
                :key="child.path"
                :to="child.path"
                class="submenu-item"
                :class="{ active: $route.path === child.path }"
              >
                <i :class="`pi ${child.icon}`"></i>
                <span>{{ child.label }}</span>
              </router-link>
            </div>
          </div>

          <!-- Single menu item -->
          <router-link
            v-else
            :to="item.path"
            class="menu-item"
            :class="{ active: $route.path === item.path }"
          >
            <div class="menu-item-content">
              <i :class="`pi ${item.icon}`"></i>
              <span v-if="!sidebarCollapsed">{{ item.label }}</span>
            </div>
          </router-link>
        </template>
      </nav>

      <div class="sidebar-footer" v-if="!sidebarCollapsed">
        <div class="user-profile">
          <Avatar
            :label="authStore.user?.full_name?.charAt(0)"
            size="large"
            shape="circle"
            class="user-avatar"
          />
          <div class="user-details">
            <p class="user-name">{{ authStore.user?.full_name }}</p>
            <p class="user-role">{{ authStore.user?.role?.name }}</p>
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

    <!-- Main Content -->
    <div class="admin-content" :class="{ expanded: sidebarCollapsed }">
      <!-- Topbar -->
      <div class="admin-topbar">
        <div class="topbar-left">
          <h1 class="page-title">{{ getPageTitle() }}</h1>
        </div>
        <div class="topbar-right">
          <Button icon="pi pi-search" text rounded />
          <Button icon="pi pi-bell" text rounded badge="3" badge-severity="danger" />
          <Button icon="pi pi-cog" text rounded />
          <Avatar
            v-if="sidebarCollapsed"
            :label="authStore.user?.full_name?.charAt(0)"
            shape="circle"
          />
        </div>
      </div>

      <!-- Page Content -->
      <div class="admin-main">
        <router-view />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useAuthStore } from '../stores/auth'
import Button from 'primevue/button'
import Avatar from 'primevue/avatar'

const router = useRouter()
const route = useRoute()
const authStore = useAuthStore()

const sidebarCollapsed = ref(false)

const menuItems = ref([
  { 
    path: '/admin/dashboard', 
    label: 'Dashboard', 
    icon: 'pi-home'
  },
  {
    label: 'User Management',
    icon: 'pi-users',
    expanded: false,
    children: [
      { path: '/admin/users', label: 'Users', icon: 'pi-user' },
      { path: '/admin/roles', label: 'Roles & Permissions', icon: 'pi-shield' }
    ]
  },
  {
    label: 'System',
    icon: 'pi-cog',
    expanded: false,
    children: [
      { path: '/admin/settings', label: 'Settings', icon: 'pi-sliders-h' },
      { path: '/admin/logs', label: 'Logs', icon: 'pi-file' }
    ]
  },
  { 
    path: '/admin/analytics', 
    label: 'Analytics', 
    icon: 'pi-chart-bar'
  }
])

const toggleSidebar = () => {
  sidebarCollapsed.value = !sidebarCollapsed.value
}

const toggleMenuItem = (item) => {
  item.expanded = !item.expanded
}

const handleLogout = () => {
  authStore.clearTokens()
  router.push('/login')
}

const getPageTitle = () => {
  // Find in flat menu items
  const flatItem = menuItems.value.find(m => m.path === route.path)
  if (flatItem) return flatItem.label

  // Find in nested menu items
  for (const item of menuItems.value) {
    if (item.children) {
      const child = item.children.find(c => c.path === route.path)
      if (child) return child.label
    }
  }

  return 'Admin Panel'
}
</script>

<style scoped>
.admin-layout {
  display: flex;
  min-height: 100vh;
  background: #f8f9fa;
}

/* Sidebar */
.admin-sidebar {
  width: 280px;
  background: linear-gradient(180deg, #2c3e50 0%, #34495e 100%);
  color: white;
  position: fixed;
  height: 100vh;
  overflow-y: auto;
  overflow-x: hidden;
  display: flex;
  flex-direction: column;
  box-shadow: 4px 0 10px rgba(0, 0, 0, 0.1);
  transition: width 0.3s ease;
  z-index: 100;
}

.admin-sidebar.collapsed {
  width: 80px;
}

.sidebar-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem 1.25rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.logo {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.logo h2 {
  margin: 0;
  font-size: 1.5rem;
  font-weight: 700;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.collapsed .logo h2 {
  display: none;
}

.collapse-btn {
  color: white !important;
}

/* Menu */
.sidebar-menu {
  flex: 1;
  padding: 1rem 0.5rem;
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.menu-group {
  margin-bottom: 0.5rem;
}

.menu-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.875rem 1rem;
  border-radius: 8px;
  color: rgba(255, 255, 255, 0.8);
  text-decoration: none;
  transition: all 0.2s ease;
  cursor: pointer;
  font-weight: 500;
}

.menu-item-content {
  display: flex;
  align-items: center;
  gap: 0.875rem;
}

.menu-item:hover {
  background: rgba(255, 255, 255, 0.1);
  color: white;
  transform: translateX(4px);
}

.menu-item.active {
  background: rgba(103, 126, 234, 0.2);
  color: #667eea;
  box-shadow: 0 2px 8px rgba(103, 126, 234, 0.3);
}

.menu-item i {
  font-size: 1.125rem;
  min-width: 1.125rem;
}

.submenu-icon {
  font-size: 0.875rem;
  transition: transform 0.2s;
}

.submenu {
  margin-left: 1rem;
  margin-top: 0.25rem;
  padding-left: 1rem;
  border-left: 2px solid rgba(255, 255, 255, 0.1);
}

.submenu-item {
  display: flex;
  align-items: center;
  gap: 0.875rem;
  padding: 0.75rem 1rem;
  border-radius: 6px;
  color: rgba(255, 255, 255, 0.7);
  text-decoration: none;
  transition: all 0.2s;
  font-size: 0.9rem;
}

.submenu-item:hover {
  background: rgba(255, 255, 255, 0.05);
  color: white;
}

.submenu-item.active {
  background: rgba(103, 126, 234, 0.15);
  color: #667eea;
}

.submenu-item i {
  font-size: 0.875rem;
}

/* Sidebar Footer */
.sidebar-footer {
  padding: 1.5rem 1rem;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.user-profile {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1rem;
  padding: 0.75rem;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 8px;
}

.user-avatar {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.user-details {
  flex: 1;
  overflow: hidden;
}

.user-name {
  margin: 0;
  font-weight: 600;
  font-size: 0.9rem;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.user-role {
  margin: 0;
  font-size: 0.75rem;
  opacity: 0.7;
  text-transform: uppercase;
}

/* Main Content */
.admin-content {
  margin-left: 280px;
  flex: 1;
  display: flex;
  flex-direction: column;
  transition: margin-left 0.3s ease;
}

.admin-content.expanded {
  margin-left: 80px;
}

/* Topbar */
.admin-topbar {
  background: white;
  padding: 1rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  z-index: 50;
  position: sticky;
  top: 0;
}

.page-title {
  margin: 0;
  font-size: 1.75rem;
  font-weight: 700;
  color: #2c3e50;
}

.topbar-right {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

/* Main Area */
.admin-main {
  flex: 1;
  padding: 2rem;
  overflow-y: auto;
}

/* Scrollbar */
.admin-sidebar::-webkit-scrollbar,
.admin-main::-webkit-scrollbar {
  width: 6px;
}

.admin-sidebar::-webkit-scrollbar-track {
  background: rgba(255, 255, 255, 0.05);
}

.admin-sidebar::-webkit-scrollbar-thumb {
  background: rgba(255, 255, 255, 0.2);
  border-radius: 3px;
}

.admin-sidebar::-webkit-scrollbar-thumb:hover {
  background: rgba(255, 255, 255, 0.3);
}

/* Responsive */
@media (max-width: 768px) {
  .admin-sidebar {
    width: 240px;
  }
  
  .admin-content {
    margin-left: 240px;
  }
  
  .admin-sidebar.collapsed {
    width: 0;
    padding: 0;
  }
  
  .admin-content.expanded {
    margin-left: 0;
  }
}
</style>

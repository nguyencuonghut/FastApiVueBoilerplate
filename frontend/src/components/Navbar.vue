<template>
  <div class="navbar p-3 surface-ground" style="box-shadow: 0 2px 4px rgba(0,0,0,0.1)">
    <div class="flex align-items-center justify-content-between">
      <div class="flex align-items-center gap-3">
        <h3 class="m-0">{{ getPageTitle() }}</h3>
      </div>

      <div class="flex align-items-center gap-3">
        <router-link to="/profile" class="p-button p-button-text">
          <i class="pi pi-user"></i>
          {{ authStore.user?.full_name || 'Profile' }}
        </router-link>

        <Menu ref="menu" :model="menuItems" :popup="true" />
        <Button
          icon="pi pi-ellipsis-v"
          class="p-button-rounded p-button-text"
          @click="toggle"
          aria-haspopup="true"
          aria-controls="overlay_menu"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useAuthStore } from '../stores/auth'
import Button from 'primevue/button'
import Menu from 'primevue/menu'

const router = useRouter()
const route = useRoute()
const authStore = useAuthStore()
const menu = ref()

const menuItems = [
  {
    label: 'Profile',
    icon: 'pi pi-user',
    command: () => router.push('/profile')
  },
  {
    label: 'Settings',
    icon: 'pi pi-cog',
    command: () => router.push('/settings')
  },
  { separator: true },
  {
    label: 'Logout',
    icon: 'pi pi-sign-out',
    command: () => handleLogout()
  }
]

const toggle = (event) => {
  menu.value.toggle(event)
}

const handleLogout = () => {
  authStore.clearTokens()
  router.push('/login')
}

const getPageTitle = () => {
  const titles = {
    '/dashboard': 'Dashboard',
    '/profile': 'My Profile',
    '/admin/dashboard': 'Admin Dashboard',
    '/admin/users': 'User Management',
    '/admin/roles': 'Role Management'
  }
  return titles[route.path] || route.path
}
</script>

<style scoped>
.navbar {
  background: white;
}
</style>

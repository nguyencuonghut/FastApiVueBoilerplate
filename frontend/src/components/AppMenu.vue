<template>
  <ul class="layout-menu">
    <template v-for="(item, i) in model" :key="item">
      <app-menu-item 
        v-if="!item.separator" 
        :item="item" 
        :index="i"
      ></app-menu-item>
      <li v-if="item.separator" class="menu-separator"></li>
    </template>
  </ul>
</template>

<script setup>
import { ref } from 'vue'
import AppMenuItem from './AppMenuItem.vue'
import { useAuthStore } from '@/stores/auth'

const authStore = useAuthStore()

const model = ref([
  {
    label: 'Home',
    items: [
      {
        label: 'Dashboard',
        icon: 'pi pi-fw pi-home',
        to: '/admin/dashboard'
      }
    ]
  },
  {
    label: 'Management',
    path: '/management',
    items: [
      {
        label: 'User Management',
        icon: 'pi pi-fw pi-users',
        to: '/admin/users'
      },
      {
        label: 'Role Management',
        icon: 'pi pi-fw pi-shield',
        to: '/admin/roles'
      }
    ]
  },
  {
    label: 'System',
    path: '/system',
    items: [
      {
        label: 'Settings',
        icon: 'pi pi-fw pi-cog',
        to: '/admin/settings'
      },
      {
        label: 'Analytics',
        icon: 'pi pi-fw pi-chart-bar',
        to: '/admin/analytics'
      },
      {
        label: 'Logs',
        icon: 'pi pi-fw pi-file',
        to: '/admin/logs'
      }
    ]
  },
  {
    separator: true
  },
  {
    label: 'Profile',
    items: [
      {
        label: `${authStore.user?.full_name || 'User'}`,
        icon: 'pi pi-fw pi-user',
        to: '/profile'
      },
      {
        label: 'Settings',
        icon: 'pi pi-fw pi-cog',
        to: '/profile/settings'
      }
    ]
  }
])
</script>

<style scoped>
/* Menu styles handled by global SCSS */
</style>

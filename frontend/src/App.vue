<template>
  <div class="app-container" :class="{ 'layout-route': isLayoutRoute }">
    <Navbar v-if="showNavbar && authStore.isAuthenticated && !isLayoutRoute" />
    <router-view />
  </div>
  <Toast />
  <ConfirmDialog />
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { useAuthStore } from './stores/auth'
import Navbar from './components/Navbar.vue'
import Toast from 'primevue/toast'
import ConfirmDialog from 'primevue/confirmdialog'

const route = useRoute()
const authStore = useAuthStore()

authStore.loadTokens()

// Don't show navbar for login, not found, and layout routes
const showNavbar = computed(() => {
  return route.name !== 'Login' && route.name !== 'NotFound'
})

// Check if current route uses a layout
const isLayoutRoute = computed(() => {
  return route.path.startsWith('/admin') || 
         route.path.startsWith('/monitor') || 
         route.path.startsWith('/system') || 
         route.path.startsWith('/kiosk')
})
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html, body, #app {
  height: 100%;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
    'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
    sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  background-color: var(--surface-ground);
  color: var(--text-color);
}

.app-container {
  height: 100vh;
}

.app-container:not(.layout-route) {
  display: flex;
  flex-direction: column;
}

.app-container:not(.layout-route) .main-content {
  flex: 1;
  overflow-y: auto;
}

code {
  font-family: source-code-pro, Menlo, Monaco, Consolas, 'Courier New',
    monospace;
}
</style>

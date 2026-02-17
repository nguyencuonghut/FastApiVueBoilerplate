<template>
  <div class="layout-topbar">
    <div class="layout-topbar-logo-container">
      <button class="layout-menu-button layout-topbar-action" @click="toggleMenu">
        <i class="pi pi-bars"></i>
      </button>
      <router-link to="/admin/dashboard" class="layout-topbar-logo">
        <span>{{ authStore.user?.username }}</span>
      </router-link>
    </div>

    <div class="layout-topbar-actions">
      <button type="button" class="layout-topbar-action" @click="toggleDarkMode" title="Toggle Dark Mode">
        <i :class="['pi', { 'pi-moon': isDarkTheme, 'pi-sun': !isDarkTheme }]"></i>
      </button>

      <!-- Desktop menu - hidden on mobile -->
      <button type="button" class="layout-topbar-action hidden lg:inline-flex" title="Notifications">
        <i class="pi pi-bell"></i>
      </button>
      <button type="button" class="layout-topbar-action hidden lg:inline-flex" title="Profile">
        <i class="pi pi-user"></i>
      </button>
      <button type="button" class="layout-topbar-action hidden lg:inline-flex" @click="handleLogout" title="Logout">
        <i class="pi pi-sign-out"></i>
      </button>

      <!-- Mobile menu button -->
      <button
        type="button"
        class="layout-topbar-action lg:hidden"
        @click="toggleMobileMenu"
      >
        <i class="pi pi-ellipsis-v"></i>
      </button>

      <!-- Mobile dropdown -->
      <div v-if="showMobileMenu" class="layout-topbar-menu-mobile lg:hidden" @click.stop>
        <button type="button" class="mobile-menu-item" @click="handleMobileMenuClick('notifications')">
          <i class="pi pi-bell"></i>
          <span>Notifications</span>
        </button>
        <button type="button" class="mobile-menu-item" @click="handleMobileMenuClick('profile')">
          <i class="pi pi-user"></i>
          <span>Profile</span>
        </button>
        <button type="button" class="mobile-menu-item" @click="handleMobileMenuClick('logout')">
          <i class="pi pi-sign-out"></i>
          <span>Logout</span>
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { useLayout } from '@/composables/layout'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const { toggleMenu, toggleDarkMode, isDarkTheme } = useLayout()
const router = useRouter()
const authStore = useAuthStore()
const showMobileMenu = ref(false)

const toggleMobileMenu = () => {
  showMobileMenu.value = !showMobileMenu.value
}

const handleMobileMenuClick = (action) => {
  showMobileMenu.value = false
  
  if (action === 'logout') {
    handleLogout()
  } else if (action === 'notifications') {
    // Handle notifications
  } else if (action === 'profile') {
    // Handle profile
  }
}

const handleLogout = () => {
  authStore.clearTokens()
  router.push('/login')
}

// Close mobile menu when clicking outside
const handleClickOutside = (event) => {
  const mobileMenu = document.querySelector('.layout-topbar-menu-mobile')
  const mobileMenuButton = event.target.closest('.layout-topbar-action')
  
  if (showMobileMenu.value && mobileMenu && !mobileMenu.contains(event.target) && !mobileMenuButton) {
    showMobileMenu.value = false
  }
}

onMounted(() => {
  document.addEventListener('click', handleClickOutside)
})

onBeforeUnmount(() => {
  document.removeEventListener('click', handleClickOutside)
})
</script>

<style scoped>
/* Add any additional custom styles if needed */
</style>

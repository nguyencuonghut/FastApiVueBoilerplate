<template>
  <div class="kiosk-layout" :class="{ 'fullscreen': isFullscreen }">
    <!-- Minimal Header -->
    <div class="kiosk-header">
      <h1>{{ title }}</h1>
      <div class="kiosk-controls">
        <Button
          :icon="isFullscreen ? 'pi pi-window-minimize' : 'pi pi-window-maximize'"
          text
          rounded
          @click="toggleFullscreen"
        />
        <Button
          icon="pi pi-sign-out"
          text
          rounded
          severity="danger"
          @click="handleLogout"
        />
      </div>
    </div>

    <!-- Fullscreen Content -->
    <div class="kiosk-content">
      <router-view />
    </div>

    <!-- Auto-hide time indicator -->
    <div class="kiosk-time" :class="{ 'show': showTime }">
      {{ currentTime }}
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'
import Button from 'primevue/button'

const router = useRouter()
const authStore = useAuthStore()

const title = ref('Kiosk Mode')
const isFullscreen = ref(false)
const showTime = ref(true)
const currentTime = ref('')

let timeInterval = null
let hideTimeTimeout = null

const updateTime = () => {
  const now = new Date()
  currentTime.value = now.toLocaleString('en-US', {
    weekday: 'long',
    month: 'long',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}

const toggleFullscreen = () => {
  if (!document.fullscreenElement) {
    document.documentElement.requestFullscreen()
    isFullscreen.value = true
  } else {
    if (document.exitFullscreen) {
      document.exitFullscreen()
      isFullscreen.value = false
    }
  }
}

const handleMouseMove = () => {
  showTime.value = true
  if (hideTimeTimeout) clearTimeout(hideTimeTimeout)
  hideTimeTimeout = setTimeout(() => {
    showTime.value = false
  }, 3000)
}

const handleLogout = () => {
  if (document.fullscreenElement) {
    document.exitFullscreen()
  }
  authStore.clearTokens()
  router.push('/login')
}

onMounted(() => {
  updateTime()
  timeInterval = setInterval(updateTime, 1000)
  document.addEventListener('mousemove', handleMouseMove)
  
  // Hide time after 3 seconds
  hideTimeTimeout = setTimeout(() => {
    showTime.value = false
  }, 3000)
})

onUnmounted(() => {
  if (timeInterval) clearInterval(timeInterval)
  if (hideTimeTimeout) clearTimeout(hideTimeTimeout)
  document.removeEventListener('mousemove', handleMouseMove)
})
</script>

<style scoped>
.kiosk-layout {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  background: #000;
  color: white;
  position: relative;
}

.kiosk-layout.fullscreen {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 9999;
}

.kiosk-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  background: rgba(255, 255, 255, 0.05);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.kiosk-header h1 {
  margin: 0;
  font-size: 1.5rem;
  font-weight: 600;
}

.kiosk-controls {
  display: flex;
  gap: 0.5rem;
}

.kiosk-content {
  flex: 1;
  overflow: hidden;
  padding: 2rem;
}

.kiosk-time {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  padding: 1rem 2rem;
  background: rgba(0, 0, 0, 0.7);
  backdrop-filter: blur(10px);
  border-radius: 8px;
  font-size: 1.25rem;
  font-weight: 500;
  opacity: 0;
  transition: opacity 0.3s ease;
  pointer-events: none;
}

.kiosk-time.show {
  opacity: 1;
}
</style>

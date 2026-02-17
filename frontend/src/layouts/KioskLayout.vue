<template>
  <div class="kiosk-layout" :class="{ 'app-dark': isDarkTheme }">
    <!-- Status Bar -->
    <div class="kiosk-status-bar">
      <div class="status-left">
        <div class="status-item">
          <i class="pi pi-user"></i>
          <span>{{ authStore.user?.full_name || 'User' }}</span>
        </div>
        <div class="status-item">
          <i :class="['pi', edgeStatus.icon]" :style="{ color: edgeStatus.color }"></i>
          <span>{{ edgeStatus.text }}</span>
        </div>
      </div>
      <div class="status-right">
        <div class="status-item time">
          {{ currentTime }}
        </div>
        <Button
          :icon="isFullscreen ? 'pi pi-window-minimize' : 'pi pi-window-maximize'"
          text
          rounded
          @click="toggleFullscreen"
          class="status-button"
        />
        <Button
          icon="pi pi-sign-out"
          text
          rounded
          severity="danger"
          @click="handleLogout"
          class="status-button"
        />
      </div>
    </div>

    <!-- Main Content -->
    <div class="kiosk-content">
      <router-view />
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'
import { useLayout } from '../composables/layout'
import Button from 'primevue/button'

const router = useRouter()
const authStore = useAuthStore()
const { isDarkTheme } = useLayout()

const isFullscreen = ref(false)
const currentTime = ref('')
const edgeConnected = ref(true) // Simulate Edge connection status

let timeInterval = null

const edgeStatus = computed(() => {
  if (edgeConnected.value) {
    return {
      icon: 'pi-check-circle',
      color: '#22c55e',
      text: 'Edge Connected'
    }
  }
  return {
    icon: 'pi-times-circle',
    color: '#ef4444',
    text: 'Edge Disconnected'
  }
})

const updateTime = () => {
  const now = new Date()
  currentTime.value = now.toLocaleString('vi-VN', {
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit',
    day: '2-digit',
    month: '2-digit',
    year: 'numeric'
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

const handleLogout = () => {
  if (document.fullscreenElement) {
    document.exitFullscreen()
  }
  authStore.clearTokens()
  router.push('/login')
}

// Simulate edge connection check
const checkEdgeConnection = () => {
  // In production, this would be an actual API call to Edge device
  // For now, simulate with random status
  if (Math.random() > 0.9) {
    edgeConnected.value = !edgeConnected.value
  }
}

onMounted(() => {
  updateTime()
  timeInterval = setInterval(() => {
    updateTime()
    checkEdgeConnection()
  }, 1000)
  
  // Auto enter fullscreen on mobile
  if (window.innerWidth <= 768) {
    setTimeout(() => {
      document.documentElement.requestFullscreen()
      isFullscreen.value = true
    }, 500)
  }
})

onUnmounted(() => {
  if (timeInterval) clearInterval(timeInterval)
})
</script>

<style scoped>
.kiosk-layout {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  background: var(--surface-ground);
  color: var(--text-color);
  overflow: hidden;
}

.kiosk-status-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  background: var(--surface-card);
  border-bottom: 2px solid var(--surface-border);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  min-height: 80px;
}

.status-left,
.status-right {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.status-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  font-size: 1.125rem;
  font-weight: 500;
}

.status-item i {
  font-size: 1.5rem;
}

.status-item.time {
  font-family: 'Courier New', monospace;
  font-weight: 600;
  color: var(--primary-color);
}

.status-button {
  font-size: 1.5rem;
}

.kiosk-content {
  flex: 1;
  overflow-y: auto;
  padding: 2rem;
}

/* Mobile responsive */
@media (max-width: 768px) {
  .kiosk-status-bar {
    padding: 0.75rem 1rem;
    min-height: 70px;
  }
  
  .status-left,
  .status-right {
    gap: 0.75rem;
  }
  
  .status-item {
    font-size: 0.875rem;
  }
  
  .status-item i {
    font-size: 1.125rem;
  }
  
  .kiosk-content {
    padding: 1rem;
  }
}

@media (max-width: 480px) {
  .status-item span {
    display: none;
  }
  
  .status-item.time span {
    display: inline;
  }
}
</style>

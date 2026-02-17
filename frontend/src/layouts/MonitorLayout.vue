<template>
  <div class="monitor-layout">
    <!-- Top Bar -->
    <div class="monitor-header">
      <div class="header-left">
        <i class="pi pi-chart-line text-3xl"></i>
        <div>
          <h1 class="m-0">Real-time Monitoring</h1>
          <p class="m-0 text-sm opacity-80">{{ currentTime }}</p>
        </div>
      </div>
      <div class="header-right">
        <Tag :value="`${authStore.user?.full_name}`" severity="success" icon="pi pi-user" />
        <Button
          icon="pi pi-sign-out"
          label="Logout"
          severity="danger"
          text
          @click="handleLogout"
        />
      </div>
    </div>

    <!-- Main Content -->
    <div class="monitor-content">
      <router-view />
    </div>

    <!-- Footer -->
    <div class="monitor-footer">
      <div class="footer-status">
        <Tag severity="success" icon="pi pi-check-circle" value="System Online" />
        <span class="mx-2">|</span>
        <span>Last updated: {{ lastUpdate }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'
import Button from 'primevue/button'
import Tag from 'primevue/tag'

const router = useRouter()
const authStore = useAuthStore()

const currentTime = ref('')
const lastUpdate = ref('')

const updateTime = () => {
  const now = new Date()
  currentTime.value = now.toLocaleTimeString('en-US', { 
    hour: '2-digit', 
    minute: '2-digit',
    second: '2-digit'
  })
  lastUpdate.value = now.toLocaleTimeString('en-US')
}

let timeInterval = null

onMounted(() => {
  updateTime()
  timeInterval = setInterval(updateTime, 1000)
})

onUnmounted(() => {
  if (timeInterval) clearInterval(timeInterval)
})

const handleLogout = () => {
  authStore.clearTokens()
  router.push('/login')
}
</script>

<style scoped>
.monitor-layout {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
  color: white;
}

.monitor-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem 2rem;
  background: rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(10px);
  border-bottom: 2px solid rgba(255, 255, 255, 0.1);
}

.header-left {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.header-left h1 {
  font-size: 1.75rem;
  font-weight: 700;
  letter-spacing: -0.02em;
}

.header-right {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.monitor-content {
  flex: 1;
  padding: 2rem;
  overflow-y: auto;
}

.monitor-footer {
  padding: 1rem 2rem;
  background: rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(10px);
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.footer-status {
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.875rem;
}

/* Scrollbar styling */
.monitor-content::-webkit-scrollbar {
  width: 8px;
}

.monitor-content::-webkit-scrollbar-track {
  background: rgba(255, 255, 255, 0.1);
}

.monitor-content::-webkit-scrollbar-thumb {
  background: rgba(255, 255, 255, 0.3);
  border-radius: 4px;
}

.monitor-content::-webkit-scrollbar-thumb:hover {
  background: rgba(255, 255, 255, 0.5);
}
</style>

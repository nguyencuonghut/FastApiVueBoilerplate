<template>
  <div class="dashboard-container">
    <div class="dashboard-header">
      <h1>Real-time Monitoring Dashboard</h1>
      <Button
        icon="pi pi-sign-out"
        label="Logout"
        class="p-button-rounded p-button-danger"
        @click="handleLogout"
      />
    </div>

    <div class="p-4">
      <Card>
        <template #title>
          <div class="flex align-items-center">
            <i class="pi pi-chart-bar mr-2"></i>
            System Monitoring
          </div>
        </template>
        <template #content>
          <div class="grid">
            <div class="col-12 md:col-6 lg:col-3">
              <Statistic
                label="Total Users"
                :value="stats.totalUsers"
                icon="pi-users"
              />
            </div>
            <div class="col-12 md:col-6 lg:col-3">
              <Statistic
                label="Active Sessions"
                :value="stats.activeSessions"
                icon="pi-window-maximize"
              />
            </div>
            <div class="col-12 md:col-6 lg:col-3">
              <Statistic
                label="Server Status"
                value="Online"
                icon="pi-server"
                severity="success"
              />
            </div>
            <div class="col-12 md:col-6 lg:col-3">
              <Statistic
                label="CPU Usage"
                value="45%"
                icon="pi-chart-pie"
              />
            </div>
          </div>

          <Divider />

          <div class="grid mt-4">
            <div class="col-12 md:col-6">
              <h3>Real-time Activity</h3>
              <DataTable :value="activityLog" :rows="5" striped-rows>
                <Column field="timestamp" header="Time" />
                <Column field="action" header="Action" />
                <Column field="user" header="User" />
              </DataTable>
            </div>
            <div class="col-12 md:col-6">
              <h3>System Alerts</h3>
              <div v-for="alert in alerts" :key="alert.id" class="mb-3">
                <Message
                  :severity="alert.severity"
                  :text="alert.message"
                  class="w-full"
                />
              </div>
            </div>
          </div>
        </template>
      </Card>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'
import Button from 'primevue/button'
import Card from 'primevue/card'
import DataTable from 'primevue/datatable'
import Column from 'primevue/column'
import Divider from 'primevue/divider'
import Message from 'primevue/message'
import Statistic from '../components/Statistic.vue'

const router = useRouter()
const authStore = useAuthStore()

const stats = ref({
  totalUsers: 1250,
  activeSessions: 48,
  serverStatus: 'online'
})

const activityLog = ref([
  { timestamp: '10:45 AM', action: 'Login', user: 'John Doe' },
  { timestamp: '10:30 AM', action: 'Data Export', user: 'Jane Smith' },
  { timestamp: '10:15 AM', action: 'Settings Update', user: 'Admin' }
])

const alerts = ref([
  { id: 1, severity: 'info', message: 'System backup completed successfully' },
  { id: 2, severity: 'warn', message: 'High memory usage detected' }
])

const handleLogout = () => {
  authStore.clearTokens()
  router.push('/login')
}

onMounted(() => {
  // Set up real-time updates
  const interval = setInterval(() => {
    stats.value.activeSessions = Math.floor(Math.random() * 100)
  }, 5000)

  return () => clearInterval(interval)
})
</script>

<style scoped>
.dashboard-container {
  min-height: 100vh;
  background: #f5f7fa;
}

.dashboard-header {
  background: white;
  padding: 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin-bottom: 20px;
}

.dashboard-header h1 {
  margin: 0;
  font-size: 24px;
  color: #333;
}
</style>

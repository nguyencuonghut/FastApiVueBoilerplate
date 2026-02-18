<template>
  <div class="monitor-dashboard">
    <!-- Stats Grid -->
    <div class="grid">
      <div v-for="stat in stats" :key="stat.id" class="col-12 md:col-6 lg:col-3">
        <div class="stat-card">
          <div class="stat-content">
            <div class="stat-icon" :style="{ background: stat.color }">
              <i :class="`pi ${stat.icon}`"></i>
            </div>
            <div class="stat-details">
              <span class="stat-label">{{ stat.label }}</span>
              <div class="stat-value">{{ stat.value }}</div>
              <div class="stat-trend" :class="stat.trend">
                <i :class="`pi ${stat.trend === 'up' ? 'pi-arrow-up' : 'pi-arrow-down'}`"></i>
                <span>{{ stat.change }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Main Content Grid -->
    <div class="grid">
      <!-- Real-time Activity Feed -->
      <div class="col-12 lg:col-6">
        <Card class="h-full">
          <template #title>
            <div class="flex align-items-center justify-content-between">
              <div class="flex align-items-center gap-2">
                <i class="pi pi-bolt"></i>
                <span>Real-time Activity</span>
              </div>
              <Tag severity="success" value="LIVE" icon="pi pi-circle-fill" />
            </div>
          </template>
          <template #content>
            <div class="activity-feed">
              <div
                v-for="activity in activities"
                :key="activity.id"
                class="activity-item"
              >
                <Avatar
                  :label="activity.user.charAt(0)"
                  size="large"
                  :style="{ background: activity.color, color: 'white' }"
                />
                <div class="activity-details">
                  <div class="activity-action">
                    <strong>{{ activity.user }}</strong> {{ activity.action }}
                  </div>
                  <div class="activity-time">{{ activity.time }}</div>
                </div>
                <Tag :severity="activity.severity" :value="activity.status" />
              </div>
            </div>
          </template>
        </Card>
      </div>

      <!-- System Health -->
      <div class="col-12 lg:col-6">
        <Card class="h-full">
          <template #title>
            <div class="flex align-items-center gap-2">
              <i class="pi pi-heart"></i>
              <span>System Health</span>
            </div>
          </template>
          <template #content>
            <div class="health-metrics">
              <div v-for="metric in healthMetrics" :key="metric.name" class="metric-item">
                <div class="metric-header">
                  <span class="metric-name">{{ metric.name }}</span>
                  <span class="metric-value">{{ metric.value }}%</span>
                </div>
                <ProgressBar
                  :value="metric.value"
                  :show-value="false"
                  :class="getHealthClass(metric.value)"
                />
              </div>
            </div>

            <Divider />

            <div class="server-status">
              <h4>Server Status</h4>
              <div class="status-grid">
                <div v-for="server in servers" :key="server.name" class="status-item">
                  <i
                    :class="`pi ${server.status === 'online' ? 'pi-check-circle' : 'pi-times-circle'}`"
                    :style="{ color: server.status === 'online' ? '#22c55e' : '#ef4444' }"
                  ></i>
                  <div>
                    <div class="server-name">{{ server.name }}</div>
                    <div class="server-location">{{ server.location }}</div>
                  </div>
                </div>
              </div>
            </div>
          </template>
        </Card>
      </div>
    </div>

    <!-- Data Table -->
    <Card>
      <template #title>
        <div class="flex justify-content-between align-items-center">
          <div class="flex align-items-center gap-2">
            <i class="pi pi-table"></i>
            <span>Recent Transactions</span>
          </div>
          <Button label="Export" icon="pi pi-download" outlined size="small" />
        </div>
      </template>
      <template #content>
        <DataTable
          :value="transactions"
          :rows="10"
          :paginator="true"
          striped-rows
          responsive-layout="scroll"
        >
          <Column field="id" header="ID" sortable />
          <Column field="user" header="User" sortable />
          <Column field="action" header="Action" />
          <Column field="timestamp" header="Timestamp" sortable />
          <Column field="status" header="Status">
            <template #body="{ data }">
              <Tag :severity="data.status === 'success' ? 'success' : 'danger'" :value="data.status" />
            </template>
          </Column>
        </DataTable>
      </template>
    </Card>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import Card from 'primevue/card'
import Tag from 'primevue/tag'
import Avatar from 'primevue/avatar'
import ProgressBar from 'primevue/progressbar'
import Divider from 'primevue/divider'
import DataTable from 'primevue/datatable'
import Column from 'primevue/column'
import Button from 'primevue/button'

const stats = ref([
  {
    id: 1,
    label: 'Total Users',
    value: '1,250',
    icon: 'pi-users',
    color: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
    trend: 'up',
    change: '+12%'
  },
  {
    id: 2,
    label: 'Active Sessions',
    value: '48',
    icon: 'pi-bolt',
    color: 'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)',
    trend: 'up',
    change: '+5%'
  },
  {
    id: 3,
    label: 'Revenue',
    value: '$25.4K',
    icon: 'pi-dollar',
    color: 'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)',
    trend: 'up',
    change: '+18%'
  },
  {
    id: 4,
    label: 'CPU Usage',
    value: '45%',
    icon: 'pi-chart-pie',
    color: 'linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)',
    trend: 'down',
    change: '-3%'
  }
])

const activities = ref([
  {
    id: 1,
    user: 'John Doe',
    action: 'logged in to the system',
    time: '2 seconds ago',
    color: '#667eea',
    severity: 'success',
    status: 'Success',
    isNew: true
  },
  {
    id: 2,
    user: 'Jane Smith',
    action: 'exported data report',
    time: '5 minutes ago',
    color: '#f093fb',
    severity: 'info',
    status: 'Completed'
  },
  {
    id: 3,
    user: 'Admin',
    action: 'updated system settings',
    time: '12 minutes ago',
    color: '#4facfe',
    severity: 'warn',
    status: 'Warning'
  },
  {
    id: 4,
    user: 'Mike Johnson',
    action: 'created new user account',
    time: '25 minutes ago',
    color: '#43e97b',
    severity: 'success',
    status: 'Success'
  }
])

const healthMetrics = ref([
  { name: 'CPU Usage', value: 45 },
  { name: 'Memory Usage', value: 62 },
  { name: 'Disk Space', value: 78 },
  { name: 'Network Load', value: 34 }
])

const servers = ref([
  { name: 'API Server', location: 'US East', status: 'online' },
  { name: 'Database', location: 'US West', status: 'online' },
  { name: 'Cache Server', location: 'EU Central', status: 'online' },
  { name: 'CDN', location: 'Asia Pacific', status: 'online' }
])

const transactions = ref([
  {
    id: 'TXN-001',
    user: 'John Doe',
    action: 'Login',
    timestamp: '2026-02-17 00:45:23',
    status: 'success'
  },
  {
    id: 'TXN-002',
    user: 'Jane Smith',
    action: 'Data Export',
    timestamp: '2026-02-17 00:40:15',
    status: 'success'
  },
  {
    id: 'TXN-003',
    user: 'Mike Johnson',
    action: 'Settings Update',
    timestamp: '2026-02-17 00:35:42',
    status: 'success'
  },
  {
    id: 'TXN-004',
    user: 'Sarah Williams',
    action: 'File Upload',
    timestamp: '2026-02-17 00:30:18',
    status: 'failed'
  },
  {
    id: 'TXN-005',
    user: 'Admin',
    action: 'System Backup',
    timestamp: '2026-02-17 00:25:50',
    status: 'success'
  }
])

const getHealthClass = (value) => {
  if (value < 50) return 'health-good'
  if (value < 75) return 'health-warning'
  return 'health-danger'
}

let activityInterval = null
let statsInterval = null

onMounted(() => {
  // Simulate real-time activity updates
  activityInterval = setInterval(() => {
    // Remove old "new" flags
    activities.value.forEach(a => a.isNew = false)
    
    // Add new activity
    const newActivity = {
      id: Date.now(),
      user: ['John Doe', 'Jane Smith', 'Mike Johnson', 'Sarah Williams'][Math.floor(Math.random() * 4)],
      action: ['logged in', 'exported data', 'updated settings', 'created report'][Math.floor(Math.random() * 4)],
      time: 'Just now',
      color: ['#667eea', '#f093fb', '#4facfe', '#43e97b'][Math.floor(Math.random() * 4)],
      severity: ['success', 'info', 'warn'][Math.floor(Math.random() * 3)],
      status: ['Success', 'Completed', 'Warning'][Math.floor(Math.random() * 3)],
      isNew: true
    }
    
    activities.value.unshift(newActivity)
    if (activities.value.length > 8) {
      activities.value.pop()
    }
  }, 8000)

  // Update stats periodically
  statsInterval = setInterval(() => {
    stats.value[1].value = Math.floor(Math.random() * 100).toString()
    stats.value[3].value = (30 + Math.random() * 40).toFixed(0) + '%'
    
    healthMetrics.value = healthMetrics.value.map(m => ({
      ...m,
      value: Math.min(100, Math.max(0, m.value + (Math.random() - 0.5) * 10))
    }))
  }, 5000)
})

onUnmounted(() => {
  if (activityInterval) clearInterval(activityInterval)
  if (statsInterval) clearInterval(statsInterval)
})
</script>

<style scoped>
.monitor-dashboard {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

/* Ensure equal height cards */
:deep(.h-full) {
  height: 100%;
}

:deep(.h-full .p-card) {
  height: 100%;
  display: flex;
  flex-direction: column;
}

:deep(.h-full .p-card-body) {
  flex: 1;
  display: flex;
  flex-direction: column;
}

:deep(.h-full .p-card-content) {
  flex: 1;
}

/* Stat Cards */
.stat-card {
  background: var(--surface-card);
  border-radius: var(--border-radius);
  padding: 1.5rem;
  border: 1px solid var(--surface-border);
  height: 100%;
}

.stat-content {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.stat-icon {
  width: 60px;
  height: 60px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.75rem;
  color: white;
  flex-shrink: 0;
}

.stat-details {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
  min-width: 0;
}

.stat-label {
  font-size: 0.875rem;
  color: var(--text-color-secondary);
  font-weight: 500;
}

.stat-value {
  font-size: 1.75rem;
  font-weight: 700;
  color: var(--text-color);
  line-height: 1;
}

.stat-trend {
  display: flex;
  align-items: center;
  gap: 0.25rem;
  font-size: 0.875rem;
  font-weight: 600;
  margin-top: 0.25rem;
}

.stat-trend.up {
  color: #22c55e;
}

.stat-trend.down {
  color: #ef4444;
}

/* Activity Feed */
.activity-feed {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  max-height: 450px;
  overflow-y: auto;
}

.activity-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  background: var(--surface-50);
  border-radius: var(--border-radius);
  transition: transform 0.2s;
}

.activity-item:hover {
  transform: translateX(4px);
  background: var(--surface-100);
}

.activity-details {
  flex: 1;
  min-width: 0;
}

.activity-action {
  margin: 0 0 0.25rem 0;
  color: var(--text-color);
  font-size: 0.9rem;
}

.activity-time {
  margin: 0;
  font-size: 0.8rem;
  color: var(--text-color-secondary);
}

/* Health Metrics */
.health-metrics {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  margin-bottom: 1.5rem;
}

.metric-item {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.metric-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.metric-name {
  font-weight: 600;
  color: var(--text-color);
  font-size: 0.9rem;
}

.metric-value {
  font-weight: 700;
  color: var(--text-color);
  font-size: 0.9rem;
}

:deep(.health-good .p-progressbar-value) {
  background: linear-gradient(90deg, #22c55e, #16a34a);
}

:deep(.health-warning .p-progressbar-value) {
  background: linear-gradient(90deg, #f59e0b, #d97706);
}

:deep(.health-danger .p-progressbar-value) {
  background: linear-gradient(90deg, #ef4444, #dc2626);
}

/* Server Status */
.server-status h4 {
  margin: 0 0 1rem 0;
  color: var(--text-color);
  font-size: 1rem;
  font-weight: 600;
}

.status-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
  gap: 0.75rem;
}

.status-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.75rem;
  background: var(--surface-50);
  border-radius: var(--border-radius);
}

.status-item i {
  font-size: 1.5rem;
  flex-shrink: 0;
}

.server-name {
  margin: 0 0 0.25rem 0;
  font-weight: 600;
  font-size: 0.875rem;
  color: var(--text-color);
}

.server-location {
  margin: 0;
  font-size: 0.75rem;
  color: var(--text-color-secondary);
}

/* Scrollbar */
.activity-feed::-webkit-scrollbar {
  width: 6px;
}

.activity-feed::-webkit-scrollbar-track {
  background: var(--surface-100);
  border-radius: 3px;
}

.activity-feed::-webkit-scrollbar-thumb {
  background: var(--surface-300);
  border-radius: 3px;
}

.activity-feed::-webkit-scrollbar-thumb:hover {
  background: var(--surface-400);
}
</style>

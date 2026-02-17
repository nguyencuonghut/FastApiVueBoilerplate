<template>
  <div>
    <Card>
      <template #title>
        <div class="flex align-items-center">
          <i class="pi pi-home mr-2"></i>
          Admin Dashboard
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
              label="Active Users"
              :value="stats.activeUsers"
              icon="pi-check-circle"
              severity="success"
            />
          </div>
          <div class="col-12 md:col-6 lg:col-3">
            <Statistic
              label="Total Roles"
              :value="stats.totalRoles"
              icon="pi-shield"
            />
          </div>
          <div class="col-12 md:col-6 lg:col-3">
            <Statistic
              label="System Status"
              value="Healthy"
              icon="pi-heart-fill"
              severity="success"
            />
          </div>
        </div>

        <Divider />

        <h3>Recent Activities</h3>
        <DataTable :value="recentActivities" striped-rows>
          <Column field="timestamp" header="Time" />
          <Column field="action" header="Action" />
          <Column field="user" header="User" />
          <Column field="status" header="Status">
            <template #body="{ data }">
              <Tag :value="data.status" :severity="getSeverity(data.status)" />
            </template>
          </Column>
        </DataTable>
      </template>
    </Card>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import Card from 'primevue/card'
import DataTable from 'primevue/datatable'
import Column from 'primevue/column'
import Divider from 'primevue/divider'
import Tag from 'primevue/tag'
import Statistic from '../../components/Statistic.vue'

const stats = ref({
  totalUsers: 1250,
  activeUsers: 980,
  totalRoles: 5
})

const recentActivities = ref([
  { timestamp: '10:45 AM', action: 'User Registration', user: 'John Doe', status: 'Success' },
  { timestamp: '10:30 AM', action: 'Role Assignment', user: 'Admin', status: 'Success' },
  { timestamp: '10:15 AM', action: 'Settings Update', user: 'Admin', status: 'Success' }
])

const getSeverity = (status) => {
  switch (status) {
    case 'Success':
      return 'success'
    case 'Failed':
      return 'danger'
    default:
      return 'info'
  }
}

onMounted(() => {
  // Load dashboard data
})
</script>

<style scoped>
</style>

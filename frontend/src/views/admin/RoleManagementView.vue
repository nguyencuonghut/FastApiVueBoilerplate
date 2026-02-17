<template>
  <div>
    <Card>
      <template #title>
        <div class="flex align-items-center">
          <i class="pi pi-shield mr-2"></i>
          Role Management
        </div>
      </template>
      <template #content>
        <DataTable
          :value="roles"
          striped-rows
          :loading="loading"
          expandable-rows
        >
          <Column expander style="width: 5rem" />
          <Column field="id" header="ID" style="width: 10%" />
          <Column field="name" header="Role Name" />
          <Column field="description" header="Description" />

          <template #expansion="slotProps">
            <div class="p-3">
              <h5>Permissions</h5>
              <div class="flex flex-wrap gap-2">
                <Tag
                  v-for="permission in slotProps.data.permissions"
                  :key="permission.id"
                  :value="permission.name"
                />
              </div>
            </div>
          </template>
        </DataTable>
      </template>
    </Card>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { adminService } from '../../services'
import Card from 'primevue/card'
import DataTable from 'primevue/datatable'
import Column from 'primevue/column'
import Tag from 'primevue/tag'
import { useToast } from 'primevue/usetoast'

const toast = useToast()

const roles = ref([])
const loading = ref(false)

const loadRoles = async () => {
  loading.value = true
  try {
    const response = await adminService.listRoles()
    roles.value = response.data
  } catch (error) {
    toast.add({
      severity: 'error',
      summary: 'Error',
      detail: 'Failed to load roles'
    })
  } finally {
    loading.value = false
  }
}

onMounted(loadRoles)
</script>

<style scoped>
</style>

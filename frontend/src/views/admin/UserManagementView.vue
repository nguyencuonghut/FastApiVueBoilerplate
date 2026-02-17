<template>
  <div>
    <Card>
      <template #title>
        <div class="flex align-items-center">
          <i class="pi pi-users mr-2"></i>
          User Management
        </div>
      </template>
      <template #content>
        <Toolbar class="mb-4">
          <template #start>
            <Button
              icon="pi pi-plus"
              label="Add User"
              severity="success"
              @click="openDialog"
            />
          </template>
          
          <template #end>
            <Button
              icon="pi pi-upload"
              label="Export"
              severity="secondary"
              @click="exportUsers"
            />
          </template>
        </Toolbar>
        
        <DataTable
          :value="users"
          striped-rows
          :loading="loading"
          lazy
          paginator
          :rows="rows"
          :totalRecords="totalRecords"
          :rowsPerPageOptions="[10, 25, 50]"
          @page="onPage"
          paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
          currentPageReportTemplate="Showing {first} to {last} of {totalRecords} users"
        >
          <template #header>
            <div class="flex align-items-center justify-content-end gap-2">
              <IconField class="w-full md:w-20rem">
                <InputIcon>
                  <i class="pi pi-search" />
                </InputIcon>
                <InputText
                  v-model="searchQuery"
                  placeholder="Search..."
                  class="w-full"
                  @input="onSearch"
                />
              </IconField>
            </div>
          </template>

          <Column field="id" header="ID" style="width: 10%" />
          <Column field="username" header="Username" />
          <Column field="email" header="Email" />
          <Column field="full_name" header="Full Name" />
          <Column field="role.name" header="Role" />
          <Column header="Actions" style="width: 15%">
            <template #body="{ data }">
              <Button
                icon="pi pi-trash"
                class="p-button-rounded p-button-danger p-button-sm"
                @click="deleteUser(data.id)"
              />
            </template>
          </Column>
        </DataTable>
      </template>
    </Card>

    <!-- User Dialog -->
    <Dialog v-model:visible="dialogVisible" header="Add User" modal>
      <form @submit.prevent="createUser">
        <div class="field grid">
          <label for="username" class="col-12 mb-2 font-bold"
            >Username</label
          >
          <InputText
            id="username"
            v-model="newUser.username"
            class="col-12"
            placeholder="Enter username"
          />
        </div>

        <div class="field grid">
          <label for="email" class="col-12 mb-2 font-bold">Email</label>
          <InputText
            id="email"
            v-model="newUser.email"
            type="email"
            class="col-12"
            placeholder="Enter email"
          />
        </div>

        <div class="field grid">
          <label for="password" class="col-12 mb-2 font-bold"
            >Password</label
          >
          <Password
            id="password"
            v-model="newUser.password"
            class="col-12"
            placeholder="Enter password"
            :feedback="false"
          />
        </div>

        <div class="field grid">
          <label for="full_name" class="col-12 mb-2 font-bold"
            >Full Name</label
          >
          <InputText
            id="full_name"
            v-model="newUser.full_name"
            class="col-12"
            placeholder="Enter full name"
          />
        </div>

        <div class="flex gap-2 justify-content-end">
          <Button
            label="Cancel"
            class="p-button-text"
            @click="dialogVisible = false"
          />
          <Button label="Save" @click="createUser" />
        </div>
      </form>
    </Dialog>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { adminService } from '../../services'
import Card from 'primevue/card'
import DataTable from 'primevue/datatable'
import Column from 'primevue/column'
import Button from 'primevue/button'
import Dialog from 'primevue/dialog'
import InputText from 'primevue/inputtext'
import IconField from 'primevue/iconfield'
import InputIcon from 'primevue/inputicon'
import Password from 'primevue/password'
import Toolbar from 'primevue/toolbar'
import { useToast } from 'primevue/usetoast'

const toast = useToast()

const users = ref([])
const loading = ref(false)
const dialogVisible = ref(false)
const searchQuery = ref('')
const totalRecords = ref(0)
const rows = ref(10)
const first = ref(0)
let searchTimeout = null

const newUser = ref({
  username: '',
  email: '',
  password: '',
  full_name: ''
})

const loadUsers = async () => {
  loading.value = true
  try {
    const skip = first.value
    const limit = rows.value
    const search = searchQuery.value.trim()
    
    const response = await adminService.listUsers(skip, limit, search)
    users.value = response.data.data
    totalRecords.value = response.data.total
  } catch (error) {
    toast.add({
      severity: 'error',
      summary: 'Error',
      detail: 'Failed to load users'
    })
  } finally {
    loading.value = false
  }
}

const onPage = (event) => {
  first.value = event.first
  rows.value = event.rows
  loadUsers()
}

const onSearch = () => {
  // Debounce search to avoid too many API calls
  clearTimeout(searchTimeout)
  searchTimeout = setTimeout(() => {
    first.value = 0 // Reset to first page on search
    loadUsers()
  }, 500)
}

const openDialog = () => {
  newUser.value = {
    username: '',
    email: '',
    password: '',
    full_name: ''
  }
  dialogVisible.value = true
}

const createUser = async () => {
  try {
    await adminService.createUser(newUser.value)
    dialogVisible.value = false
    loadUsers()
    toast.add({
      severity: 'success',
      summary: 'Success',
      detail: 'User created successfully'
    })
  } catch (error) {
    toast.add({
      severity: 'error',
      summary: 'Error',
      detail: error.response?.data?.detail || 'Failed to create user'
    })
  }
}

const deleteUser = async (userId) => {
  if (confirm('Are you sure you want to deactivate this user?')) {
    try {
      await adminService.deactivateUser(userId)
      loadUsers()
      toast.add({
        severity: 'success',
        summary: 'Success',
        detail: 'User deactivated successfully'
      })
    } catch (error) {
      toast.add({
        severity: 'error',
        summary: 'Error',
        detail: 'Failed to deactivate user'
      })
    }
  }
}

const exportUsers = () => {
  // Export users to CSV
  const headers = ['ID', 'Username', 'Email', 'Full Name', 'Role']
  const csvData = users.value.map(user => [
    user.id,
    user.username,
    user.email,
    user.full_name,
    user.role.name
  ])
  
  const csvContent = [
    headers.join(','),
    ...csvData.map(row => row.join(','))
  ].join('\n')
  
  const blob = new Blob([csvContent], { type: 'text/csv' })
  const url = window.URL.createObjectURL(blob)
  const link = document.createElement('a')
  link.href = url
  link.download = `users_${new Date().toISOString().split('T')[0]}.csv`
  link.click()
  window.URL.revokeObjectURL(url)
  
  toast.add({
    severity: 'success',
    summary: 'Success',
    detail: 'Users exported successfully'
  })
}

onMounted(loadUsers)
</script>

<style scoped>
</style>

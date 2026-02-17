<template>
  <div>
    <Card>
      <template #title>
        <div class="flex align-items-center">
          <i class="pi pi-users mr-2"></i>
          User Management
        </div>
      </template>
      <template #toolbar>
        <div class="p-toolbar-group-start mr-4">
          <Button
            icon="pi pi-plus"
            label="Add User"
            class="p-button-success"
            @click="openDialog"
          />
        </div>
      </template>
      <template #content>
        <DataTable
          :value="users"
          striped-rows
          :loading="loading"
          :paginator="true"
          :rows="10"
        >
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
import Password from 'primevue/password'
import { useToast } from 'primevue/usetoast'

const toast = useToast()

const users = ref([])
const loading = ref(false)
const dialogVisible = ref(false)
const newUser = ref({
  username: '',
  email: '',
  password: '',
  full_name: ''
})

const loadUsers = async () => {
  loading.value = true
  try {
    const response = await adminService.listUsers()
    users.value = response.data
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

onMounted(loadUsers)
</script>

<style scoped>
</style>

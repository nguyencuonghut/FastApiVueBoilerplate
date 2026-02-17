<template>
  <div class="profile-container p-4">
    <Card>
      <template #title>
        <div class="flex align-items-center">
          <i class="pi pi-user mr-2"></i>
          My Profile
        </div>
      </template>
      <template #content>
        <div class="grid">
          <div class="col-12 md:col-6">
            <form @submit.prevent="updateProfile">
              <div class="field">
                <label for="full_name">Full Name</label>
                <InputText
                  id="full_name"
                  v-model="profileForm.full_name"
                  class="w-full"
                />
              </div>

              <div class="field">
                <label for="email">Email</label>
                <InputText
                  id="email"
                  v-model="profileForm.email"
                  type="email"
                  class="w-full"
                  disabled
                />
              </div>

              <div class="field">
                <label for="username">Username</label>
                <InputText
                  id="username"
                  :value="currentUser.username"
                  class="w-full"
                  disabled
                />
              </div>

              <Button
                label="Update Profile"
                @click="updateProfile"
                class="mt-4"
              />
            </form>
          </div>

          <div class="col-12 md:col-6">
            <form @submit.prevent="changePassword">
              <h4>Change Password</h4>

              <div class="field">
                <label for="current_password">Current Password</label>
                <Password
                  id="current_password"
                  v-model="passwordForm.current_password"
                  class="w-full"
                  :feedback="false"
                />
              </div>

              <div class="field">
                <label for="new_password">New Password</label>
                <Password
                  id="new_password"
                  v-model="passwordForm.new_password"
                  class="w-full"
                  strength-only
                />
              </div>

              <Button
                label="Change Password"
                @click="changePassword"
                class="mt-4"
              />
            </form>
          </div>
        </div>
      </template>
    </Card>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useAuthStore } from '../stores/auth'
import { userService } from '../services'
import Card from 'primevue/card'
import Button from 'primevue/button'
import InputText from 'primevue/inputtext'
import Password from 'primevue/password'
import { useToast } from 'primevue/usetoast'

const toast = useToast()
const authStore = useAuthStore()

const currentUser = computed(() => authStore.user)

const profileForm = ref({
  full_name: '',
  email: ''
})

const passwordForm = ref({
  current_password: '',
  new_password: ''
})

const updateProfile = async () => {
  try {
    await userService.updateProfile({
      full_name: profileForm.value.full_name,
      email: profileForm.value.email
    })
    toast.add({
      severity: 'success',
      summary: 'Success',
      detail: 'Profile updated successfully'
    })
  } catch (error) {
    toast.add({
      severity: 'error',
      summary: 'Error',
      detail: error.response?.data?.detail || 'Failed to update profile'
    })
  }
}

const changePassword = async () => {
  if (!passwordForm.value.current_password || !passwordForm.value.new_password) {
    toast.add({
      severity: 'warn',
      summary: 'Warning',
      detail: 'Please fill all fields'
    })
    return
  }

  try {
    await userService.changePassword(
      passwordForm.value.current_password,
      passwordForm.value.new_password
    )
    passwordForm.value = {
      current_password: '',
      new_password: ''
    }
    toast.add({
      severity: 'success',
      summary: 'Success',
      detail: 'Password changed successfully'
    })
  } catch (error) {
    toast.add({
      severity: 'error',
      summary: 'Error',
      detail: error.response?.data?.detail || 'Failed to change password'
    })
  }
}

onMounted(() => {
  if (currentUser.value) {
    profileForm.value.full_name = currentUser.value.full_name || ''
    profileForm.value.email = currentUser.value.email || ''
  }
})
</script>

<style scoped>
.profile-container {
  max-width: 1200px;
  margin: 0 auto;
}
</style>

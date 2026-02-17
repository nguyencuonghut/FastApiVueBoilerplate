<template>
  <div class="login-container">
    <div class="login-card">
      <h1 class="login-title">FastAPI Vue Boilerplate</h1>
      <p class="login-subtitle">Sign in to your account</p>

      <form @submit.prevent="handleLogin">
        <div class="form-group">
          <label for="username">Username</label>
          <InputText
            id="username"
            v-model="username"
            placeholder="Enter username"
            class="w-full"
            :disabled="loading"
          />
        </div>

        <div class="form-group">
          <label for="password">Password</label>
          <Password
            id="password"
            v-model="password"
            placeholder="Enter password"
            :feedback="false"
            class="w-full"
            :disabled="loading"
          />
        </div>

        <Button
          type="submit"
          label="Sign In"
          class="w-full"
          :loading="loading"
          :disabled="loading || !username || !password"
        />
      </form>

      <Message
        v-if="error"
        severity="error"
        class="mt-4"
        :text="error"
        closable
        @close="error = null"
      />

      <!-- Demo credentials -->
      <div class="demo-credentials mt-4 p-3 surface-50 border-round">
        <p class="text-sm font-semibold mb-2">Demo Credentials:</p>
        <p class="text-xs">Admin: admin / admin123</p>
        <p class="text-xs">User: user / user123</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useAuthStore } from '../stores/auth'
import { authService } from '../services'
import InputText from 'primevue/inputtext'
import Password from 'primevue/password'
import Button from 'primevue/button'
import Message from 'primevue/message'

const router = useRouter()
const route = useRoute()
const authStore = useAuthStore()

const username = ref('')
const password = ref('')
const loading = ref(false)
const error = ref(null)

const handleLogin = async () => {
  loading.value = true
  error.value = null

  try {
    const response = await authService.login(username.value, password.value)
    authStore.storeTokens(response.data)

    // Redirect to dashboard or admin based on role
    const redirectPath = route.query.redirect || (authStore.isAdmin ? '/admin/dashboard' : '/dashboard')
    router.push(redirectPath)
  } catch (err) {
    error.value = err.response?.data?.detail || 'Login failed'
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.login-container {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.login-card {
  background: white;
  border-radius: 8px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
  padding: 40px;
  width: 100%;
  max-width: 400px;
}

.login-title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 8px;
  text-align: center;
  color: #333;
}

.login-subtitle {
  font-size: 14px;
  color: #999;
  text-align: center;
  margin-bottom: 24px;
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  font-size: 14px;
  font-weight: 500;
  margin-bottom: 8px;
  color: #333;
}

.demo-credentials {
  background-color: #f0f3ff;
  border: 1px solid #e0e7ff;
}
</style>

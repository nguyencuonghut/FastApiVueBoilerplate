<template>
  <div class="login-container">
    <button class="theme-toggle" @click="toggleDarkMode" type="button" title="Toggle Dark Mode">
      <i :class="['pi', { 'pi-moon': isDarkTheme, 'pi-sun': !isDarkTheme }]"></i>
    </button>
    <div class="login-card">
      <h1 class="login-title">FastAPI Vue Boilerplate</h1>
      <p class="login-subtitle">Sign in to your account</p>

      <form @submit.prevent="handleLogin">
        <div class="form-group">
          <label for="email">Email</label>
          <InputText
            id="email"
            v-model="email"
            type="email"
            placeholder="Enter your email"
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
            inputClass="w-full"
            :disabled="loading"
          />
        </div>

        <Button
          type="submit"
          label="Sign In"
          class="w-full"
          :loading="loading"
          :disabled="loading || !email || !password"
        />
      </form>

      <Message
        v-if="error"
        severity="error"
        class="mt-4"
        closable
        @close="error = null"
      >
        {{ error }}
      </Message>

      <!-- Demo credentials -->
      <div class="demo-credentials mt-4 p-3 surface-50 border-round">
        <p class="text-sm font-semibold mb-2">Demo Credentials:</p>
        <div class="credentials-grid">
          <div class="credential-item">
            <strong>SuperAdmin:</strong> superadmin@example.com / super123
          </div>
          <div class="credential-item">
            <strong>Admin:</strong> admin@example.com / admin123
          </div>
          <div class="credential-item">
            <strong>IT Staff:</strong> it@example.com / it123
          </div>
          <div class="credential-item">
            <strong>Bảo Trì:</strong> baotri@example.com / baotri123
          </div>
          <div class="credential-item">
            <strong>Bảo Vệ:</strong> baove@example.com / baove123
          </div>
          <div class="credential-item">
            <strong>Quản Lý:</strong> quanly@example.com / quanly123
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useAuthStore } from '../stores/auth'
import { useLayout } from '../composables/layout'
import { authService } from '../services'
import InputText from 'primevue/inputtext'
import Password from 'primevue/password'
import Button from 'primevue/button'
import Message from 'primevue/message'

const router = useRouter()
const route = useRoute()
const authStore = useAuthStore()
const { toggleDarkMode, isDarkTheme } = useLayout()

const email = ref('')
const password = ref('')
const loading = ref(false)
const error = ref(null)

const handleLogin = async () => {
  loading.value = true
  error.value = null

  try {
    const response = await authService.login(email.value, password.value)
    authStore.storeTokens(response.data)

    // Redirect based on role and query parameter
    const redirectPath = route.query.redirect || authStore.getDefaultRoute()
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
  position: relative;
}

.theme-toggle {
  position: absolute;
  top: 1.5rem;
  right: 1.5rem;
  width: 3rem;
  height: 3rem;
  border: none;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(10px);
  color: white;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.25rem;
  transition: all 0.3s;
  z-index: 10;
}

.theme-toggle:hover {
  background: rgba(255, 255, 255, 0.3);
  transform: scale(1.1);
}

.login-card {
  background: var(--surface-card);
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
  color: var(--text-color);
}

.login-subtitle {
  font-size: 14px;
  color: var(--text-color-secondary);
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
  color: var(--text-color);
}

.demo-credentials {
  background-color: var(--surface-50);
  border: 1px solid var(--surface-border);
}

.credentials-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 0.5rem;
}

.credential-item {
  font-size: 0.75rem;
  padding: 0.25rem 0;
}

.credential-item strong {
  color: var(--primary-color);
}
</style>

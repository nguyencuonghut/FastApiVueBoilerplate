<template>
  <div class="kiosk-workflow">
    <div class="workflow-header">
      <Button
        icon="pi pi-arrow-left"
        text
        rounded
        size="large"
        @click="goBack"
        class="back-button"
      />
      <h1><i class="pi pi-exclamation-triangle"></i> Báo Mất Thẻ</h1>
    </div>

    <div v-if="!reported" class="step-content">
      <h2>Thông Tin Báo Mất</h2>
      <div class="form-section">
        <div class="form-field">
          <label>Mã Thẻ *</label>
          <InputText
            v-model="formData.cardNumber"
            placeholder="Nhập mã thẻ bị mất"
            size="large"
            class="large-input"
          />
        </div>
        <div class="form-field">
          <label>CMND/CCCD *</label>
          <InputText
            v-model="formData.idNumber"
            placeholder="Nhập số CMND/CCCD"
            size="large"
            class="large-input"
          />
        </div>
        <div class="form-field">
          <label>Lý do mất thẻ</label>
          <Textarea
            v-model="formData.reason"
            placeholder="Mô tả lý do mất thẻ..."
            rows="5"
            class="large-input"
          />
        </div>
      </div>
      <div class="action-buttons">
        <Button
          label="Hủy"
          severity="secondary"
          size="large"
          @click="goBack"
          class="action-btn"
        />
        <Button
          label="Xác Nhận Báo Mất"
          icon="pi pi-check"
          size="large"
          @click="reportLost"
          :disabled="!canSubmit"
          class="action-btn"
        />
      </div>
    </div>

    <div v-else class="step-content success">
      <div class="success-icon">
        <i class="pi pi-check-circle"></i>
      </div>
      <h2>Đã Ghi Nhận Báo Mất!</h2>
      <p class="success-message">Mã Báo Mất: <strong>{{ reportId }}</strong></p>
      <p class="instruction">Vui lòng liên hệ bộ phận quản lý để được cấp thẻ mới</p>
      <div class="action-buttons">
        <Button
          label="Báo Mất Khác"
          icon="pi pi-refresh"
          size="large"
          @click="reset"
          class="action-btn"
        />
        <Button
          label="Về Trang Chủ"
          icon="pi pi-home"
          size="large"
          severity="secondary"
          @click="goBack"
          class="action-btn"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import InputText from 'primevue/inputtext'
import Textarea from 'primevue/textarea'
import Button from 'primevue/button'

const router = useRouter()

const reported = ref(false)
const reportId = ref('')
const formData = ref({
  cardNumber: '',
  idNumber: '',
  reason: ''
})

const canSubmit = computed(() => {
  return formData.value.cardNumber && formData.value.idNumber
})

const reportLost = () => {
  reportId.value = 'L' + Date.now().toString().slice(-8)
  reported.value = true
}

const reset = () => {
  reported.value = false
  reportId.value = ''
  formData.value = {
    cardNumber: '',
    idNumber: '',
    reason: ''
  }
}

const goBack = () => {
  router.push('/kiosk/dashboard')
}
</script>

<style scoped>
.kiosk-workflow {
  max-width: 1200px;
  margin: 0 auto;
}

.workflow-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 3rem;
}

.workflow-header h1 {
  font-size: 2.5rem;
  font-weight: 700;
  margin: 0;
  color: var(--text-color);
  display: flex;
  align-items: center;
  gap: 1rem;
}

.workflow-header i {
  color: #fa709a;
}

.back-button {
  font-size: 2rem;
}

.step-content {
  background: var(--surface-card);
  border-radius: 16px;
  padding: 3rem;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
}

.step-content h2 {
  font-size: 2rem;
  font-weight: 700;
  margin: 0 0 2rem 0;
  color: var(--text-color);
}

.form-section {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  margin-bottom: 2rem;
}

.form-field {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.form-field label {
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--text-color);
}

.large-input {
  font-size: 1.25rem !important;
  padding: 1rem !important;
  min-height: 60px;
}

.step-content.success {
  text-align: center;
}

.success-icon {
  margin-bottom: 2rem;
}

.success-icon i {
  font-size: 8rem;
  color: #22c55e;
}

.success-message {
  font-size: 1.5rem;
  color: var(--text-color);
  margin: 2rem 0;
}

.success-message strong {
  color: var(--primary-color);
  font-family: 'Courier New', monospace;
}

.instruction {
  font-size: 1.25rem;
  color: var(--text-color-secondary);
  margin: 1rem 0 2rem 0;
}

.action-buttons {
  display: flex;
  gap: 1.5rem;
  justify-content: center;
}

.action-btn {
  min-width: 200px;
  font-size: 1.25rem !important;
  padding: 1.25rem 2.5rem !important;
  border-radius: 12px !important;
}

@media (max-width: 768px) {
  .workflow-header h1 {
    font-size: 1.75rem;
  }
  
  .step-content {
    padding: 2rem;
  }
  
  .action-buttons {
    flex-direction: column;
  }
  
  .action-btn {
    width: 100%;
  }
}
</style>
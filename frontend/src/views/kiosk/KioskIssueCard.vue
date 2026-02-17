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
      <h1><i class="pi pi-plus-circle"></i> Cấp Phát Thẻ</h1>
    </div>

    <!-- Step Indicator -->
    <div class="steps-indicator">
      <div
        v-for="(step, index) in steps"
        :key="index"
        class="step-item"
        :class="{ active: currentStep === index + 1, completed: currentStep > index + 1 }"
      >
        <div class="step-circle">{{ index + 1 }}</div>
        <span>{{ step }}</span>
      </div>
    </div>

    <!-- Step 1: Nhập thông tin -->
    <div v-if="currentStep === 1" class="step-content">
      <h2>Bước 1: Nhập Thông Tin</h2>
      <div class="form-grid">
        <div class="form-field">
          <label>Họ và Tên *</label>
          <InputText
            v-model="formData.fullName"
            placeholder="Nhập họ tên"
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
          <label>Số Điện Thoại</label>
          <InputText
            v-model="formData.phone"
            placeholder="Nhập số điện thoại"
            size="large"
            class="large-input"
          />
        </div>
        <div class="form-field">
          <label>Lý Do</label>
          <Dropdown
            v-model="formData.reason"
            :options="reasons"
            optionLabel="label"
            optionValue="value"
            placeholder="Chọn lý do"
            size="large"
            class="large-input"
          />
        </div>
      </div>
    </div>

    <!-- Step 2: Xác nhận -->
    <div v-if="currentStep === 2" class="step-content">
      <h2>Bước 2: Xác Nhận Thông Tin</h2>
      <div class="confirmation-card">
        <div class="confirm-item">
          <span class="label">Họ và Tên:</span>
          <span class="value">{{ formData.fullName }}</span>
        </div>
        <div class="confirm-item">
          <span class="label">CMND/CCCD:</span>
          <span class="value">{{ formData.idNumber }}</span>
        </div>
        <div class="confirm-item">
          <span class="label">Số Điện Thoại:</span>
          <span class="value">{{ formData.phone || 'Không có' }}</span>
        </div>
        <div class="confirm-item">
          <span class="label">Lý Do:</span>
          <span class="value">{{ getReasonLabel(formData.reason) }}</span>
        </div>
      </div>
    </div>

    <!-- Step 3: Hoàn thành -->
    <div v-if="currentStep === 3" class="step-content success">
      <div class="success-icon">
        <i class="pi pi-check-circle"></i>
      </div>
      <h2>Cấp Thẻ Thành Công!</h2>
      <div class="card-info">
        <div class="card-number">
          <span class="label">Mã Thẻ:</span>
          <span class="number">{{ cardNumber }}</span>
        </div>
        <p class="instruction">Vui lòng lấy thẻ và giữ cẩn thận</p>
      </div>
    </div>

    <!-- Action Buttons -->
    <div class="action-buttons">
      <Button
        v-if="currentStep > 1 && currentStep < 3"
        label="Quay Lại"
        icon="pi pi-arrow-left"
        size="large"
        severity="secondary"
        @click="prevStep"
        class="action-btn"
      />
      <Button
        v-if="currentStep < 3"
        :label="currentStep === 2 ? 'Xác Nhận Cấp Thẻ' : 'Tiếp Tục'"
        :icon="currentStep === 2 ? 'pi pi-check' : 'pi pi-arrow-right'"
        iconPos="right"
        size="large"
        @click="nextStep"
        :disabled="!canProceed"
        class="action-btn"
      />
      <Button
        v-if="currentStep === 3"
        label="Cấp Thẻ Mới"
        icon="pi pi-plus"
        size="large"
        @click="reset"
        class="action-btn"
      />
      <Button
        v-if="currentStep === 3"
        label="Về Trang Chủ"
        icon="pi pi-home"
        size="large"
        severity="secondary"
        @click="goBack"
        class="action-btn"
      />
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import InputText from 'primevue/inputtext'
import Dropdown from 'primevue/dropdown'
import Button from 'primevue/button'

const router = useRouter()

const currentStep = ref(1)
const steps = ['Nhập Thông Tin', 'Xác Nhận', 'Hoàn Thành']

const formData = ref({
  fullName: '',
  idNumber: '',
  phone: '',
  reason: null
})

const reasons = [
  { label: 'Người thân', value: 'family' },
  { label: 'Công tác', value: 'work' },
  { label: 'Giao hàng', value: 'delivery' },
  { label: 'Khác', value: 'other' }
]

const cardNumber = ref('')

const canProceed = computed(() => {
  if (currentStep.value === 1) {
    return formData.value.fullName && formData.value.idNumber
  }
  return true
})

const getReasonLabel = (value) => {
  const reason = reasons.find(r => r.value === value)
  return reason ? reason.label : 'Không xác định'
}

const nextStep = () => {
  if (currentStep.value === 2) {
    // Simulate issuing card
    cardNumber.value = 'C' + Date.now().toString().slice(-8)
  }
  currentStep.value++
}

const prevStep = () => {
  currentStep.value--
}

const reset = () => {
  currentStep.value = 1
  formData.value = {
    fullName: '',
    idNumber: '',
    phone: '',
    reason: null
  }
  cardNumber.value = ''
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
  color: var(--primary-color);
}

.back-button {
  font-size: 2rem;
}

.steps-indicator {
  display: flex;
  justify-content: center;
  gap: 2rem;
  margin-bottom: 3rem;
}

.step-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  opacity: 0.5;
  transition: opacity 0.3s;
}

.step-item.active,
.step-item.completed {
  opacity: 1;
}

.step-circle {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background: var(--surface-border);
  color: var(--text-color-secondary);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  font-weight: 700;
  transition: all 0.3s;
}

.step-item.active .step-circle {
  background: var(--primary-color);
  color: white;
  transform: scale(1.1);
}

.step-item.completed .step-circle {
  background: #22c55e;
  color: white;
}

.step-item span {
  font-size: 1.125rem;
  font-weight: 500;
  color: var(--text-color);
}

.step-content {
  background: var(--surface-card);
  border-radius: 16px;
  padding: 3rem;
  margin-bottom: 2rem;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
}

.step-content h2 {
  font-size: 2rem;
  font-weight: 700;
  margin: 0 0 2rem 0;
  color: var(--text-color);
}

.form-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
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

.confirmation-card {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.confirm-item {
  display: flex;
  justify-content: space-between;
  padding: 1.5rem;
  background: var(--surface-50);
  border-radius: 12px;
  border-left: 4px solid var(--primary-color);
}

.confirm-item .label {
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--text-color-secondary);
}

.confirm-item .value {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--text-color);
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

.card-info {
  margin-top: 2rem;
}

.card-number {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  padding: 2rem;
  background: var(--surface-50);
  border-radius: 12px;
  margin-bottom: 1.5rem;
}

.card-number .label {
  font-size: 1.25rem;
  color: var(--text-color-secondary);
}

.card-number .number {
  font-size: 3rem;
  font-weight: 700;
  color: var(--primary-color);
  font-family: 'Courier New', monospace;
}

.instruction {
  font-size: 1.25rem;
  color: var(--text-color-secondary);
  margin: 0;
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

/* Mobile responsive */
@media (max-width: 768px) {
  .workflow-header h1 {
    font-size: 1.75rem;
  }
  
  .steps-indicator {
    gap: 1rem;
  }
  
  .step-circle {
    width: 48px;
    height: 48px;
    font-size: 1.25rem;
  }
  
  .step-item span {
    font-size: 0.875rem;
  }
  
  .step-content {
    padding: 2rem;
  }
  
  .form-grid {
    grid-template-columns: 1fr;
  }
  
  .action-buttons {
    flex-direction: column;
  }
  
  .action-btn {
    width: 100%;
  }
}
</style>

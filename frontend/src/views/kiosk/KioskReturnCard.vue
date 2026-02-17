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
      <h1><i class="pi pi-arrow-circle-left"></i> Thu Hồi Thẻ</h1>
    </div>

    <!-- Step 1: Scan/Enter Card -->
    <div v-if="!cardFound" class="step-content">
      <h2>Quét Hoặc Nhập Mã Thẻ</h2>
      <div class="scan-section">
        <div class="scan-icon">
          <i class="pi pi-qrcode"></i>
        </div>
        <p>Quét mã QR trên thẻ hoặc nhập mã thẻ</p>
        <InputText
          v-model="cardNumber"
          placeholder="Nhập mã thẻ (VD: C12345678)"
          size="large"
          class="large-input"
          @keyup.enter="searchCard"
        />
        <Button
          label="Tra Cứu"
          icon="pi pi-search"
          size="large"
          @click="searchCard"
          :disabled="!cardNumber"
          class="scan-button"
        />
      </div>
    </div>

    <!-- Step 2: Confirm Return -->
    <div v-else-if="!returned" class="step-content">
      <h2>Xác Nhận Thu Hồi</h2>
      <div class="card-details">
        <div class="detail-item">
          <span class="label">Mã Thẻ:</span>
          <span class="value">{{ cardInfo.number }}</span>
        </div>
        <div class="detail-item">
          <span class="label">Họ Tên:</span>
          <span class="value">{{ cardInfo.holderName }}</span>
        </div>
        <div class="detail-item">
          <span class="label">Ngày Cấp:</span>
          <span class="value">{{ cardInfo.issueDate }}</span>
        </div>
      </div>
      <div class="action-buttons">
        <Button
          label="Hủy"
          severity="secondary"
          size="large"
          @click="reset"
          class="action-btn"
        />
        <Button
          label="Xác Nhận Thu Hồi"
          icon="pi pi-check"
          size="large"
          @click="returnCard"
          class="action-btn"
        />
      </div>
    </div>

    <!-- Step 3: Success -->
    <div v-else class="step-content success">
      <div class="success-icon">
        <i class="pi pi-check-circle"></i>
      </div>
      <h2>Thu Hồi Thành Công!</h2>
      <p class="success-message">Thẻ {{ cardInfo.number }} đã được thu hồi</p>
      <div class="action-buttons">
        <Button
          label="Thu Hồi Thẻ Khác"
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
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import InputText from 'primevue/inputtext'
import Button from 'primevue/button'

const router = useRouter()

const cardNumber = ref('')
const cardFound = ref(false)
const returned = ref(false)
const cardInfo = ref({})

const searchCard = () => {
  // Simulate card search
  cardFound.value = true
  cardInfo.value = {
    number: cardNumber.value,
    holderName: 'Nguyễn Văn A',
    issueDate: new Date().toLocaleDateString('vi-VN')
  }
}

const returnCard = () => {
  returned.value = true
}

const reset = () => {
  cardNumber.value = ''
  cardFound.value = false
  returned.value = false
  cardInfo.value = {}
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

.scan-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2rem;
}

.scan-icon {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
  display: flex;
  align-items: center;
  justify-content: center;
}

.scan-icon i {
  font-size: 6rem;
  color: white;
}

.scan-section p {
  font-size: 1.5rem;
  color: var(--text-color-secondary);
  text-align: center;
  margin: 0;
}

.large-input {
  font-size: 1.5rem !important;
  padding: 1.25rem !important;
  min-height: 70px;
  width: 100%;
  max-width: 500px;
  text-align: center;
}

.scan-button {
  font-size: 1.5rem !important;
  padding: 1.25rem 3rem !important;
  border-radius: 12px !important;
}

.card-details {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.detail-item {
  display: flex;
  justify-content: space-between;
  padding: 1.5rem;
  background: var(--surface-50);
  border-radius: 12px;
  border-left: 4px solid var(--primary-color);
}

.detail-item .label {
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--text-color-secondary);
}

.detail-item .value {
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

.success-message {
  font-size: 1.5rem;
  color: var(--text-color-secondary);
  margin: 2rem 0;
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
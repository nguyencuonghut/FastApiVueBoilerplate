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
      <h1><i class="pi pi-search"></i> Tra Cứu Thẻ</h1>
    </div>

    <div class="step-content">
      <div class="search-section">
        <div class="search-icon">
          <i class="pi pi-search"></i>
        </div>
        <p>Nhập mã thẻ hoặc số CMND/CCCD để tra cứu</p>
        <InputText
          v-model="searchQuery"
          placeholder="Nhập thông tin tra cứu..."
          size="large"
          class="large-input"
          @keyup.enter="search"
        />
        <Button
          label="Tra Cứu"
          icon="pi pi-search"
          size="large"
          @click="search"
          :disabled="!searchQuery"
          class="search-button"
        />
      </div>

      <div v-if="searched && !found" class="not-found">
        <i class="pi pi-info-circle"></i>
        <p>Không tìm thấy thông tin</p>
      </div>

      <div v-if="found" class="result-section">
        <h2>Thông Tin Thẻ</h2>
        <div class="result-card">
          <div class="card-visual" :class="cardInfo.status">
            <div class="card-header">
              <span>THẺ RA VÀO</span>
              <span class="status-badge" :class="cardInfo.status">{{ getStatusLabel(cardInfo.status) }}</span>
            </div>
            <div class="card-number">{{ cardInfo.number }}</div>
            <div class="card-holder">{{ cardInfo.holderName }}</div>
          </div>
          <div class="card-details">
            <div class="detail-row">
              <span class="label"><i class="pi pi-id-card"></i> CMND/CCCD:</span>
              <span class="value">{{ cardInfo.idNumber }}</span>
            </div>
            <div class="detail-row">
              <span class="label"><i class="pi pi-phone"></i> Điện Thoại:</span>
              <span class="value">{{ cardInfo.phone }}</span>
            </div>
            <div class="detail-row">
              <span class="label"><i class="pi pi-calendar"></i> Ngày Cấp:</span>
              <span class="value">{{ cardInfo.issueDate }}</span>
            </div>
            <div class="detail-row">
              <span class="label"><i class="pi pi-info-circle"></i> Lý Do:</span>
              <span class="value">{{ cardInfo.reason }}</span>
            </div>
          </div>
        </div>
        <Button
          label="Tra Cứu Khác"
          icon="pi pi-refresh"
          size="large"
          @click="reset"
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

const searchQuery = ref('')
const searched = ref(false)
const found = ref(false)
const cardInfo = ref({})

const search = () => {
  searched.value = true
  // Simulate search
  found.value = true
  cardInfo.value = {
    number: 'C' + searchQuery.value,
    holderName: 'Nguyễn Văn A',
    idNumber: '0123456789',
    phone: '0901234567',
    issueDate: new Date().toLocaleDateString('vi-VN'),
    reason: 'Người thân',
    status: 'active'
  }
}

const reset = () => {
  searchQuery.value = ''
  searched.value = false
  found.value = false
  cardInfo.value = {}
}

const getStatusLabel = (status) => {
  const labels = {
    active: 'Đang Sử Dụng',
    returned: 'Đã Thu Hồi',
    lost: 'Báo Mất'
  }
  return labels[status] || status
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
  color: #43e97b;
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

.search-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2rem;
  margin-bottom: 3rem;
}

.search-icon {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
  display: flex;
  align-items: center;
  justify-content: center;
}

.search-icon i {
  font-size: 6rem;
  color: white;
}

.search-section p {
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
  max-width: 600px;
  text-align: center;
}

.search-button {
  font-size: 1.5rem !important;
  padding: 1.25rem 3rem !important;
  border-radius: 12px !important;
}

.not-found {
  text-align: center;
  padding: 3rem;
  color: var(--text-color-secondary);
}

.not-found i {
  font-size: 6rem;
  margin-bottom: 1rem;
}

.not-found p {
  font-size: 1.5rem;
  margin: 0;
}

.result-section {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.result-section h2 {
  font-size: 2rem;
  font-weight: 700;
  margin: 0;
  color: var(--text-color);
}

.result-card {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.card-visual {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 16px;
  padding: 2rem;
  color: white;
  min-height: 200px;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.card-visual.lost {
  background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
}

.card-visual.returned {
  background: linear-gradient(135deg, #6b7280 0%, #4b5563 100%);
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.875rem;
  font-weight: 600;
}

.status-badge {
  background: rgba(255, 255, 255, 0.2);
  padding: 0.5rem 1rem;
  border-radius: 20px;
  font-size: 0.875rem;
}

.card-number {
  font-size: 2rem;
  font-weight: 700;
  font-family: 'Courier New', monospace;
  margin-top: auto;
}

.card-holder {
  font-size: 1.5rem;
  font-weight: 600;
}

.card-details {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.detail-row {
  display: flex;
  justify-content: space-between;
  padding: 1.25rem;
  background: var(--surface-50);
  border-radius: 12px;
}

.detail-row .label {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  font-size: 1.125rem;
  font-weight: 600;
  color: var(--text-color-secondary);
}

.detail-row .value {
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--text-color);
}

.action-btn {
  align-self: center;
  min-width: 250px;
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
  
  .card-visual {
    padding: 1.5rem;
  }
  
  .card-number {
    font-size: 1.5rem;
  }
  
  .card-holder {
    font-size: 1.25rem;
  }
  
  .detail-row {
    flex-direction: column;
    gap: 0.5rem;
  }
}
</style>
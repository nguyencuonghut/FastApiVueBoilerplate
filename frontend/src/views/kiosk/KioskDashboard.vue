<template>
  <div class="kiosk-dashboard">
    <div class="kiosk-title">
      <i class="pi pi-id-card"></i>
      <h1>Hệ Thống Quản Lý Thẻ</h1>
    </div>

    <div class="workflow-grid">
      <div
        v-for="workflow in workflows"
        :key="workflow.id"
        class="workflow-card"
        :style="{ background: workflow.gradient }"
        @click="navigateTo(workflow.route)"
      >
        <div class="workflow-icon">
          <i :class="`pi ${workflow.icon}`"></i>
        </div>
        <div class="workflow-info">
          <h2>{{ workflow.title }}</h2>
          <p>{{ workflow.description }}</p>
        </div>
        <i class="pi pi-chevron-right workflow-arrow"></i>
      </div>
    </div>

    <div class="quick-stats">
      <div class="stat-card" v-for="stat in stats" :key="stat.label">
        <i :class="`pi ${stat.icon}`" :style="{ color: stat.color }"></i>
        <div class="stat-info">
          <span class="stat-value">{{ stat.value }}</span>
          <span class="stat-label">{{ stat.label }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const workflows = ref([
  {
    id: 1,
    title: 'Cấp Phát Thẻ',
    description: 'Đăng ký và cấp thẻ mới',
    icon: 'pi-plus-circle',
    route: '/kiosk/issue-card',
    gradient: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)'
  },
  {
    id: 2,
    title: 'Thu Hồi Thẻ',
    description: 'Thu hồi thẻ khi ra khỏi trại',
    icon: 'pi-arrow-circle-left',
    route: '/kiosk/return-card',
    gradient: 'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)'
  },
  {
    id: 3,
    title: 'Báo Mất Thẻ',
    description: 'Báo cáo thẻ bị mất hoặc hỏng',
    icon: 'pi-exclamation-triangle',
    route: '/kiosk/report-lost',
    gradient: 'linear-gradient(135deg, #fa709a 0%, #fee140 100%)'
  },
  {
    id: 4,
    title: 'Tra Cứu',
    description: 'Tra cứu thông tin thẻ',
    icon: 'pi-search',
    route: '/kiosk/search',
    gradient: 'linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)'
  }
])

const stats = ref([
  {
    icon: 'pi-id-card',
    value: '156',
    label: 'Thẻ Đang Dùng',
    color: '#667eea'
  },
  {
    icon: 'pi-check-circle',
    value: '12',
    label: 'Cấp Hôm Nay',
    color: '#22c55e'
  },
  {
    icon: 'pi-times-circle',
    value: '3',
    label: 'Báo Mất',
    color: '#ef4444'
  }
])

const navigateTo = (route) => {
  router.push(route)
}
</script>

<style scoped>
.kiosk-dashboard {
  max-width: 1400px;
  margin: 0 auto;
}

.kiosk-title {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 3rem;
  color: var(--text-color);
}

.kiosk-title i {
  font-size: 3rem;
  color: var(--primary-color);
}

.kiosk-title h1 {
  font-size: 2.5rem;
  font-weight: 700;
  margin: 0;
}

.workflow-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin-bottom: 3rem;
}

.workflow-card {
  background: var(--surface-card);
  border-radius: 16px;
  padding: 2.5rem;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  position: relative;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  min-height: 280px;
}

.workflow-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(255, 255, 255, 0.1);
  opacity: 0;
  transition: opacity 0.3s;
}

.workflow-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.2);
}

.workflow-card:hover::before {
  opacity: 1;
}

.workflow-card:active {
  transform: translateY(-4px) scale(0.98);
}

.workflow-icon {
  width: 80px;
  height: 80px;
  border-radius: 20px;
  background: rgba(255, 255, 255, 0.2);
  display: flex;
  align-items: center;
  justify-content: center;
  backdrop-filter: blur(10px);
}

.workflow-icon i {
  font-size: 3rem;
  color: white;
}

.workflow-info {
  flex: 1;
  color: white;
}

.workflow-info h2 {
  font-size: 1.75rem;
  font-weight: 700;
  margin: 0 0 0.5rem 0;
  color: white;
}

.workflow-info p {
  font-size: 1.125rem;
  margin: 0;
  opacity: 0.9;
  color: white;
}

.workflow-arrow {
  position: absolute;
  bottom: 2rem;
  right: 2rem;
  font-size: 2rem;
  color: white;
  opacity: 0.7;
  transition: all 0.3s;
}

.workflow-card:hover .workflow-arrow {
  opacity: 1;
  transform: translateX(4px);
}

.quick-stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
}

.stat-card {
  background: var(--surface-card);
  border-radius: 12px;
  padding: 2rem;
  display: flex;
  align-items: center;
  gap: 1.5rem;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
  transition: transform 0.2s;
}

.stat-card:hover {
  transform: translateY(-4px);
}

.stat-card i {
  font-size: 3rem;
}

.stat-info {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.stat-value {
  font-size: 2rem;
  font-weight: 700;
  color: var(--text-color);
}

.stat-label {
  font-size: 1rem;
  color: var(--text-color-secondary);
  font-weight: 500;
}

/* Mobile responsive */
@media (max-width: 768px) {
  .kiosk-title {
    margin-bottom: 2rem;
  }
  
  .kiosk-title i {
    font-size: 2rem;
  }
  
  .kiosk-title h1 {
    font-size: 1.75rem;
  }
  
  .workflow-grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
  
  .workflow-card {
    min-height: 200px;
    padding: 2rem;
  }
  
  .workflow-icon {
    width: 64px;
    height: 64px;
  }
  
  .workflow-icon i {
    font-size: 2.5rem;
  }
  
  .workflow-info h2 {
    font-size: 1.5rem;
  }
  
  .workflow-info p {
    font-size: 1rem;
  }
  
  .quick-stats {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 480px) {
  .workflow-card {
    min-height: 180px;
    padding: 1.5rem;
  }
  
  .workflow-icon {
    width: 56px;
    height: 56px;
  }
  
  .workflow-icon i {
    font-size: 2rem;
  }
  
  .stat-card {
    padding: 1.5rem;
  }
  
  .stat-card i {
    font-size: 2.5rem;
  }
  
  .stat-value {
    font-size: 1.75rem;
  }
}
</style>

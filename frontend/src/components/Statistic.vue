<template>
  <div class="statistic-card">
    <div class="statistic-icon" :style="{ color: getColorBySeverity() }">
      <i :class="`pi ${icon}`"></i>
    </div>
    <div class="statistic-content">
      <p class="statistic-label">{{ label }}</p>
      <p class="statistic-value">{{ value }}</p>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  label: {
    type: String,
    required: true
  },
  value: {
    type: [String, Number],
    required: true
  },
  icon: {
    type: String,
    default: 'pi-chart-bar'
  },
  severity: {
    type: String,
    default: 'info'
  }
})

const getColorBySeverity = () => {
  const colors = {
    success: '#22c55e',
    info: '#3b82f6',
    warning: '#f59e0b',
    danger: '#ef4444'
  }
  return colors[props.severity] || colors.info
}
</script>

<style scoped>
.statistic-card {
  background: var(--surface-card);
  border-radius: 8px;
  padding: 20px;
  display: flex;
  align-items: center;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s;
}

.statistic-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.statistic-icon {
  font-size: 32px;
  margin-right: 20px;
}

.statistic-content {
  flex: 1;
}

.statistic-label {
  margin: 0;
  font-size: 12px;
  color: var(--text-color-secondary);
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.statistic-value {
  margin: 4px 0 0 0;
  font-size: 28px;
  font-weight: bold;
  color: var(--text-color);
}
</style>

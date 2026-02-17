<template>
  <div class="layout-footer">
    <div class="footer-content">
      <span class="font-medium">FastAPI Vue Boilerplate</span>
      <span class="ml-2">v1.0.0</span>
    </div>
    <div class="footer-links">
      <a href="#" class="text-muted-color">Documentation</a>
      <a href="#" class="text-muted-color ml-4">Support</a>
      <a href="#" class="text-muted-color ml-4">License</a>
    </div>
  </div>
</template>

<script setup>
// Footer component - no additional logic needed
</script>

<style scoped>
.layout-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem 2rem;
  border-top: 1px solid var(--surface-border);
  background-color: var(--surface-card);
  margin-top: auto;
}

.footer-content {
  display: flex;
  align-items: center;
}

.footer-links a {
  text-decoration: none;
  transition: color 0.3s;
}

.footer-links a:hover {
  color: var(--primary-color);
}
</style>

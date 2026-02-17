<template>
  <li :class="{ 'layout-root-menuitem': root }">
    <div v-if="root && item.visible !== false" class="layout-menuitem-root-text">{{ item.label }}</div>
    <a 
      v-if="(!item.to || item.items) && item.visible !== false"
      :href="item.url" 
      @click="itemClick($event, item)" 
      :class="itemClass"
      :target="item.target"
      tabindex="0"
    >
      <i :class="item.icon" class="layout-menuitem-icon"></i>
      <span class="layout-menuitem-text">{{ item.label }}</span>
      <i v-if="item.items" class="pi pi-fw pi-angle-down layout-submenu-toggler"></i>
    </a>
    <router-link 
      v-if="item.to && !item.items && item.visible !== false" 
      @click="itemClick($event, item)"
      :class="itemClass" 
      tabindex="0" 
      :to="item.to"
      active-class="active-route"
      exact-active-class="active-route"
    >
      <i :class="item.icon" class="layout-menuitem-icon"></i>
      <span class="layout-menuitem-text">{{ item.label }}</span>
      <i v-if="item.items" class="pi pi-fw pi-angle-down layout-submenu-toggler"></i>
    </router-link>
    <Transition v-if="item.items && item.visible !== false" name="layout-submenu">
      <ul v-show="root ? true : isActive" class="layout-submenu">
        <app-menu-item 
          v-for="(child, i) in item.items" 
          :key="child"
          :index="i" 
          :item="child" 
          :parentPath="fullPath"
          :root="false"
        ></app-menu-item>
      </ul>
    </Transition>
  </li>
</template>

<script setup>
import { useLayout } from '@/composables/layout'
import { computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'

const { layoutState, isDesktop } = useLayout()
const router = useRouter()
const route = useRoute()

const props = defineProps({
  item: {
    type: Object,
    default: () => ({})
  },
  index: {
    type: Number,
    default: 0
  },
  root: {
    type: Boolean,
    default: true
  },
  parentPath: {
    type: String,
    default: null
  }
})

const fullPath = computed(() => {
  if (props.item.path) {
    return props.parentPath ? props.parentPath + props.item.path : props.item.path
  }
  return null
})

const isActive = computed(() => {
  // For parent items with path (group items)
  if (props.item.path) {
    // Check both layoutState and route for active state
    return layoutState.activePath?.startsWith(fullPath.value) ||
           route.path.startsWith(fullPath.value)
  }
  // For leaf items with 'to' route
  if (props.item.to) {
    return route.path === props.item.to || route.path.startsWith(props.item.to + '/')
  }
  return false
})

const itemClass = computed(() => {
  // For parent items (with subitems), we add active-route based on children
  if (props.item.items) {
    return ['layout-menuitem-link', {
      'active-route': isActive.value
    }]
  }
  // For leaf items (router-link), Vue Router will handle active-route via activeClass prop
  return 'layout-menuitem-link'
})

const itemClick = (event, item) => {
  if (item.disabled) {
    event.preventDefault()
    return
  }

  if (item.command) {
    item.command({ originalEvent: event, item: item })
  }

  if (item.items) {
    if (isActive.value) {
      layoutState.activePath = layoutState.activePath.replace(item.path, '')
    } else {
      layoutState.activePath = fullPath.value
    }
  } else {
    if (!isDesktop()) {
      layoutState.mobileMenuActive = false
    }
  }

  if (item.to) {
    router.push(item.to)
  }

  if (item.url) {
    window.location.href = item.url
  }
}
</script>

<style scoped>
/* Menu item styles handled by global SCSS */
</style>

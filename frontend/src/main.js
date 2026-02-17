import { createPinia } from 'pinia'
import { createApp } from 'vue'
import PrimeVue from 'primevue/config'
import { definePreset } from '@primevue/themes'
import Aura from '@primevue/themes/aura'
import Tooltip from 'primevue/tooltip'
import StyleClass from 'primevue/styleclass'
import ToastService from 'primevue/toastservice'
import App from './App.vue'
import router from './router'

import 'primeicons/primeicons.css'
import 'primeflex/primeflex.css'
import './assets/styles/layout.scss'

// Customize Aura preset with indigo as primary color
const MyPreset = definePreset(Aura, {
  semantic: {
    primary: {
      50: '{indigo.50}',
      100: '{indigo.100}',
      200: '{indigo.200}',
      300: '{indigo.300}',
      400: '{indigo.400}',
      500: '{indigo.500}',
      600: '{indigo.600}',
      700: '{indigo.700}',
      800: '{indigo.800}',
      900: '{indigo.900}',
      950: '{indigo.950}'
    }
  }
})

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(PrimeVue, {
  theme: {
    preset: MyPreset,
    options: {
      prefix: 'p',
      darkModeSelector: '.app-dark',
      cssLayer: false
    }
  }
})
app.use(ToastService)

// Register PrimeVue directives
app.directive('tooltip', Tooltip)
app.directive('styleclass', StyleClass)

app.mount('#app')

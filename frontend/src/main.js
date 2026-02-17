import { createPinia } from 'pinia'
import { createApp } from 'vue'
import PrimeVue from 'primevue/config'
import Aura from '@primevue/themes/aura'
import Tooltip from 'primevue/tooltip'
import StyleClass from 'primevue/styleclass'
import App from './App.vue'
import router from './router'

import 'primeicons/primeicons.css'
import './assets/styles/layout.scss?v=2'

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(PrimeVue, {
  theme: {
    preset: Aura,
    options: {
      darkModeSelector: '.app-dark'
    }
  }
})

// Register PrimeVue directives
app.directive('tooltip', Tooltip)
app.directive('styleclass', StyleClass)

app.mount('#app')

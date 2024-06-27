
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import {createPinia} from 'pinia'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'

import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

import Particles from "@tsparticles/vue3";
import { loadSlim } from "@tsparticles/slim"; 


const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)

createApp(App)
.use(router)
.use(pinia)
.use(ElementPlus)

.use(Particles, {
    init: async engine => {
        await loadSlim(engine);
    },
})

.mount('#app')

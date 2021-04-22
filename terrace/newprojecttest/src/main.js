import Vue from 'vue'
import './plugins/axios'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify';
import api from '../src/api/api'

Vue.config.productionTip = false
vue.prototype.$api = api

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')

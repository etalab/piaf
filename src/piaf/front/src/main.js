import Vue from 'vue'
import App from './App.vue'

import vuetify from './plugins/vuetify';
import store from './store'
import router from './router'

router.beforeEach((to, from, next) => {
  document.title = to.meta.title
  next()
})

Vue.config.productionTip = false

new Vue({
  vuetify,
  store,
  router,
  render: h => h(App)
}).$mount('#app')

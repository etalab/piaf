import Vue from 'vue'
import Router from 'vue-router'
import Theme from './views/Theme.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: '/app',
  routes: [
    {
      path: '',
      name: 'theme',
      component: Theme
    },
    {
      path: '/annotation',
      name: 'annotation',
      component: () => import('./views/Annotation.vue')
    },
    {
      path: '/bravo',
      name: 'bravo',
      component: () => import('./views/Bravo.vue')
    },
    // {
    //   path: '/*',
    //   component: () => import('./views/FourOhFour.vue')
    // },
  ]
})

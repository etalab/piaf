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
      meta: {title: 'Choix du thème'},
      component: Theme
    },
    {
      path: '/annotation',
      name: 'annotation',
      meta: {title: 'Question-réponse'},
      component: () => import('./views/Annotation.vue')
    },
    {
      path: '/introduction',
      name: 'introduction',
      meta: {title: 'Introduction'},
      component: () => import('./views/introduction/Introduction.vue')
    },
    {
      path: '/introduction-1',
      name: 'introduction-1',
      meta: {title: 'Introduction'},
      component: () => import('./views/introduction/Introduction-1.vue')
    },
    {
      path: '/introduction-2',
      name: 'introductio-2',
      meta: {title: 'Introduction'},
      component: () => import('./views/introduction/Introduction-2.vue')
    },
    {
      path: '/introduction-3',
      name: 'introduction-3',
      meta: {title: 'Introduction'},
      component: () => import('./views/introduction/Introduction-3.vue')
    },
    {
      path: '/test-1',
      name: 'test-1',
      meta: {title: 'test'},
      component: () => import('./views/introduction/Test-1.vue')
    },
    {
      path: '/test-2',
      name: 'test-2',
      meta: {title: 'test'},
      component: () => import('./views/introduction/Test-2.vue')
    },
    {
      path: '/test-3',
      name: 'test-3',
      meta: {title: 'test'},
      component: () => import('./views/introduction/Test-3.vue')
    },
    {
      path: '/bravo',
      name: 'bravo',
      meta: {title: 'Bravo'},
      component: () => import('./views/Bravo.vue')
    },
    {
      path: '/*',
      component: () => import('./views/FourOhFour.vue')
    },
  ]
})

import Vue from 'vue'
import Router from 'vue-router'
import Theme from './views/Theme.vue'
import store from './store'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: '/app',
  routes: [
    {
      path: '',
      name: 'level',
      meta: {title: 'Niveaux'},
      component: () => import('./views/Level.vue'),
      beforeEnter: async (to, from, next) => {
        await store.dispatch('getUserDetails')
        if (store.state && store.state.userDetails && store.state.userDetails.level_completed == 3) {
          next('/annotation/3/theme')
        }else {
          next()
        }
      },
    },
    {
      path: '/introduction/:level/',
      name: 'examples',
      meta: {title: 'Exemples'},
      component: () => import('./views/introduction/Examples.vue')
    },
    {
      path: '/introduction/:level/play',
      name: 'play',
      meta: {title: 'jouer'},
      component: () => import('./views/introduction/Play.vue')
    },
    {
      path: '/introduction/:level/bravo',
      name: 'level_finished',
      meta: {title: 'Niveau déverouillé'},
      component: () => import('./views/introduction/Bravo.vue')
    },
    {
      path: '/annotation/:level',
      name: 'annotation',
      meta: {title: 'à vous de jouer'},
      component: () => import('./views/annotation/Annotation.vue')
    },
    {
      path: '/annotation/:level/theme',
      name: 'annotation_theme',
      meta: {title: 'Choix du thème'},
      component: Theme
    },
    {
      path: '/annotation/:level/bravo',
      name: 'annotation_bravo',
      meta: {title: 'Bravo'},
      component: () => import('./views/annotation/Bravo.vue')
    },
    {
      path: '/*',
      component: () => import('./views/FourOhFour.vue')
    },
  ]
})

import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    // should the user see the screen "choose a theme"
    currentTheme: null,
    showTheme: true,
    showAnnotationTask: false,
  },
  mutations: {
    setShowTheme(state,boo) {
      state.showTheme = boo
    },
    setShowAnnotationTask(state,boo) {
      state.showAnnotationTask = boo
    },
    setCurrentTheme(state,newTheme) {
      state.currentTheme = newTheme
    },
  },
  actions: {

  }
})

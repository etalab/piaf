import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    // should the user see the screen "choose a theme"
    currentTheme: null,
    // show or not specific Vue components
    showTheme: true,
    showAnnotationTask: false,
    // Current paragraph we display
    currentDocument: {
      title: 'title article',
      text:'balbalblbalablalbblabalbalblbalablalbbla DD balbalblbalablalbbla'
    },
    // annotations from the user on the current paragraph
    annotations: null,
    currentQuestionIndex:0,
    maxAnnotationsPerDoc: 5,
    // interaction with the text for highliting answers
    startOffset: null,
    endOffset: null,
  },
  getters: {
    // here we have the number of completed annotation (It means proper question and its proper answer)
    finishedQuestionNumber: state => {
      return (state.annotations) ? state.annotations.filter(annotation =>
        annotation.question && annotation.answer).length : 0
    },
    currentAnnotation: state => {
      return (state.annotations) ? state.annotations[state.currentQuestionIndex] : null
    },
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
    setAnnotations(state,annotations){
      state.annotations = annotations
    },
    setStartOffset(state,num){
      state.startOffset = num
    },
    setEndOffset(state,num){
      state.endOffset = num
    },
  },
  actions: {
    switchFromThemeToAnnotationTask(context){
      context.commit('setShowAnnotationTask', true)
      context.commit('setShowTheme', false)
    }
  }
})

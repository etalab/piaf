import Vue from 'vue'
import Vuex from 'vuex'
import { getNewParagraph, sendQA } from './storeUtils.js'

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
      text:'this is a fake docuemnt, to be replaced by an API call. It means there is a problem loading the text. please contact us using this email: piaf@data.gouv.fr'
    },
    // annotations from the user on the current paragraph
    annotations: [
      {question:'',answer:{} },
      {question:'',answer:{} },
      {question:'',answer:{} },
      {question:'',answer:{} },
      {question:'',answer:{} }
    ], // [{"question": "q1", "answer": {"text": "a1", "index": 1}}]
    currentQuestionIndex:0,
    maxAnnotationsPerDoc: 5,
    // interaction with the text for highliting answers
    startOffset: null,
    endOffset: null,
    highlitedText: null,
    editMode:false,
  },
  getters: {
    // here we have the number of completed annotation (It means proper question and its proper answer)
    finishedQuestionNumber: state => {
      return state.annotations.filter(annotation =>
        annotation.question !== '' && annotation.answer.index !== undefined).length
    },
    currentAnnotation: state => {
      return state.annotations[state.currentQuestionIndex]
    },
    answersForTextInteraction: state => {
      return state.annotations
      .map(annotation => annotation.answer)
      .filter(answer => typeof answer.text === 'string')
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
    setHighlitedText(state,text){
      state.highlitedText = text
    },
    setEditeMode(state,boo){
      state.editMode = boo
    },
    setCurrentDocument(state, currentDocument){
      state.currentDocument = currentDocument
    }
  },
  actions: {
    switchFromThemeToAnnotationTask(context){
      context.commit('setShowAnnotationTask', true)
      context.commit('setShowTheme', false)
    },
    addNewHighlitedText({ commit, state }) {
      let newAnnotations = state.annotations
      newAnnotations[state.currentQuestionIndex].answer = {"text": state.highlitedText, "index": state.startOffset},
      commit('setAnnotations', newAnnotations)
      commit('setEndOffset', null)
      commit('setStartOffset', null)
      commit('setHighlitedText', null)

      // Bus.$emit('switch-editmode',false);

      // this.editedInput = null
      // if (this.isLastQuestion) {
        // this.$emit('submitToDatabase');
      // }
    },
    async loadNewText ({ commit }) {
      const newParagraph = await getNewParagraph()
      if(newParagraph){
        commit('setCurrentDocument', newParagraph)
        return true
      }else{
        console.log('problem loading the new paragraph');
        return false
      }
    },
    async saveQAs ({ commit }, data) {
      const res = await sendQA(data)
      if(res){
        return true
      }else{
        console.log('problem saving your Q&As');
        return false
      }
    },
  }
})

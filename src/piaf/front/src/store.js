import Vue from 'vue'
import Vuex from 'vuex'
import { getNewParagraph, sendQA, getUserDetails, getDatasetInfo, sendA, getNewQuestion } from './storeUtils.js'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    // should the user see the screen "choose a theme"
    currentTheme: null,
    // show or not specific Vue components
    showContinue: false,
    // Current paragraph we display
    currentDocument: false,
    // {
    //   title: 'Titre',
    //   text:'Ceci est un document par défaut. Il y a donc un problème de connexion, ou alors veuillez nous contacter à l\'adresse : piaf@data.gouv.fr',
    //   id:766,
    //   count_pending_batches:1,
    //   count_pending_paragraphs:1,
    //   count_completed_paragraphs:1,
    //   count_progress_batches:1,
    //   count_completed_batches:1,
    // },
    // annotations from the user on the current paragraph
    annotations: [
      {question:{}, answer:{} },
      {question:{}, answer:{} },
      {question:{}, answer:{} },
      {question:{}, answer:{} },
      {question:{}, answer:{} }
    ], // [{"question": {"text": "question 1"}, "answer": {"text": "a1", "index": 1}}]
    currentQuestionIndex:0,
    maxAnnotationsPerDoc: 5,
    // interaction with the text for highliting answers
    startOffset: null,
    endOffset: null,
    highlitedText: null,
    editMode:false,
    // what deals with the user
    userDetails: {},
    // {
    //     "id": 1,
    //     "username": "email@example.com",
    //     "email": "email@example.com",
    //     "is_certified": true,
    //     "level_completed": 3,
    //     "paragraphs_count": 14
    // }
    datasetInfo:{},
    themes: [
      {
        name: "Histoire",
        logo: "mdi-book-open-page-variant",
        color: "primary",
        empty: false,
      },
      {
        name: "Géographie",
        logo: "mdi-map-search",
        color: "warning",
        empty: false,
      },
      {
        name: "Société",
        logo: "mdi-city-variant",
        color: "error",
        empty: false,
      },
      {
        name: "Sport",
        logo: "mdi-basketball",
        color: "success",
        empty: false,
      },
      {
        name: "Religion",
        logo: "mdi-alpha-r",
        color: "secondary",
        empty: false,
      },
      {
        name: "Arts",
        logo: "mdi-palette",
        color: "info",
        empty: false,
      },
      {
        name: "Sciences",
        logo: "mdi-telescope",
        color: "accent",
        empty: false,
      },
      {
        name: "Mystère",
        logo: "mdi-help-circle",
        color: "black",
        empty: false,
      }
    ],
  },
  getters: {
    // here we have the number of completed annotation (It means proper question and its proper answer)
    numOfFinishedQA: state => {
      return state.annotations.filter(annotation =>
        typeof annotation.question.text === 'string' && typeof annotation.answer.text === 'string').length
    },
    numOfFinishedA: state => {
      return state.annotations.filter(annotation => typeof annotation.answer.text === 'string').length
    },
    currentAnnotation: state => {
      return state.annotations[state.currentQuestionIndex]
    },
    currentProgress: (state, getters) => {
      let index = state.currentQuestionIndex
      let hasAnswer = getters.hasAnswer
      let hasQuestion = getters.hasQuestion
      return index + 1 / 3 + hasAnswer / 3 + hasQuestion / 3
    },
    hasQuestion: (state, getters) => {
      return (typeof getters.currentAnnotation.question.text === 'string') ? true : false
    },
    hasAnswer: (state, getters) => {
      return (typeof getters.currentAnnotation.answer.text === 'string') ? true : false
    },
    answersForTextInteraction: state => {
      return state.annotations
      .map(annotation => (annotation.answer && typeof annotation.answer.text === 'string') ? annotation.answer : {})
    },
    currentDocumentChapitresInfo: state => {
      let total = (state.currentDocument && typeof state.currentDocument.count_completed_batches === 'number') ?  state.currentDocument.count_pending_batches + state.currentDocument.count_progress_batches + state.currentDocument.count_completed_batches : false
      let toDo = (state.currentDocument && typeof state.currentDocument.count_completed_batches === 'number') ?  state.currentDocument.count_pending_batches + state.currentDocument.count_progress_batches : false
      return {total:total,toDo:toDo}
    },
  },
  mutations: {
    setCurrentTheme(state,newTheme) {
      state.currentTheme = newTheme
    },
    setThemes(state,newThemes) {
      state.themes = newThemes
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
    },
    setDatasetInfo(state, datasetInfo){
      state.datasetInfo = datasetInfo
    },
    setCurrentQuestionIndex(state, num){
      state.currentQuestionIndex = num
    },
    setshowContinue(state, boo){
      state.showContinue = boo
    },
    setUserDetails(state, doc){
      state.userDetails = doc
    },
  },
  actions: {
    addNewHighlitedText({ commit, state }) {
      let newAnnotations = state.annotations
      newAnnotations[state.currentQuestionIndex].answer = {"text": state.highlitedText, "index": state.startOffset},
      commit('setAnnotations', newAnnotations)
    },
    restoreHighliting({ commit }) {
      commit('setEndOffset', null)
      commit('setStartOffset', null)
      commit('setHighlitedText', null)
    },
    syncAnswerWithHighliting({ state, commit }) {
      const answer = state.annotations[state.currentQuestionIndex].answer
      if(answer === {}) { return false }
      commit('setEndOffset', answer.index + answer.text.length)
      commit('setStartOffset', answer.index)
      commit('setHighlitedText', answer.text)
    },
    removeAnswer({ commit, state, dispatch }) {
      let newAnnotations = state.annotations
      newAnnotations[state.currentQuestionIndex].answer = {}
      commit('setAnnotations', newAnnotations)
      dispatch('restoreHighliting')
      commit('setshowContinue', false)
    },
    async loadNewText ({ commit, state }) {
      const p = await getNewParagraph(state.currentTheme)
      if(p){
        const doc = {
          title: p.title,
          id: p.id,
          theme: p.theme,
          text: p.text,
          count_pending_batches: p.count_pending_batches,
          count_pending_paragraphs: p.count_pending_paragraphs,
          count_completed_paragraphs:p.count_completed_paragraphs,
          count_progress_batches:p.count_progress_batches,
          count_completed_batches:p.count_completed_batches,
        }
        commit('setCurrentDocument', doc)
        return true
      }else{
        // eslint-disable-next-line
        console.log('problem loading the new paragraph');
        return false
      }
    },
    async loadNewQuestion ({ commit, state }) {
      const p = await getNewQuestion(state.currentTheme)
      if(p){
        console.log(p);
        const doc = {
          title: p.paragraph.title,
          id: p.paragraph.id,
          theme: p.paragraph.theme,
          text: p.paragraph.text,
          count_pending_batches: null,
          count_pending_paragraphs: null,
          count_completed_paragraphs:null,
          count_progress_batches:null,
          count_completed_batches:null,
        }
        commit('setCurrentDocument', doc)
        const anno = [
          {question:{text: p.text, id:p.id}, answer:{} },
          {question:{}, answer:{} },
          {question:{}, answer:{} },
          {question:{}, answer:{} },
          {question:{}, answer:{} }
        ]
        commit('setAnnotations', anno)
        return true
      }else{
        // eslint-disable-next-line
        console.log('problem loading the new question');
        return false
      }
    },
    async saveQAs ({ state, dispatch }) {
      let qas = {}
      qas.paragraph = state.currentDocument.id
      qas.data = state.annotations
      const res = await sendQA(qas)
      if(res){
        return true
      }else{
        // eslint-disable-next-line
        console.log('problem saving your Q&As');
        return false
      }
    },
    async saveA ({ state, dispatch }) {
      let a = {}
      let anno = false
      if (state.annotations
        && state.annotations[0]
        && state.annotations[0].question
        && state.annotations[0].question.id) {
        anno = state.annotations[0]
      }else{
        // eslint-disable-next-line
        console.log('problem saving your Answer - input');
        return false
      }
      a.id = anno.question.id
      a.index = anno.answer.index
      a.text = anno.answer.text
      const res = await sendA(a)
      if(res){
        return true
      }else{
        // eslint-disable-next-line
        console.log('problem saving your Answer');
        return false
      }
    },
    goToNextIndex({commit, state, getters, dispatch}){
      let i = state.currentQuestionIndex
      let f = getters.numOfFinishedQA
      if( (i + 1) <= f){
        if (i + 1 < 5) {
          commit('setCurrentQuestionIndex', i + 1)
          dispatch('restoreHighliting')
        }else{
          // eslint-disable-next-line
          console.log('we cannot go further than 5 QR');
        }
      }else{
        // eslint-disable-next-line
        console.log('we cannot increase the current question index');
      }
    },
    async getUserDetails ({ commit }) {
      const u = await getUserDetails()
      if(u){
        commit('setUserDetails', u)
        return true
      }else{
        return false
      }
    },
    resetDefaultStore ({ commit }) {
      commit('setCurrentQuestionIndex', 0)
      commit('setEndOffset',null)
      commit('setStartOffset',null)
      commit('setHighlitedText',null)
      commit('setEditeMode',false)
      commit('setshowContinue',false)
      const defaultAnnotations = [
        {question:{}, answer:{} },
        {question:{}, answer:{} },
        {question:{}, answer:{} },
        {question:{}, answer:{} },
        {question:{}, answer:{} }
      ]
      commit('setAnnotations',defaultAnnotations)
    },
    async loadDatasetInfo ({ commit, state }) {
      let newThemes = JSON.parse(JSON.stringify(state.themes))
      for (var i = 0; i < newThemes.length; i++) {
        let p = await getDatasetInfo(newThemes[i].name)
        if(p){
          newThemes[i].count_pending_articles = p.count_pending_articles
          newThemes[i].count_completed_articles = p.count_completed_articles
          if (p.count_pending_articles === 0) {
            newThemes[i].empty = true
          }
          // return true
        }else{
          // eslint-disable-next-line
          console.log('problem loading the new datasetInfo');
          // return false
        }
      }
      commit('setThemes', newThemes)
    },
  }
})

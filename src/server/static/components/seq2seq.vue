<template lang="pug">
extends ./annotation_custom.pug

block annotation-area
  messageInfo(
    v-bind:messageInfo="messageInfo"
    v-on:remove-label="removeLabel"
  )

  div
    p.textaligncenter Le texte que vous allez lire est extrait d'un article Wikipédia dont le titre est : {{ articleTitle }}
  div.card.has-background-white.maxWidth1100.marginAuto
    div.card-content
      div.content(v-if="docs[pageNumber] && !annotations[pageNumber]")
        span.text(
          oncopy="return false"
          oncut="return false"
        ) {{ docs[pageNumber].text }}
      div.content(v-if="docs[pageNumber] && annotations[pageNumber]")
        annotator(
          v-bind:entity-positions="currentAnswerForAnnotator"
          v-bind:text="docs[pageNumber].text"
          v-bind:pageNumber="pageNumber"
          v-bind:currentQuestionIndex="currentQuestionIndex"
          ref="annotator"
        )

  navigationButtons(
    v-bind:currentQuestionIndex="currentQuestionIndex"
    v-bind:currentNumberOfQuestion="currentNumberOfQuestion"
    v-bind:currentNumberOfAnswer="currentNumberOfAnswer"
    v-on:setCurrentQuestionIndex="setCurrentQuestionIndex"
    v-on:reduceCurrentQuestionIndex="reduceCurrentQuestionIndex"
    v-on:increaseCurrentQuestionIndex="increaseCurrentQuestionIndex"
    v-bind:questionClass="questionClass"
  )

  div.maxWidth1100.marginAuto
    genericInput(
      ref="questionInputComponent"
      v-on:increaseCurrentQuestionIndex="`do something after update question?`"
      v-bind:buttonMessage1="`Modifier`"
      v-bind:buttonMessage2="`OK`"
      v-on:updateJSONs="updateQuestions"
      v-bind:JSONs="annotations"
      v-bind:pageNumber="pageNumber"
      v-bind:currentQuestionIndex="currentQuestionIndex"
      v-bind:currentJSON="currentQuestion"
      v-bind:placeholder="`Écrire une question`"
    )

    qandaButton(
      v-if="currentQuestion"
      ref="quandaButtonComponent"
      v-on:increaseCurrentQuestionIndex="increaseCurrentQuestionIndex"
      v-bind:buttonMessage1="`Modifier la réponse`"
      v-bind:buttonMessage2="`Valider`"
      v-bind:buttonMessage3="`Valider + envoyer`"
      v-on:updateJSONs="updateAnswers"
      v-on:submitToDatabase="submitToDatabase"
      v-bind:JSONs="answers"
      v-bind:pageNumber="pageNumber"
      v-bind:currentQuestionIndex="currentQuestionIndex"
      v-bind:questionIndexMax="questionIndexMax"
      v-bind:currentJSON="currentAnswer"
      v-bind:placeholder="`Surligner la réponse dans le texte :`"
    )
</template>

<script>
import annotationMixin from './annotationMixin';
import todoFocus from './directives';
import HTTP from './http';
import MessageInfo from './messageInfo.vue';
import NavigationButtons from './navigationButtons.vue';
import GenericInput from './genericInput.vue';
import QandaButton from './qandaButton.vue';
import Annotator from './annotator_qanda_fullmode.vue';

import Bus from './bus.js'

export default {
  directives: { todoFocus },

  mixins: [annotationMixin],

  components: { MessageInfo, NavigationButtons, GenericInput, QandaButton, Annotator},

  data: () => ({
    newTodo: '',
    editedTodo: null,
    currentQuestionIndex: 0,
    questionIndexMax: 4,
    //- newAnswer: '',
    editedAnswer: null,
    answers: [[]],
    messageInfo: '',
    articleTitle: '"Agriculture péri-urbaine"',
  }),

  computed: {
    currentNumberOfQuestion() {
      return (this.annotations[this.pageNumber]) ? this.annotations[this.pageNumber].length : 0
    },
    currentQuestion(){
      return (this.annotations[this.pageNumber])? this.annotations[this.pageNumber][this.currentQuestionIndex] : null
    },
    currentNumberOfAnswer() {
      return (this.answers[this.pageNumber]) ? this.answers[this.pageNumber].length : 0
    },
    currentAnswer(){
      return this.answers[this.pageNumber][this.currentQuestionIndex]
    },
    currentAnswerForAnnotator(){
      return (this.currentAnswer) ? [this.currentAnswer] : []
    },
  },

  methods: {
    updateQuestions(questions){
      this.annotations = questions
    },

    submitToDatabase() {
      const p = this.pageNumber
      const docId = this.docs[p].id;

      // let's check that every question is different
      if (Array.isArray( this.annotations[p]) ) {
        let annotations = this.annotations[p].map(annotation => annotation.text);
        let annotationsNoDuplicates = new Set(annotations)
        if (annotationsNoDuplicates.size !== annotations.length) {
          console.log('err in the question array 1'); this.messageInfo = 'Every questions must be different'; return false
        }
      }else{
        console.log('err in the question array 2'); this.messageInfo = 'problem with questions'; return false
      }

      this.annotations[p].forEach((annotation,i) => {
        // here we check before sending the first request that Q and A are conform to expected (this is frontend verification, used for sending error messages. We check on the backend as well)
        if ( !(typeof annotation === 'object' && annotation.text) ) {
          console.log('error in the question'); this.messageInfo = 'problem while checking the questions'; return false
        }
        let responseObj = (this.answers && this.answers[p] && this.answers[p][i]) ? JSON.parse(JSON.stringify(this.answers[p][i])) : null
        if ( !(responseObj && typeof responseObj.start_offset === 'number' && typeof responseObj.response === 'string') ) {
          console.log('error in the answer'); this.messageInfo = 'problem while checking the answers'; return false
        }
        // console.log(this.answers[p][i],'responseObj',responseObj );

        // we send the QA to the database
        HTTP.post(`docs/${docId}/annotations`, annotation).then((res,err) => {
          console.log('res,err',res,err);
          if (res.data && typeof res.data.id === 'number') {
              HTTP.post(`seq2seq_annotations/${res.data.id}/response`, responseObj).then((result,error) => {
                if(error){
                  console.log('RESPONSE PROBLEM',error);
                  this.messageInfo = 'problem while saving the question'
                }else{
                  console.log('RESPONSE ADDED',result);
                }
              });
          } else {
            console.log('problem while saving the question. It did not work:', res);
            this.messageInfo = 'problem while saving the question'
            return false
          }
        });

      })
      this.reinitialise()
      console.log('chargement du texte suivant à implementer: this.submit();');
      // chargement du texte suivant
      this.submit();

    },

    async submit() {
      const state = this.getState();
      this.url = `docs?q=${this.searchQuery}&is_checked=${state}&offset=${this.offset}&seq2seq_annotations__isnull=true`;
      await this.search();
      this.pageNumber = 0;
    },

    questionClass(i){
      let qNum = parseInt(this.currentNumberOfQuestion)
      let qCur = parseInt(this.currentQuestionIndex)
      return (i == qCur) ? 'activeButton'
                         : (i >= qNum && i > qCur) ? 'notYetButton'
                                                  : 'doneButton'
    },

    setCurrentQuestionIndex(i){
      Bus.$emit('switch-editmode',false);
      // in case we go to a new question, the _answerInputComponent_ is not yet defined unitl we press enter
      if(this.$refs.answerInputComponent){this.$refs.answerInputComponent.reInitialiseInputs()}
      if (this.questionClass(i) !== 'notYetButton') {
        this.currentQuestionIndex=i
      }else if(this.currentNumberOfQuestion === i && this.answers[this.pageNumber].length === this.currentNumberOfQuestion){
        this.currentQuestionIndex=i
      }
    },

    reduceCurrentQuestionIndex(){
      Bus.$emit('switch-editmode',false);
      if(this.$refs.answerInputComponent){this.$refs.answerInputComponent.reInitialiseInputs()}
      if(this.currentQuestionIndex>0){
        this.currentQuestionIndex--
      }
    },

    increaseCurrentQuestionIndex(){
      Bus.$emit('switch-editmode',false);
      if(this.$refs.answerInputComponent){this.$refs.answerInputComponent.reInitialiseInputs()}
      if(this.currentQuestionIndex<4){
        this.currentQuestionIndex++
      }else{
        console.log('trouver une autrea ction apres avoir soumis la dernier repose');
        // this.pageNumber++
      }
    },

    updateAnswers(answers) {
      this.answers = answers
    },

    reinitialise(){
      this.answers = [[]]
      this.annotations[this.pageNumber] = []
      this.currentQuestionIndex = 0
      this.editedAnswer= null
      this.messageInfo = ''
    },

  },

  mounted() {
    const thisBis = this
    // gestion des évènement liés au keyboard
    window.addEventListener('keyup', function(event) {
      // arrow left
      // if (event.keyCode == 37) {
      //   thisBis.reduceCurrentQuestionIndex()
      // arrow right
      // } else if (event.keyCode == 39) {
      //   thisBis.setCurrentQuestionIndex(thisBis.currentQuestionIndex+1)
      // escape
      // } else if (event.keyCode == 27) {
      if(event.keyCode == 27) {
        Bus.$emit('switch-editmode',false);
        if(thisBis.$refs.answerInputComponent){
          thisBis.$refs.answerInputComponent.cancelEditJSON()
        }
        if(thisBis.$refs.questionInputComponent) {
          thisBis.$refs.questionInputComponent.cancelEditJSON()
        }
      }
    });
  },


};
</script>

<style scoped>
  .todoapp{
    border-radius: 4em;
  }
  .maxWidth1100{
    max-width: 700px
  }
  .marginAuto{
    margin: auto;
  }
</style>

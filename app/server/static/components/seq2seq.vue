<template lang="pug">
extends ./annotation_custom.pug

block annotation-area
  messageInfo(
    v-bind:messageInfo="messageInfo"
    v-on:remove-label="removeLabel"
  )

  navigationButtons(
    v-bind:currentQuestionIndex="currentQuestionIndex"
    v-on:setCurrentQuestionIndex="setCurrentQuestionIndex"
    v-on:reduceCurrentQuestionIndex="reduceCurrentQuestionIndex"
    v-bind:questionClass="questionClass"
  )

  div.card.has-background-white
    div.card-content
      div.content(v-if="docs[pageNumber]")
        span.text {{ docs[pageNumber].text }}

  genericInput(
    ref="questionInputComponent"
    v-on:increaseCurrentQuestionIndex="`do something after update question?`"
    v-bind:buttonMessage1="`Edit`"
    v-bind:buttonMessage2="`OK`"
    v-on:updateJSONs="updateQuestions"
    v-bind:JSONs="annotations"
    v-bind:pageNumber="pageNumber"
    v-bind:currentQuestionIndex="currentQuestionIndex"
    v-bind:currentJSON="currentQuestion"
    v-bind:placeholder="`Écrire une question`"
  )


  genericInput(
    v-if="currentQuestion"
    ref="answerInputComponent"
    v-on:increaseCurrentQuestionIndex="increaseCurrentQuestionIndex"
    v-bind:buttonMessage1="`Edit`"
    v-bind:buttonMessage2="`OK`"
    v-on:updateJSONs="updateAnswers"
    v-bind:JSONs="answers"
    v-bind:pageNumber="pageNumber"
    v-bind:currentQuestionIndex="currentQuestionIndex"
    v-bind:currentJSON="currentAnswer"
    v-bind:placeholder="`Écrire une réponse`"
  )
</template>

<script>
import annotationMixin from './annotationMixin';
import todoFocus from './directives';
import HTTP from './http';
import MessageInfo from './messageInfo.vue';
import NavigationButtons from './navigationButtons.vue';
import GenericInput from './genericInput.vue';

export default {
  directives: { todoFocus },

  mixins: [annotationMixin],

  components: { MessageInfo, NavigationButtons, GenericInput},

  data: () => ({
    newTodo: '',
    editedTodo: null,
    currentQuestionIndex: 0,
    //- newAnswer: '',
    editedAnswer: null,
    answers: [[]],
    messageInfo: 'teston',
  }),

  computed: {
    currentNumberOfQuestion() {
      return (this.annotations[this.pageNumber]) ? this.annotations[this.pageNumber].length : 0
    },
    currentQuestion(){
      return (this.annotations[this.pageNumber])? this.annotations[this.pageNumber][this.currentQuestionIndex] : null
    },
    currentAnswer(){
      return this.answers[this.pageNumber][this.currentQuestionIndex]
    },
  },

  methods: {
    updateQuestions(questions){
      this.annotations = questions
    },

    submitToDatabase() {
      const docId = this.docs[this.pageNumber].id;
      this.annotations[this.pageNumber].forEach((annotation) => {
        console.log('annotation:',JSON.parse(JSON.stringify(annotation)));
        console.log(typeof annotation);
        if (typeof annotation === 'object' && annotation.text) {
          HTTP.post(`docs/${docId}/annotations`, annotation).then((response) => {
            // this.annotations[this.pageNumber].push(response.data);
            console.log('RESPONSE ADDED',response.data);
          });
        }
      })
      console.log('FORCER A LA PAGE SUIVANTE');
    },

    // async submit() {
    //   const state = this.getState();
    //   this.url = `docs?q=${this.searchQuery}&seq2seq_annotations__isnull=${state}&offset=${this.offset}`;
    //   await this.search();
    //   this.pageNumber = 0;
    // },

    questionClass(i){
      let qNum = parseInt(this.currentNumberOfQuestion)
      let qCur = parseInt(this.currentQuestionIndex)
      return (i == qCur) ? 'activeButton'
                         : (i >= qNum && i > qCur) ? 'notYetButton'
                                                  : 'doneButton'
    },

    setCurrentQuestionIndex(i){
      // in case we go to a new question, the _answerInputComponent_ is not yet defined unitl we press enter
      if(this.$refs.answerInputComponent){this.$refs.answerInputComponent.reInitialiseInputs()}
      if (this.questionClass(i) !== 'notYetButton') {
        this.currentQuestionIndex=i
      }else if(this.currentNumberOfQuestion === i && this.answers[this.pageNumber].length === this.currentNumberOfQuestion){
        this.currentQuestionIndex=i
      }
    },

    reduceCurrentQuestionIndex(){
      if(this.$refs.answerInputComponent){this.$refs.answerInputComponent.reInitialiseInputs()}
      if(this.currentQuestionIndex>0){
        this.currentQuestionIndex--
      }
    },

    increaseCurrentQuestionIndex(){
      if(this.$refs.answerInputComponent){this.$refs.answerInputComponent.reInitialiseInputs()}
      if(this.currentQuestionIndex<4){
        this.currentQuestionIndex++
      }else{
        this.pageNumber++
      }
    },

    updateAnswers(answers) {
      this.answers = answers
    },

  },

  mounted() {
    const thisBis = this
    // gestion des évènement liés au keyboard
    window.addEventListener('keyup', function(event) {
      // arrow left
      if (event.keyCode == 37) {
        thisBis.reduceCurrentQuestionIndex()
      // arrow right
      } else if (event.keyCode == 39) {
        thisBis.setCurrentQuestionIndex(thisBis.currentQuestionIndex+1)
      // escape
      } else if (event.keyCode == 27) {
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
</style>

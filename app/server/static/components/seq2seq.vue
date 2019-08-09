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

  section.todoapp(v-if="!currentQuestion")
    header.header
      input.textarea.new-todo(
        v-model="newTodo"
        v-on:keyup.enter="addTodo"
        type="text"
        placeholder="Écrire une question"
      )

  questionInput(
    v-bind:buttonMessage="`Edit`"
    v-bind:currentQuestion="currentQuestion"
  )

  answerInput(
    v-if="currentQuestion"
    v-on:increaseCurrentQuestionIndex="increaseCurrentQuestionIndex"
    v-bind:buttonMessage="`Edit`"
    v-on:updateAnswers="updateAnswers"
    v-on:updateEditAnswerMode="updateEditAnswerMode"
    v-bind:editAnswerMode="editAnswerMode"
    v-bind:answers="answers"
    v-bind:pageNumber="pageNumber"
    v-bind:currentQuestionIndex="currentQuestionIndex"
    v-bind:currentAnswer="currentAnswer"
  )
</template>

<script>
import annotationMixin from './annotationMixin';
import todoFocus from './directives';
import HTTP from './http';
import MessageInfo from './messageInfo.vue';
import NavigationButtons from './navigationButtons.vue';
import QuestionInput from './questionInput.vue';
import AnswerInput from './answerInput.vue';

export default {
  directives: { todoFocus },

  mixins: [annotationMixin],

  components: { MessageInfo, NavigationButtons, QuestionInput, AnswerInput},

  data: () => ({
    newTodo: '',
    editedTodo: null,
    currentQuestionIndex: 0,
    //- newAnswer: '',
    editedAnswer: null,
    answers: [[]],
    editAnswerMode: true,
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
    addTodo() {
      const value = this.newTodo && this.newTodo.trim();
      if (!value) {
        return;
      }

      const payload = {
        text: value,
      };

      if (!this.annotations[this.pageNumber]) {
        this.annotations[this.pageNumber] = []
      }
      // forcing the update for nested object
      let questionCopy = JSON.parse(JSON.stringify(this.annotations))
      questionCopy[this.pageNumber][this.currentQuestionIndex] = payload;
      this.annotations = questionCopy
      this.newTodo = '';
    },

    addTodoComplete() {
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

    removeTodo(todo) {
      const index = this.annotations[this.pageNumber].indexOf(todo);
      this.annotations[this.pageNumber].splice(index, 1);
    },

    editTodo(todo) {
      this.beforeEditCache = todo.text;
      this.editedTodo = todo;
    },

    doneEdit(todo) {
      if (!this.editedTodo) {
        return;
      }
      this.editedTodo = null;
      todo.text = todo.text.trim();
      if (!todo.text) {
        this.removeTodo(todo);
      }
      const docId = this.docs[this.pageNumber].id;

      console.log('is this enough ?',response);
    },

    doneEditComplete(todo) {
      // if (!this.editedTodo) {
      //   return;
      // }
      // this.editedTodo = null;
      // todo.text = todo.text.trim();
      // if (!todo.text) {
      //   this.removeTodo(todo);
      // }
      // const docId = this.docs[this.pageNumber].id;
      // HTTP.put(`docs/${docId}/annotations/${todo.id}`, todo).then((response) => {
      //   console.log(response); // eslint-disable-line no-console
      // });
    },

    cancelEdit(todo) {
      this.editedTodo = null;
      todo.text = this.beforeEditCache;
    },

    async submit() {
      const state = this.getState();
      this.url = `docs?q=${this.searchQuery}&seq2seq_annotations__isnull=${state}&offset=${this.offset}`;
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
      if (this.questionClass(i) !== 'notYetButton') {
        this.currentQuestionIndex=i
        this.editAnswerMode = false
      }else if(this.currentNumberOfQuestion === i && this.answers[this.pageNumber].length === this.currentNumberOfQuestion){
        this.currentQuestionIndex=i
        this.editAnswerMode = true
      }
    },

    reduceCurrentQuestionIndex(){
      if(this.currentQuestionIndex>0){
        this.currentQuestionIndex--
      }
    },

    increaseCurrentQuestionIndex(){
      if(this.currentQuestionIndex<4){
        this.currentQuestionIndex++
      }else{
        this.pageNumber++
      }
    },

    updateAnswers(answers) {
      this.answers = answers
    },
    updateEditAnswerMode(boo) {
      this.editAnswerMode = boo
    },

  },
};
</script>

<style scoped>
  .todoapp{
    border-radius: 4em;
  }
</style>

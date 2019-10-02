<template lang="pug">
  section.todoapp(
    v-bind:class="{ 'is-transparentbackground': isProtected}"
  )
    header.header.card-content
      div.columns.is-gapless.is-mobile.is-vertical-center
        p.column.is-11.new-todo.has-text-left.is-paddingless.is-shadowless(
          v-if="isProtected"
          v-model="editedAnswer"
          v-on:keyup.enter="doneEditAnswer(editedAnswer)"
        ) {{ currentAnswer.text }}
        input.column.is-11.new-todo.has-text-left.is-paddingless.is-shadowless(
          v-else
          v-model="newAnswer"
          v-on:keyup.enter="addAnswer"
          type="text"
          placeholder="Écrire une réponse"
        )
        a.column.is-1.is-rounded.button.is-inline-block.doneButton(
          v-on:click="onClick"
          v-bind:class="{ 'has-background-royalblue': !isProtected}"
        )
          span(v-if="isProtected") Edit
          span(v-else) Ok
</template>

<script>
export default {
  props: ['buttonMessage','answers','pageNumber','currentQuestionIndex','currentAnswer'],

  data: () => ({
    newAnswer: '',
    editedAnswer: null,
    beforeEditAnswerCache: null,
  }),

  computed: {
    isProtected(){
      return this.currentAnswer && this.editedAnswer === null
    }
  },

  methods: {
    addAnswer() {
      const value = this.newAnswer && this.newAnswer.trim();
      if (!value) {
        return;
      }

      const payload = {
        text: value,
      };

      // forcing the update for nested object
      let answersCopy = JSON.parse(JSON.stringify(this.answers))

      if (!answersCopy[this.pageNumber]) {
        answersCopy[this.pageNumber] = []
      }
      answersCopy[this.pageNumber][this.currentQuestionIndex] = payload;
      this.$emit('updateAnswers',answersCopy);
      this.newAnswer = '';
      this.editedAnswer = null
      if (this.currentQuestionIndex < 4) {
        this.$emit('increaseCurrentQuestionIndex');
      }
    },

    removeAnswer(answer) {
      const index = this.answers[this.pageNumber].indexOf(answer);
      let answersCopy = JSON.parse(JSON.stringify(this.answers))
      answersCopy[this.pageNumber].splice(index, 1);
      this.$emit('updateAnswers',answersCopy);
    },

    reInitialiseAnswerInputs(){
      this.newAnswer = ''
      this.editedAnswer = null;
      this.beforeEditAnswerCache = null;
    },

    editAnswer(answer) {
      this.beforeEditAnswerCache = answer.text;
      this.editedAnswer = answer;
    },

    cancelEditAnswer(answer) {
      this.reInitialiseAnswerInputs()
    },

    doneEditAnswer() {
      if (!this.editedAnswer) {
        return;
      }

      const payload = {
        text: this.editedAnswer.trim(),
      };

      let answersCopy = JSON.parse(JSON.stringify(this.answers))
      answersCopy[this.pageNumber][this.currentQuestionIndex] = payload;
      this.reInitialiseAnswerInputs()
      this.$emit('updateAnswers',answersCopy);
    },

    onClick(){
      if (this.isProtected) {
        this.editAnswer(this.currentAnswer)
      } else {
        this.addAnswer()
      }
    },

  },
}
</script>

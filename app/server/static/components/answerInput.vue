<template lang="pug">
  section.todoapp(
    v-bind:class="{ 'is-transparentbackground': !editAnswerMode}"
  )
    header.header.card-content.columns.is-gapless(v-if="editAnswerMode")
      input.column.is-mobile.is-vertical-center.is-11.new-todo.has-text-left.is-paddingless.is-shadowless(
        v-model="newAnswer"
        v-on:keyup.enter="addAnswer"
        type="text"
        placeholder="Écrire une réponse"
      )
      a.column.is-1.is-rounded.button.is-inline-block.doneButton.has-background-royalblue(
        v-on:click="switchEditAnswerMode"
      ) Ok

    header.header.card-content(v-if="!editAnswerMode")
      div.columns.is-gapless.is-mobile.is-vertical-center(
         v-if="currentAnswer"
      )
        p.column.is-11.new-todo.has-text-left.is-paddingless.is-shadowless {{ currentAnswer.text }}
        a.column.is-1.is-rounded.button.is-inline-block.doneButton(
          v-on:click="switchEditAnswerMode"
        ) Edit
      div.columns.is-gapless.is-mobile.is-vertical-center(
         v-if="!currentAnswer"
      )
        input.textarea.new-todo(
          v-model="newAnswer"
          v-on:keyup.enter="addAnswer"
          type="text"
          placeholder="Écrire une réponse"
        )
</template>

<script>
export default {
  props: ['buttonMessage','editAnswerMode','answers','pageNumber','currentQuestionIndex','currentAnswer'],

  data: () => ({
    newAnswer: '',
  }),

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
      this.$emit('updateEditAnswerMode',false);
      if (this.currentQuestionIndex < 4) {
        this.$emit('increaseCurrentQuestionIndex');
      }
    },

    removeAnswer(answer) {
      const index = this.answers[this.pageNumber].indexOf(answer);
      let answersCopy = JSON.parse(JSON.stringify(this.answers))
      answersCopy[this.pageNumber].splice(index, 1);
      this.$emit('updateAnswers',answersCopy);
      this.$emit('updateEditAnswerMode',true);
    },

    switchEditAnswerMode() {
      this.$emit('updateEditAnswerMode',!this.editAnswerMode);
    },

    // editAnswer(answer) {
    //   this.beforeEditAnswerCache = answer.text;
    //   this.editedAnswer = answer;
    //   this.$emit('updateEditAnswerMode',true);
    // },

    // cancelEditAnswer(answer) {
    //   this.editedAnswer = null;
    //   answer.text = this.beforeEditAnswerCache;
    //   this.$emit('updateEditAnswerMode',false);
    // },

    // doneEditAnswer(answer) {
    //   if (!this.editedAnswer) {
    //     return;
    //   }
    //   this.editedAnswer = null;
    //   answer.text = answer.text.trim();
    //   if (!answer.text) {
    //     this.removeAnswer(answer);
    //   }
    //   const docId = this.docs[this.pageNumber].id;
    //
    //   console.log('something to do ?');
    // },
  },
}
</script>

<template lang="pug">
  section.is-transparentbackground
    header.header.card-content
      div.columns.is-gapless.is-mobile.is-vertical-center
        p.column.new-todo.has-text-left.is-paddingless.is-shadowless(
          v-if="isProtected"
          v-model="editedInput"
          v-on:keyup.enter="doneEditInput(editedInput)"
        ) {{ currentJSON.text }}
        p.paddingright.column.new-todo.has-text-left.is-paddingless.is-shadowless.has-text-grey-light.is-italic.is-justifycontentright.is-flex(
          v-else
          ref="input"
        ) {{ placeholder }}
        a.is-rounded.button.is-inline-block.doneButton.has-text-weight-bold.is-size-5.hoverEffect(
          v-on:click="onClick"
          v-if="isLastQuestion"
          v-bind:class="{ 'has-background-royalblue': !isProtected}"
        ) {{ buttonMessage3 }}
        a.is-one-quarter-mobile.is-one-tenth-morethandesktop.is-one-fifth-tabletdesktop.is-rounded.button.is-inline-block.doneButton.has-text-weight-bold.is-size-5.hoverEffect(
          v-on:click="onClick"
          v-else
          v-bind:class="{ 'has-background-royalblue': !isProtected}"
        ) {{ buttonMessage }}
</template>

<style>
.paddingright{
  padding-right: 15px !important;
}
</style>

<script>
import Bus from './bus.js'

export default {
  props: ['buttonMessage1', 'buttonMessage2', 'buttonMessage3', 'JSONs', 'pageNumber', 'currentQuestionIndex', 'currentJSON','placeholder', 'questionIndexMax'],

  data: () => ({
    editedInput: null,
  }),

  computed: {
    isProtected(){
      return this.currentJSON && this.editedInput === null
    },
    buttonMessage(){
      return (this.isProtected) ? this.buttonMessage1 : this.buttonMessage2;
    },
    isLastQuestion(){
      return this.currentQuestionIndex >= this.questionIndexMax
    }
  },

  methods: {
    addJSON() {
      Bus.$emit('clicked-on-addAnswer')
    },

    addJSONwithText(json) {
      if (!json || typeof json !== 'object' || typeof json.response !== 'string' || typeof json.start_offset !== 'number') {
        return;
      }
      // forcing the update for nested object
      let JSONsCopy = JSON.parse(JSON.stringify(this.JSONs))
      if (!JSONsCopy[this.pageNumber]) {
        JSONsCopy[this.pageNumber] = []
      }
      JSONsCopy[this.pageNumber][this.currentQuestionIndex] = json;
      this.$emit('increaseCurrentQuestionIndex');
      this.$emit('updateJSONs',JSONsCopy);
      Bus.$emit('switch-editmode',false);

      this.editedInput = null
      if (this.isLastQuestion) {
        this.$emit('submitToDatabase');
      }
    },

    reInitialiseInputs(){
      this.editedInput = null;
    },

    editJSON(json) {
      this.editedInput = json;
      Bus.$emit('switch-editmode',true);
    },

    cancelEditJSON() {
      this.reInitialiseInputs()
    },

    doneEditInput() {
      if (!this.editedInput) {
        return;
      }

      const payload = {
        text: this.editedInput.trim(),
      };

      let JSONsCopy = JSON.parse(JSON.stringify(this.JSONs))
      JSONsCopy[this.pageNumber][this.currentQuestionIndex] = payload;
      this.reInitialiseInputs()
      this.$emit('updateJSONs',JSONsCopy);
    },

    onClick(){
      if (this.isProtected) {
        this.editJSON(this.currentJSON)
      } else {
        this.addJSON()
      }
    },

  },

  created() {
    Bus.$on('addAnswer-with-text', (answer) => {
        this.addJSONwithText(answer)
    })
    Bus.$on('clicked-on-removeAnswer', (answer) => {
        this.editJSON(this.currentJSON)
    })
  },

}
</script>

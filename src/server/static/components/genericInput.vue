<template lang="pug">
  section
    p.is-transparentbackground(
      v-if="!isProtected"
    ) Utilisez vos propres mots pour poser une question, dont la réponse est dans ce texte :
    header.header.card-content.todoapp.is-marginless(
      v-bind:class="{ 'is-transparentbackground': isProtected}"
    )
      div.columns.is-gapless.is-mobile.is-vertical-center
        p.column.new-todo.has-text-left.is-paddingless.is-shadowless.scrollable(
          v-if="isProtected"
          v-model="editedInput"
          v-on:keyup.enter="doneEditInput(editedInput)"
        ) {{ currentJSON.text }}
        input.column.new-todo.has-text-left.is-paddingless.placeholderDarker.is-shadowless(
          v-else
          v-model="newJSON"
          v-on:keyup.enter="addJSON"
          type="text"
          :placeholder="placeholder"
          ref="input"
        )
        a.column.is-one-third-mobile.is-one-tenth-morethandesktop.is-one-fifth-tabletdesktop.is-rounded.button.doneButton.has-text-weight-bold.is-size-5.is-flex.hoverEffect(
          v-on:click="onClick"
          v-bind:class="{ 'has-background-royalblue': !isProtected}"
        ) {{ buttonMessage }}
</template>

<style scoped>
.todoapp{
  border-radius: 4em;
}
section{
  margin-top:25px;
}
.scrollable{
  overflow: scroll;
}
</style>

<script>
export default {
  props: ['buttonMessage1', 'buttonMessage2', 'JSONs', 'pageNumber', 'currentQuestionIndex', 'currentJSON','placeholder'],

  data: () => ({
    newJSON: '',
    editedInput: null,
    beforeEditJSONCache: null,
  }),

  computed: {
    isProtected(){
      return this.currentJSON && this.editedInput === null
    },
    buttonMessage(){
      return (this.isProtected) ? this.buttonMessage1 : this.buttonMessage2;
    }
  },

  methods: {
    addJSON() {
      const value = this.newJSON && this.newJSON.trim();
      if (!value) {
        return;
      }

      const payload = {
        text: value,
      };

      // forcing the update for nested object
      let JSONsCopy = JSON.parse(JSON.stringify(this.JSONs))

      if (!JSONsCopy[this.pageNumber]) {
        JSONsCopy[this.pageNumber] = []
      }
      JSONsCopy[this.pageNumber][this.currentQuestionIndex] = payload;
      this.$emit('updateJSONs',JSONsCopy);
      this.newJSON = '';
      this.editedInput = null
      if (this.currentQuestionIndex < 4) {
        this.$emit('increaseCurrentQuestionIndex');
      }
    },

    // removeAnswer(json) {
    //   const index = this.JSONs[this.pageNumber].indexOf(json);
    //   let JSONsCopy = JSON.parse(JSON.stringify(this.JSONs))
    //   JSONsCopy[this.pageNumber].splice(index, 1);
    //   this.$emit('updateJSONs',JSONsCopy);
    // },

    reInitialiseInputs(){
      this.newJSON = ''
      this.editedInput = null;
      this.beforeEditJSONCache = null;
    },

    editJSON(json) {
      this.beforeEditJSONCache = json.text;
      this.editedInput = json;
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
        this.$nextTick(() => this.$refs.input.focus())
      } else {
        this.addJSON()
      }
    },

  },
  created: function() {
    // we need to wait 1sec because DOM isn't defined otherwise
    setTimeout(x => {
      this.$nextTick(() => this.$refs.input.focus());
    }, 1000);
  },
}
</script>

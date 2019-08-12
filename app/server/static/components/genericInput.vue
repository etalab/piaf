<template lang="pug">
  section.todoapp(
    v-bind:class="{ 'is-transparentbackground': isProtected}"
  )
    header.header.card-content
      div.columns.is-gapless.is-mobile.is-vertical-center
        p.column.is-11.new-todo.has-text-left.is-paddingless.is-shadowless(
          v-if="isProtected"
          v-model="editedInput"
          v-on:keyup.enter="doneEditInput(editedInput)"
        ) {{ currentJSON.text }}
        input.column.is-11.new-todo.has-text-left.is-paddingless.is-shadowless(
          v-else
          v-model="newJSON"
          v-on:keyup.enter="addJSON"
          type="text"
          :placeholder="placeholder"
        )
        a.column.is-1.is-rounded.button.is-inline-block.doneButton(
          v-on:click="onClick"
          v-bind:class="{ 'has-background-royalblue': !isProtected}"
        )
          span(v-if="isProtected") {{ buttonMessage1 }}
          span(v-else) {{ buttonMessage2 }}
</template>

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

    cancelEditJSON(json) {
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
}
</script>

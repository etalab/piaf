<template>
  <section>
    <div class="columns is-gapless is-mobile is-vertical-center">
      <v-text-field
      v-model="editedInput"
      v-bind:label="currentAnnotation.question"
      v-if="isProtected"
      disabled
      v-on:keyup.enter="doneEditInput(editedInput)">
      </v-text-field>

      <v-text-field
      v-else
      v-model="newJSON"
      v-on:keyup.enter="addJSON"
      ref="input"
      label="Question">
        <template v-slot:label>
          Allez-y: posez ici une <strong>question</strong> en utilisant vos propres mots ! (Le réponse doit être dans le texte)
        </template>
      </v-text-field>

      <v-btn
      small
      color="primary"
      dark
      v-if="isProtected"
      v-on:click="onClick"
      >Modifier
      </v-btn>
      <v-btn
      small
      color="primary"
      dark
      v-else
      v-on:click="onClick"
      class="has-background-royalblue">OK
      </v-btn>
    </div>
  </section>
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
import { mapState } from 'vuex'

export default {
  data: () => ({
    newJSON: '',
    editedInput: null,
    beforeEditJSONCache: null,
  }),

  computed: {
    ...mapState([
      'currentDocument',
      'annotations',
      'currentQuestionIndex'
    ]),
    isProtected(){
      return this.currentAnnotation && this.editedInput === null
    },
    currentAnnotation () {
      return this.$store.getters.currentAnnotation
    },
  },

  methods: {
    addJSON() {
      const value = this.newJSON && this.newJSON.trim();
      if (!value) {
        return;
      }

      const payload = {
        question: value,
      };

      // forcing the update for nested object
      let JSONsCopy = JSON.parse(JSON.stringify(this.annotations))

      if (!JSONsCopy) {
        JSONsCopy = []
      }
      JSONsCopy[this.currentQuestionIndex] = payload;
      this.$store.commit('setAnnotations', JSONsCopy)
      this.newJSON = '';
      this.editedInput = null
    },

    reInitialiseInputs(){
      this.newJSON = ''
      this.editedInput = null;
      this.beforeEditJSONCache = null;
    },

    editJSON(json) {
      this.beforeEditJSONCache = json.question;
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
        question: this.editedInput.trim(),
      };

      let JSONsCopy = JSON.parse(JSON.stringify(this.annotations))
      JSONsCopy[this.currentQuestionIndex] = payload;
      this.reInitialiseInputs()
      this.$store.commit('setAnnotations', JSONsCopy)
    },

    onClick(){
      if (this.isProtected) {
        this.editJSON(this.currentAnnotation)
        // this.$nextTick(() => this.$refs.input.focus())
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

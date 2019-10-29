<template>
  <section>
    <div>
      <v-text-field
      v-bind:value="currentAnnotation.question.text"
      v-if="isProtected"
      disabled
      >
      </v-text-field>

      <v-text-field
      v-else
      v-model="newQuestion"
      v-on:keyup.enter="onClick"
      ref="input"
      label="Question">
        <template v-slot:label>
          Allez-y: posez ici une question en utilisant vos propres mots ! (La réponse doit être dans le texte)
        </template>
      </v-text-field>

      <v-btn
      v-if="currentQuestionIndex > 0 && !isProtected"
      class="mr-10"
      fab
      dark
      x-small
      outlined
      color="secondary"
      v-on:click="reduceIndex">
        <v-icon dark>mdi-arrow-left</v-icon>
      </v-btn>


      <v-btn
      small
      color="primary"
      dark
      v-if="newQuestion !== '' && !isProtected"
      v-on:click="onClick"
      class="has-background-royalblue">Suivant
      </v-btn>

      <v-btn
      small
      disabled
      color="primary"
      v-if="newQuestion === '' && !isProtected"
      >Suivant
      </v-btn>


      <!-- <v-btn
      v-if="currentQuestionIndex < numOfFinishedQA && !isProtected"
      class="mr-10"
      fab
      dark
      x-small
      outlined
      color="secondary"
      v-on:click="next">
        <v-icon dark>mdi-arrow-right</v-icon>
      </v-btn> -->

    </div>
  </section>
</template>

<style scoped>
.todoapp{
  border-radius: 4em;
}
section{
  margin-top:0px;
}
.scrollable{
  overflow: scroll;
}
</style>

<script>
import { mapState } from 'vuex'

export default {
  data: () => ({
    newQuestion: '',
  }),

  computed: {
    ...mapState([
      'currentDocument',
      'annotations',
      'currentQuestionIndex',
      'editMode',
      'numOfFinishedQA'
    ]),
    isProtected(){
      return this.$store.getters.hasQuestion && this.editMode === false
    },
    currentAnnotation () {
      return this.$store.getters.currentAnnotation
    },
  },

  methods: {
    addJSON() {
      const value = this.newQuestion && this.newQuestion.trim();
      if (!value) {
        return;
      }

      // forcing the update for nested object
      let JSONsCopy = JSON.parse(JSON.stringify(this.annotations))

      if (!JSONsCopy) {
        JSONsCopy = []
      }

      const annotation = JSONsCopy[this.currentQuestionIndex]
      annotation.question.text = value

      JSONsCopy[this.currentQuestionIndex] = annotation;
      this.$store.commit('setAnnotations', JSONsCopy)
      this.newQuestion = '';
    },

    reInitialiseInputs(){
      this.newQuestion = ''
      this.$store.commit('setEditeMode',false)
    },

    cancelEditJSON() {
      this.reInitialiseInputs()
    },

    onClick(){
      // if (this.isProtected) {
      //   this.$store.commit('setEditeMode',true)
      //   // this.$nextTick(() => this.$refs.input.focus())
      // } else {
      this.$store.commit('setEditeMode',false)
      this.addJSON()
      // }
    },

    reduceIndex(){
      if (this.currentQuestionIndex > 0) {
        this.$store.commit('setEditeMode',false)
        this.$store.commit('setCurrentQuestionIndex', this.currentQuestionIndex - 1)
        this.$store.dispatch('syncAnswerWithHighliting')
      }
    },

    // next(){
    //   this.$store.commit('setEditeMode',false)
    //   return this.$store.commit('goToNextIndex')
    // },

  },
  created: function() {
    // we need to wait 1sec because DOM isn't defined otherwise
    setTimeout(() => {
      if (!this.isProtected) {
        this.$nextTick(() => this.$refs.input.focus());
      }
    }, 400);
  },
}
</script>

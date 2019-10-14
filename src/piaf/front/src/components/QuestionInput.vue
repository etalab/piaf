<template>
  <section>
    <div class="columns is-gapless is-mobile is-vertical-center">
      <v-text-field
      v-bind:value="currentAnnotation.question"
      v-if="isProtected"
      disabled
      >
      </v-text-field>

      <v-text-field
      v-else
      v-model="newQuestion"
      v-on:keyup.enter="addJSON"
      ref="input"
      label="Question">
        <template v-slot:label>
          Allez-y: posez ici une question en utilisant vos propres mots ! (Le réponse doit être dans le texte)
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
    newQuestion: '',
  }),

  computed: {
    ...mapState([
      'currentDocument',
      'annotations',
      'currentQuestionIndex',
      'editMode'
    ]),
    isProtected(){
      return this.currentAnnotation.question !== '' && this.editMode === false
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
      annotation.question = value

      JSONsCopy[this.currentQuestionIndex] = annotation;
      this.$store.commit('setAnnotations', JSONsCopy)
      this.newQuestion = '';
      this.$store.commit('setEditeMode',false)
    },

    reInitialiseInputs(){
      this.newQuestion = ''
      this.$store.commit('setEditeMode',false)
    },

    cancelEditJSON() {
      this.reInitialiseInputs()
    },

    onClick(){
      if (this.isProtected) {
        this.$store.commit('setEditeMode',true)
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

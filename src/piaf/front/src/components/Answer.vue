<template>
  <section class="is-transparentbackground">
    <header class="header card-content">
      <div class="columns is-gapless is-mobile is-vertical-center">
          <p v-if="!isProtected" ref="input">
            <i class="fa fa-info-circle mr5"></i>
            Surligner la réponse dans le texte
          </p>

          <v-btn
          small
          color="primary"
          dark
          v-if="isLastQuestion"
          v-on:click="onClick"
          v-bind:class="{ 'has-background-royalblue': !isProtected}"
          >Valider + envoyer
          </v-btn>

          <v-btn
          small
          color="primary"
          dark
          v-if="!isLastQuestion && !isProtected"
          v-on:click="onClick"
          v-bind:class="{ 'has-background-royalblue': !isProtected}"
          >Valider
          </v-btn>

      </div>
    </header>
  </section>
</template>

<style scoped>
.paddingright{
  padding-right: 15px !important;
}
.has-text-left{
  justify-content: end;
}
.has-background-royalblue{
  background-color:royalblue !important;
}
</style>

<script>
import { mapState } from 'vuex'

export default {
  props: ['JSONs',],

  data: () => ({
    editedInput: null,
  }),

  computed: {
    ...mapState([
      'currentDocument',
      'annotations',
      'currentQuestionIndex',
      'maxAnnotationsPerDoc'
    ]),
    isProtected(){
      return this.currentAnnotation.answer && this.editedInput === null
    },
    currentAnnotation () {
      return this.$store.getters.currentAnnotation
    },
    isLastQuestion(){
      return this.currentQuestionIndex >= (this.maxAnnotationsPerDoc - 1)
    }
  },

  methods: {
    addJSON() {
      // Bus.$emit('clicked-on-addAnswer')
    },

    addJSONwithText(json) {
      if (!json || typeof json !== 'object' || typeof json.response !== 'string' || typeof json.start_offset !== 'number') {
        return;
      }
      // forcing the update for nested object
      let JSONsCopy = JSON.parse(JSON.stringify(this.annotations))
      if (!JSONsCopy) {
        JSONsCopy = []
      }
      JSONsCopy[this.currentQuestionIndex] = json;
      this.$store.commit('setAnnotations', JSONsCopy)
      // Bus.$emit('switch-editmode',false);

      this.editedInput = null
      if (this.isLastQuestion) {
        // this.$emit('submitToDatabase');
      }
    },

    reInitialiseInputs(){
      this.editedInput = null;
    },

    editJSON(json) {
      this.editedInput = json;
      // Bus.$emit('switch-editmode',true);
    },

    cancelEditJSON() {
      this.reInitialiseInputs()
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

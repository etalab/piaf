<template>
  <section class="is-transparentbackground">
    <header class="header card-content">
      <div class="columns is-gapless is-mobile is-vertical-center">
          <v-btn
          small
          color="primary"
          dark
          v-if="!isProtected"
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
      return this.$store.getters.hasAnswer && this.editedInput === null
    },
    currentAnnotation () {
      return this.$store.getters.currentAnnotation
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
        this.$store.dispatch('addNewHighlitedText')
      }
    },

  },

}
</script>

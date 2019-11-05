<template>
  <v-flex xs12 my-0 justify-center class="container">
    <v-row class="maxWid700 mx-auto textContainer bold"
    v-if="annotationFooter">
      <span xs12 justify-center my-0 v-if="!this.$store.getters.hasQuestion">
          <v-tooltip left v-bind:open-on-click=true open-delay=1000>
            <template v-slot:activator="{ on }">
                <span v-on="on">
                Écrire une question :
                <v-icon fab small dark class="grey--text" >mdi-information-outline</v-icon>
                </span>
            </template>
            <span>Après avoir lu le texte ci-dessus, écrivez une question en utilisant vos propres mots. La réponse doit être dans le texte. Vous avez peur de faire des fautes d'orthographe ? Pas grave: l'IA comprendra mieux le français en général, y compris celui de monsieur tout le monde... On ne s'appelle pas tous Bernard Pivot</span>
          </v-tooltip>
      </span>

      <span xs12 justify-center my-5 v-if="!this.$store.getters.hasAnswer && this.editMode === false && this.$store.getters.hasQuestion">
          <v-tooltip left v-bind:open-on-click=true open-delay=1000>
            <template v-slot:activator="{ on }">
                <span v-on="on">
                  Surligner une réponse dans le texte :
                  <v-icon fab small dark class="grey--text" >mdi-information-outline</v-icon>
                </span>
            </template>
            <span>Après avoir posé une question sur ce texte, vous pouvez indiquer à l'IA où se trouve la réponse.<br> Pour ça, cliquez sur le premier mot de la réponse, puis sur le dernier mot.</span>
          </v-tooltip>
      </span>

    </v-row>
    <v-row class="maxWid700 mx-auto textContainer bold"
    v-if="lastValidationFooter">
      Bravo !
    </v-row>
    <v-row class="maxWid700 mx-auto"
    v-if="annotationFooter">
      <v-col cols='12'>
        <QuestionInput class="maxWid700 mx-auto"/>

        <span v-if="this.$store.getters.hasQuestion">
          <Answer
            v-if="currentAnnotation && currentAnnotation.question.text !== ''"
            class="maxWid700 mx-auto"
          />
        </span>
      </v-col>
    </v-row>
    <v-row class="maxWid700 mx-auto"
    v-if="lastValidationFooter">
      <v-col cols='12' class="pr-0 textContainer">

        <v-btn
        class="mx-2"
        fab
        dark
        x-small
        outlined
        color="secondary"
        v-on:click="removeAnswer">
          <v-icon dark>mdi-arrow-left</v-icon>
        </v-btn>

        <v-btn
        v-if="currentQuestionIndex === 4"
        small
        color="primary"
        dark
        v-on:click="validate"
        class="alignSelf"
        >Valider mes 5 questions
        </v-btn>


        <v-btn
        v-else
        small
        color="primary"
        dark
        v-on:click="next"
        class="alignSelf"
        >Continuer
        </v-btn>

      </v-col>
    </v-row>
  </v-flex>
</template>

<script>
import { mapState } from 'vuex'
import QuestionInput from './QuestionInput.vue';
import Answer from './Answer.vue';

export default {
  components: { QuestionInput, Answer },
  computed: {
    ...mapState([
      'currentQuestionIndex',
      'editMode',
      'showFooter',
      'showTheme',
    ]),
    currentAnnotation () {
      return this.$store.getters.currentAnnotation
    },
    lastValidationFooter () {
      return !this.showTheme && this.showFooter
    },
    annotationFooter () {
      return !this.showTheme && !this.showFooter
    },
  },
  methods:{
    validate(){
      let res = this.$store.dispatch('saveQAs')
      if (res) {
        this.next()
      } else {
        // eslint-disable-next-line
        console.log('error in the Q or A');
      }
    },
    next(){
      this.$store.commit('setShowFooter',false)
      return this.$store.dispatch('goToNextIndex')
    },
    removeAnswer(){
      return this.$store.dispatch('removeAnswer')
    },
  },
};
</script>

<style scoped>
/* for all */
.maxWid700{
  max-width: 700px;
}
.alignSelf{
  align-self: center;
}
.container{
}
.textContainer{
  display: flex;
  justify-content: space-around;
}
</style>

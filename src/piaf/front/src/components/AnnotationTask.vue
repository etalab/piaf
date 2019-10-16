<template>
  <v-container>
    <v-layout
      text-center
      wrap
    >

      <v-flex xs12 my-5>
        <div>
          <div v-if="currentDocument && annotations">
            <v-card
              max-width="700"
              class="mx-auto"
            >
              <v-card-text>
                <TextInteractive
                  v-bind:text="currentDocument.text"
                  v-bind:currentQuestionIndex="currentQuestionIndex"
                  ref="annotator"
                 />
             </v-card-text>
            </v-card>
          </div>
        </div>
      </v-flex>


      <v-flex xs12 justify-center my-0 v-if="!this.$store.getters.hasQuestion">
        <v-flex align-center>
          <v-tooltip left>
            <template v-slot:activator="{ on }">
              <i>
                Écrire une quesiton :
                <v-icon v-on="on" fab small dark class="grey--text" >mdi-information-outline</v-icon>
              </i>
            </template>
            <span>Après avoir lu le texte ci-dessus, écrivez une question en utilisant vos propres mots. La réponse doit être dans le texte. Vous avez peur de faire des fautes d'orthographe ? Pas grave: l'IA comprendra mieux le français en général, y compris celui de monsieur tout le monde... On ne s'appelle pas tous Bernard Pivot</span>
          </v-tooltip>
        </v-flex>
      </v-flex>

      <v-flex xs12 my-0>
        <QuestionInput class="maxWid700 mx-auto"/>
      </v-flex>

      <v-flex xs12 justify-center my-5 v-if="!this.$store.getters.hasAnswer && this.$store.getters.hasQuestion">
        <v-flex align-center>
          <v-tooltip left>
            <template v-slot:activator="{ on }">
              <i>
                Surligner une réponse dans le texte :
                <v-icon v-on="on" fab small dark class="grey--text" >mdi-information-outline</v-icon>
              </i>
            </template>
            <span>Après avoir posé une question sur ce texte, vous pouvez indiquer à l'IA où se trouve la réponse. Pour ça, surligner la réponse dans le texte puis validez.</span>
          </v-tooltip>
        </v-flex>
      </v-flex>

      <v-flex xs12 my-10 v-if="this.$store.getters.hasQuestion">
        <Answer
          v-if="currentAnnotation && currentAnnotation.question.text !== ''"
          class="maxWid700 mx-auto"
        />
      </v-flex>

      <v-flex xs12 my-0 justify-center>
        <v-row class="maxWid700 mx-auto">
          <v-col
            cols='1'
            v-on:click="reduceIndex"
          >
            <v-btn class="mx-2" fab dark x-small color="primary">
              <v-icon dark>mdi-arrow-left-drop-circle</v-icon>
            </v-btn>
          </v-col>

          <!-- <v-col
            cols='1'
            v-on:click="nextqa"
          >
            <v-btn class="mx-2" fab dark x-small color="primary">
              <v-icon dark>mdi-arrow-right-drop-circle</v-icon>
            </v-btn>
          </v-col> -->
        </v-row>
      </v-flex>


      <v-btn
      small
      color="primary"
      dark
      v-on:click="validate"
      >Valider QA
      </v-btn>

      <v-btn
      small
      color="primary"
      dark
      v-on:click="nextqa"
      >next QA
      </v-btn>

    </v-layout>
  </v-container>
</template>

<script>
import { mapState } from 'vuex'
import TextInteractive from './TextInteractive.vue';
import QuestionInput from './QuestionInput.vue';
import Answer from './Answer.vue';

export default {
  components: { TextInteractive, QuestionInput, Answer },
  data: () => ({
    e1: 0,
  }),
  computed: {
    ...mapState([
      'currentDocument',
      'annotations',
      'currentQuestionIndex'
    ]),
    currentAnnotation () {
      return this.$store.getters.currentAnnotation
    },
  },
  methods: {
    validate(){
      return this.$store.dispatch('saveQAs')
    },
    nextqa(){
      return this.$store.dispatch('goToNextIndex')
    },
    reduceIndex(){
      if (this.currentQuestionIndex > 0) {
        return this.$store.commit('setCurrentQuestionIndex', this.currentQuestionIndex - 1)
      }
    },

  },
};
</script>

<style scoped>
.maxWid700{
  max-width: 700px;
}
</style>

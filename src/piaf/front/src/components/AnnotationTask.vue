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
                <v-tooltip left v-bind:open-on-click=true open-delay=1000>
                  <template v-slot:activator="{ on }">
                    <span v-on="on">
                      <span v-html="currentDocument.title"></span>
                      <v-icon fab small dark class="grey--text ml-1" >mdi-information-outline</v-icon>
                    </span>
                  </template>
                  <span>Titre de l'article Wikipédia dont est extrait ce texte</span>
                </v-tooltip>
                <br>
                <v-alert
                  dense
                  outlined
                  type="error"
                  v-show="showErrorMessage"
                >
                  La réponse est <strong>trop longue</strong>, elle doit faire moins de 200 caractères
                </v-alert>
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
          <v-tooltip left v-bind:open-on-click=true open-delay=1000>
            <template v-slot:activator="{ on }">
                <span v-on="on">
                Écrire une question :
                <v-icon fab small dark class="grey--text" >mdi-information-outline</v-icon>
                </span>
            </template>
            <span>Après avoir lu le texte ci-dessus, écrivez une question en utilisant vos propres mots. La réponse doit être dans le texte. Vous avez peur de faire des fautes d'orthographe ? Pas grave: l'IA comprendra mieux le français en général, y compris celui de monsieur tout le monde... On ne s'appelle pas tous Bernard Pivot</span>
          </v-tooltip>
        </v-flex>
      </v-flex>

      <v-flex xs12 my-0>
        <QuestionInput class="maxWid700 mx-auto"/>
      </v-flex>

      <v-flex xs12 justify-center my-5 v-if="!this.$store.getters.hasAnswer && this.editMode === false && this.$store.getters.hasQuestion">
        <v-flex align-center>
          <v-tooltip left v-bind:open-on-click=true open-delay=1000>
            <template v-slot:activator="{ on }">
                <span v-on="on">
                  Surligner une réponse dans le texte :
                  <v-icon fab small dark class="grey--text" >mdi-information-outline</v-icon>
                </span>
            </template>
            <span>Après avoir posé une question sur ce texte, vous pouvez indiquer à l'IA où se trouve la réponse.<br> Pour ça, cliquez sur le premier mot de la réponse, puis sur le dernier mot.</span>
          </v-tooltip>
        </v-flex>
      </v-flex>

      <v-flex xs12 my-0 v-if="this.$store.getters.hasQuestion">
        <Answer
          v-if="currentAnnotation && currentAnnotation.question.text !== ''"
          class="maxWid700 mx-auto"
        />
      </v-flex>



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
      'currentQuestionIndex',
      'editMode',
      'highlitedText'
    ]),
    currentAnnotation () {
      return this.$store.getters.currentAnnotation
    },
    showErrorMessage () {
      return typeof this.highlitedText === 'string' && this.highlitedText.length > 200
    },
  },
};
</script>

<style scoped>
.maxWid700{
  max-width: 700px;
}
</style>

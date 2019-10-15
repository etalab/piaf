<template>
  <v-container>
    <v-layout
      text-center
      wrap
    >

      <v-flex xs12>
        <h1 class="display-2 font-weight-bold">
          Annotation
        </h1>
      </v-flex>

      <v-flex xs12 justify-center my-5>
        <v-flex align-center>
          Le texte que vous allez lire est extrait d'un article Wikipédia dont le titre est : {{ currentDocument.title }}
        </v-flex>
      </v-flex>


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
          <v-col cols='10' v-bind:style="{ alignSelf: 'center' }">
            <v-progress-linear
              v-bind:value="stepPercentage"
              color="#1b4597"
              height="25"
              rounded
              striped
              v-bind:style="{ borderRadius: 30 + 'px' }"
            >
              <template v-slot="{ value }">
                <span class="white--text">Question {{ Math.ceil(value / 20 ) + 1 }} / 5</span>
              </template>
            </v-progress-linear>
          </v-col>
          <v-col
            cols='1'
            v-on:click="nextqa"
          >
            <v-btn class="mx-2" fab dark x-small color="primary">
              <v-icon dark>mdi-arrow-right-drop-circle</v-icon>
            </v-btn>
          </v-col>
        </v-row>
      </v-flex>

      <v-flex xs12 my-0>
        <QuestionInput class="maxWid700 mx-auto"/>
      </v-flex>


      <v-flex xs12 my-10>
        <Answer
          v-if="currentAnnotation && currentAnnotation.question.text !== ''"
          class="maxWid700 mx-auto"
        />
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
    // stepPercentage: 80,
    e1: 0,
  }),
  computed: {
    ...mapState([
      'currentDocument',
      'annotations',
      'currentQuestionIndex'
    ]),
    stepPercentage(){
      return this.currentQuestionIndex * 20
    },
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

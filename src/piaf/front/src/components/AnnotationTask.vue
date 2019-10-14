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
        <v-progress-linear
          v-bind:value="stepPercentage"
          color="#130c47"
          background-color=""
          height="25"
          rounded
          class="maxWid700 mx-auto"
        >
          <template v-slot="{ value }">
            <span class="white--text">Question {{ Math.ceil(value / 20 ) }} / 5</span>
          </template>
        </v-progress-linear>
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


      <!-- <v-flex xs12 my-10>
        <v-row>
          <v-text-field>
            <template v-slot:label>
              Allez-y: posez une <strong>question</strong> en utilisant vos propres mots !
            </template>
          </v-text-field>
          <v-btn
            color="primary"
            @click="e1 = 3"
          >
            Continuer
          </v-btn>
        </v-row>
      </v-flex> -->
      <!-- <v-flex xs12 my-10>
        <v-stepper v-model="e1">
          <v-stepper-items>
            <v-stepper-content step="1">
              <v-container>
                <v-text-field>
                  <template v-slot:label>
                    Allez-y: posez ici une <strong>question</strong> en utilisant vos propres mots ! (Le réponse doit être dans le texte)
                  </template>
                </v-text-field>
              </v-container>
              <v-btn
                color="primary"
                @click="e1 = 2"
              >
                Continuer
              </v-btn>
              <v-btn
                color="primary"
                @click="e1 = 2"
              >
                Surliner la réponse et valider en cliquant ici
              </v-btn>
            </v-stepper-content>

            <v-stepper-content step="2">
              <v-container>
                <v-text-field>
                  <template v-slot:label>
                    Allez-y: posez une <strong>question</strong> en utilisant vos propres mots !
                  </template>
                </v-text-field>
              </v-container>
              <v-btn
                color="primary"
                @click="e1 = 3"
              >
                Continuer
              </v-btn>
            </v-stepper-content>

            <v-stepper-content step="3">
              <v-container>
                <v-text-field>
                  <template v-slot:label>
                    Allez-y: posez une <strong>question</strong> en utilisant vos propres mots !
                  </template>
                </v-text-field>
              </v-container>
              <v-btn
                color="primary"
                @click="e1 = 4"
              >
                Continuer
              </v-btn>
            </v-stepper-content>

            <v-stepper-content step="4">
              <v-container>
                <v-text-field>
                  <template v-slot:label>
                    Allez-y: posez une <strong>question</strong> en utilisant vos propres mots !
                  </template>
                </v-text-field>
              </v-container>
              <v-btn
                color="primary"
                @click="e1 = 5"
              >
                Continuer
              </v-btn>
            </v-stepper-content>

            <v-stepper-content step="5">
              <v-container>
                <v-text-field>
                  <template v-slot:label>
                    Allez-y: posez une <strong>question</strong> en utilisant vos propres mots !
                  </template>
                </v-text-field>
              </v-container>
              <v-btn
                color="primary"
                @click="e1 = 1"
              >
                Revenir au premier
              </v-btn>

              <v-btn text>Cancel</v-btn>
            </v-stepper-content>
          </v-stepper-items>
        </v-stepper>
      </v-flex> -->

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
      return this.$store.commit('setCurrentQuestionIndex',this.currentQuestionIndex+1)
    },

  },
};
</script>

<style scoped>
.maxWid700{
  max-width: 700px;
}
</style>

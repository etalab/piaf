<template>
  <v-flex xs12 my-0 justify-center class="container">
    <v-row class="maxWid700 mx-auto textContainer bold"
    v-if="showContinue">
      Bravo !
    </v-row>
    <v-row class="maxWid700 mx-auto textContainer bold red--text"
    v-if="networkIssueMessage">
      Pas de connexion, veuillez recommencer
    </v-row>
    <v-row class="maxWid700 mx-auto"
    v-if="!showContinue">
      <v-col cols='12' style="display:flex;justify-content:center;text-align:center">

        <span v-if="currentAnnotation && currentAnnotation.question.text && currentAnnotation.question.text !== ''">
          <span class="font-weight-thin zind0 questionClass white--text" style="background-color:#161b50">
            {{currentAnnotation.question.text}}
          </span>
          <br>
          <span>
            Cliquer sur la réponse à cette question dans le texte au-dessus
          </span>
          <br>
          <span>

            <v-btn
            class="mr-10"
            fab
            dark
            x-small
            outlined
            color="secondary"
            v-if="currentQuestionIndex > 0"
            v-on:click="removeAnswerAndReduceIndex">
              <v-icon dark>mdi-arrow-left</v-icon>
            </v-btn>

            <v-btn
            small
            color="primary"
            dark
            v-if="typeof highlitedText === 'string' && highlitedText.length < 200"
            v-on:click="onClick"
            >Valider
            </v-btn>

            <v-btn
            small
            disabled
            v-else
            >Valider
            </v-btn>
          </span>

        </span>
        <span v-else>
          Pas de question disponible. Essayez de produire des Questions-réponses complètes!
          <br>
          <v-btn
          class="mx-2"
          dark
          small
          color="primary"
          v-on:click="$router.push('/')">
            Faire des Questions-Réponses
          </v-btn>

        </span>

      </v-col>
    </v-row>
    <v-row class="maxWid700 mx-auto"
    v-if="showContinue">
      <v-col cols='12' class="pr-0 textContainer">

        <v-btn
        class="mx-2"
        fab
        dark
        x-small
        outlined
        color="secondary"
        v-if="!loading"
        v-on:click="removeAnswer">
          <v-icon dark>mdi-arrow-left</v-icon>
        </v-btn>

        <v-btn
        v-if="currentQuestionIndex === 4"
        small
        color="primary"
        dark
        :loading="loading"
        v-on:click="validate"
        class="alignSelf"
        >Valider mes 5 réponses
          <template v-slot:loading>
            <span>
              <v-icon light>cached</v-icon>
            </span>
          </template>
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
import Answer from './Answer.vue';

export default {
  data(){
    return {
      loading: false,
      networkIssueMessage: false,
    }
  },
  props: {
    routeAfterValidation: String,
  },
  components: { Answer },
  computed: {
    ...mapState([
      'currentQuestionIndex',
      'editMode',
      'showContinue',
      'highlitedText',
      'editMode'
    ]),
    currentAnnotation () {
      return this.$store.getters.currentAnnotation
    },
  },
  methods:{
    async validate(){
      this.$emit('validation')
      this.loading = true
      let res = await this.$store.dispatch('saveAs')
      this.loading = false
      if (res) {
        this.next()
        this.$router.push(this.routeAfterValidation)
      } else {
        // eslint-disable-next-line
        console.log('error in the additional Answers');
        this.networkIssueMessage = true
      }
    },
    next(){
      this.$store.commit('setshowContinue',false)
      return this.$store.dispatch('goToNextIndexAnswerMode')
    },
    removeAnswer(){
      return this.$store.dispatch('removeAnswer')
    },
    onClick(){
      this.$store.dispatch('addNewHighlitedText')
      this.$store.commit('setshowContinue',true)
    },
    reduceIndex(){
      if (this.currentQuestionIndex > 0) {
        this.$store.commit('setEditeMode',false)
        this.$store.commit('setCurrentQuestionIndex', this.currentQuestionIndex - 1)
        this.$store.dispatch('syncAnswerWithHighliting')
      }
    },
    removeAnswerAndReduceIndex(){
      this.removeAnswer()
      this.reduceIndex()
    }
  },
};
</script>

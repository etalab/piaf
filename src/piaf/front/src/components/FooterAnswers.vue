<template>
  <v-flex xs12 my-0 justify-center class="container">
    <v-row class="maxWid700 mx-auto textContainer bold red--text"
    v-if="networkIssueMessage">
      Pas de connexion, veuillez recommencer
    </v-row>
    <v-row class="maxWid700 mx-auto">
      <v-col cols='12' style="display:flex;justify-content:center;text-align:center">

        <span v-if="currentAnnotation && currentAnnotation.question.text && currentAnnotation.question.text !== ''">
          <span
          class="font-weight-thin zind0 questionClass white--text"
          style="background-color:#161b50">
            {{currentAnnotation.question.text}}
          </span>
          <br>
          <span v-if="!isAnswerHighlited">
            Cliquer sur la réponse à cette question dans le texte au-dessus
          </span>
          <br>
          <span>

            <v-btn
            small
            color="primary"
            dark
            v-if="isAnswerHighlited"
            v-on:click="validate"
            :loading="loading"
            >Valider
              <template v-slot:loading>
                <span>
                  <v-icon light>cached</v-icon>
                </span>
              </template>
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
  </v-flex>
</template>

<script>
import { mapState } from 'vuex'

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
  computed: {
    ...mapState([
      'highlitedText',
    ]),
    currentAnnotation () {
      return this.$store.getters.currentAnnotation
    },
    isAnswerHighlited (){
      return typeof this.highlitedText === 'string' && this.highlitedText.length < 200
    },
  },
  methods:{
    async validate(){
      this.$store.dispatch('addNewHighlitedText')
      this.loading = true
      let res = await this.$store.dispatch('saveA')
      this.loading = false
      if (res) {
        this.$router.push(this.routeAfterValidation)
      } else {
        // eslint-disable-next-line
        console.log('error in the additional Answers');
        this.networkIssueMessage = true
      }
    },
  },
};
</script>

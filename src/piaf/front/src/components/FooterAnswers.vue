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

            <v-dialog v-model="dialog"  max-width="290">
              <template v-slot:activator="{ on }">
                <v-btn
                small
                text
                color="red darken-1"
                :loading="loading"
                class="mr-8"
                v-on="on"
                ><v-icon light>mdi-flag</v-icon> Signaler
                  <template v-slot:loading>
                    <span>
                      <v-icon light>cached</v-icon>
                    </span>
                  </template>
                </v-btn>
              </template>
              <v-card>
                <v-card-title class="headline">
                  <v-btn
                  color="grey darken-1" text @click="dialog = false"
                  style="position:absolute;top:5px;right:5px"
                  min-width=20
                  ><v-icon dark small>mdi-close</v-icon></v-btn>
                </v-card-title>
                <v-card-text>
                  <p>Signaler une question</p>
                  <br>
                  <p>Vous êtes tombé sur une question qui rencontre l'un de ces problèmes :</p>
                  <ul>
                    <li>Pas de réponse dans le texte</li>
                    <li>Contenu inaproprié</li>
                    <li>Autre</li>
                  </ul>
                  <br>
                  <p>Merci de nous le signaler. Nous regarderons tous les signalements à la main et corrigerons ou supprimerons les questions si nécessaire.</p>
                </v-card-text>
                <v-card-actions class="d-flex justify-center">
                  <v-btn color="red darken-1 white--text" @click="reportQuestion">Signaler</v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>

          </span>
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
      dialog: false,
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
    async reportQuestion(){
      this.loading = true
      let res = await this.$store.dispatch('reportQ')
      this.loading = false
      if (res) {
        this.$router.push(this.routeAfterValidation)
      } else {
        // eslint-disable-next-line
        console.log('error in reporting the question');
        this.networkIssueMessage = true
      }
    },
  },
};
</script>

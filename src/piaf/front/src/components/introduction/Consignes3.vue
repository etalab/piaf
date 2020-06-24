<template>
  <v-container class="maxWid700">
    <span v-if="step == 0">
      <v-layout justify-center>
        <span class="font-weight-thin mb-2 white--text zind0 title">Votre première annotation</span>
      </v-layout>
      <v-layout justify-center>
        <span class="font-weight-thin mt-5 white--text zind0">Une annotation est composée d'une question et de sa réponse.</span>
      </v-layout>
      <v-layout justify-center>
        <span class="font-weight-thin mt-5 white--text zind0">Un texte a besoin de 5 questions-réponses pour être validé.</span>
      </v-layout>
    </span>
    <span v-if="[1,2].indexOf(step) !== -1">
      <v-layout justify-center>
        <span class="font-weight-thin mb-5 white--text ">Le titre de l'article wikipedia dont est extrait le texte est affiché au-dessus :</span>
      </v-layout>
      <!-- <v-card-text style="font-size:1em;line-height:1.7;"> -->
      <v-layout text-center wrap>
        <v-card max-width="700" class="mx-auto">
          <span class="black--text bold">Exemple de titre</span>
          <br>
          <v-card-text class="pa-2 consigneText">
            <span class="black--text bold">Ici c'est l'emplacement normal du texte</span>
          </v-card-text>
        </v-card>
      </v-layout>
      <v-layout justify-center v-if="step == 2">
        <span class="font-weight-thin mt-5 mb-5 white--text ">Le titre ne peut pas faire partie de la réponse.</span>
      </v-layout>
    </span>
    <span v-if="step == 3">
      <v-layout justify-center>
        <span class="font-weight-thin mb-2 white--text zind0 title">Choisissons un thème</span>
      </v-layout>
      <v-layout justify-center>
        <span class="font-weight-thin mt-2 white--text zind0">Les textes sont classés selon les thèmes suivant. Lequel préferez-vous ?</span>
      </v-layout>
      <v-layout row justify-center>
        <v-flex xs6 sm4 md3
          v-for="(theme) in themes"
          v-on:click="setCurrentTheme(theme)"
          :key="theme.name"
        >
          <div class="my-2 d-flex flex-column align-center">
            <v-btn fab large dark v-bind:color="theme.color" v-if="!theme.empty">
              <v-icon>{{theme.logo}}</v-icon>
            </v-btn>
            <span class="font-weight-thin white--text zind0">{{theme.name}}</span>
          </div>
        </v-flex>
      </v-layout>
    </span>
  </v-container>
</template>

<script>
import { mapState } from 'vuex'

export default {
  props: {
    step: Number
  },
  computed : {
    ...mapState([
      'themes',
    ]),
  },
  methods: {
    setCurrentTheme(theme){
      if(!theme.empty){
        this.$store.commit('setCurrentTheme', theme.name)
        this.$router.push("/introduction/"+Number(this.$route.params.level)+"/play")
      }
    },
  },
};
</script>
<style scoped>
.consigneText {
  font-size:1.2em;
  text-align: left;
  /* line-height:1.0; */
}
</style>

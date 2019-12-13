<template>
  <v-container class="maxWid700">
    <span v-if="step == 0">
      <v-layout justify-center>
        <span class="font-weight-thin mb-2 white--text zind0 title">Votre première annotation</span>
      </v-layout>
      <v-layout justify-center>
        <span class="font-weight-thin mt-5 white--text zind0">Une annotation est composée d'une question et de sa réponse</span>
      </v-layout>
      <v-layout justify-center>
        <span class="font-weight-thin mt-5 white--text zind0">À vous de jouer</span>
      </v-layout>
    </span>
    <span v-if="step == 1">
      <v-layout justify-center>
        <span class="font-weight-thin mb-2 white--text zind0 title">Choisissons un thème</span>
      </v-layout>
      <v-layout justify-center>
        <span class="font-weight-thin mt-5 white--text zind0">Les textes sont classés selon les thèmes suivant. Lequel préferez-vous ?</span>
      </v-layout>
      <v-layout row justify-center>
        <v-flex xs6 sm4 md3
          v-for="(theme) in themes"
          v-on:click="setCurrentTheme(theme)"
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
.maxWid700{
  max-width: 700px;
}
</style>

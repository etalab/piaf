<template>
  <v-flex xs12 my-0 justify-center>
    <v-row class="maxWid700 mx-auto">
      <v-col
        cols='1'
        class="px-0"
      >
      <v-row justify="center">
        <v-dialog
          v-model="dialog"
          width="500"
        >
          <template v-slot:activator="{ on }">
            <v-btn class="mx-0 minwidth" fab dark x-small color="primary" outlined v-on="on">
              <v-icon dark>mdi-home</v-icon>
            </v-btn>
          </template>

          <v-card>
            <v-btn class="close pa-0" color="grey darken-1" text @click="dialog = false"><v-icon dark>mdi-close</v-icon></v-btn>
            <v-card-title class="headline">Quitter ce texte ?</v-card-title>
            <v-card-text>Les questions-réponses que vous avez proposées sur ce texte ne seront pas sauvegardées. Vous pourrez alors choisir une nouvelle catégorie d'articles à annoter.</v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <router-link to="/">
                <v-btn color="red darken-1" text @click="dialog = false" class="text-capitalize"><v-icon dark>mdi-close</v-icon>Quitter</v-btn>
              </router-link>
              <v-btn color="green darken-1" text @click="dialog = false" class="text-capitalize"><v-icon dark>mdi-check</v-icon>Continuer</v-btn>
            </v-card-actions>
          </v-card>

        </v-dialog>
      </v-row>

      </v-col>
      <v-col cols='11' class="pr-0 alignSelf" style="display: flex; align-items: center; justify-content: center;">
        <v-progress-linear
          v-bind:value="stepPercentage"
          color="#11174d"
          background-color="#1b4799"
          height="25"
          rounded
          v-bind:style="{ borderRadius: 30 + 'px' }"
        >
          <template v-slot="{ value }">
            <span class="white--text" style="display: flex; align-items: center;">
              Question {{ Math.ceil(value / 20 ) }} / 5
              <v-menu offset-y>
                <template v-slot:activator="{ on }">
                  <v-btn
                    color="white"
                    dark
                    fab
                    x-small
                    v-on="on"
                    text

                  >
                     <v-icon dark>mdi-arrow-down-drop-circle</v-icon>
                  </v-btn>

                </template>
                <v-list>
                  <v-list-item v-for="(annotation, index) in $store.state.annotations" :key="index">
                    <v-list-item-title v-if="typeof annotation.question.text === 'string'">{{ annotation.question.text }}</v-list-item-title>
                    <v-list-item-title v-else>pas encore fait</v-list-item-title>
                  </v-list-item>
                </v-list>
              </v-menu>
            </span>
          </template>
        </v-progress-linear>
      </v-col>
    </v-row>
  </v-flex>

</template>

<script>
import { mapState } from 'vuex'

export default {
  computed: {
    ...mapState([
      'currentQuestionIndex',
    ]),
    stepPercentage(){
      return this.$store.getters.currentProgress * 20
    },
  },
  data () {
    return {
      dialog: false,
    }
  },
};
</script>

<style scoped>
/* for all */
.minwidth{
  min-width: 32px;
}
.close{
  position: absolute;
  height: 50px;
  right: -10px;
  top: 5px;
}
.router-link-active{
  text-decoration: none;
}
</style>

<template>
  <v-flex xs12 my-0 justify-center>
    <v-row class="maxWid700 mx-auto">
      <v-col
        cols='1'
        class="px-0"
      >
      <v-dialog v-model="dialog" persistent max-width="290">
        <template v-slot:activator="{ on }">
          <v-btn class="mx-0 minwidth" fab dark x-small color="primary" outlined v-on="on">
            <v-icon dark>mdi-close</v-icon>
          </v-btn>
        </template>

        <v-card>
          <v-card-title class="headline">Revenir à l'accueil ?</v-card-title>
          <v-card-text>Si vous n'avez pas encore fini d'annoter votre paragrahe, vous allez perdre les questions-réponses non sauvegardées. Pour revenir à la page d'accueil et perdre les annotations non enregistrées, cliquez sur <v-icon small dark color="green">mdi-check</v-icon> </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="green darken-1" text @click="dialog = false" href="https://piaf.etalab.studio"><v-icon dark>mdi-check</v-icon></v-btn>
            <v-btn color="red darken-1" text @click="dialog = false"><v-icon dark>mdi-close</v-icon></v-btn>
          </v-card-actions>
        </v-card>

      </v-dialog>

      </v-col>
      <v-col cols='11' class="pr-0 alignSelf">
        instruction
      </v-col>
    </v-row>
  </v-flex>

</template>

<script>
import { mapState } from 'vuex'

export default {
  computed: {
    ...mapState([
      'currentQuestionIndex'
    ]),
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
.maxWid700{
  max-width: 700px;
}
.alignSelf{
  align-self: center;
}
.minwidth{
  min-width: 32px;
}
</style>

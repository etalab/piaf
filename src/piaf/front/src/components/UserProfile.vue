<template>
  <v-dialog v-model="dialog" persistent max-width="290">
    <template v-slot:activator="{ on }">
      <v-btn class="mx-0 minwidth" fab dark x-small outlined v-on="on">
        <v-avatar color="blue" size=30>
          <v-icon dark>mdi-account</v-icon>
          <v-icon x-small dark v-if="userDetails.is_certified">mdi-medal</v-icon>
        </v-avatar>
      </v-btn>
    </template>
    <v-card>
      <v-card-title class="headline">
        <v-avatar
          slot="offset"
          class="mx-auto d-block"
          size="50"
        >
          <img
            src="https://i.ibb.co/fMQjbXc/logo.png"
          >
        </v-avatar>
      </v-card-title>
      <v-card-text>
        <p>Hello {{userDetails.username}},</p>
        <br>
        <p v-if="userDetails.is_certified">Vous êtes contributeur certifié <v-icon x-small dark>mdi-medal</v-icon></p>
        <p v-else>Vous êtes contributeur officiel de Piaf</p>
        <p>Merci pour vos contributions! On peut dire que vous êtes en train d'Édith Piaf :)</p>
        <br>
        <p>Rappel de votre email: {{ userDetails.email }}</p>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="grey darken-1" text @click="dialog = false"><v-icon dark>mdi-close</v-icon></v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import { mapState } from 'vuex'

export default {
  computed: {
    ...mapState([
      'userDetails'
    ]),
  },
  data () {
    return {
      dialog: false,
    }
  },
};
</script>

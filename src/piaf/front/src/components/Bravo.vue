<template>
  <v-layout class="mx-n2 pa-0" justify-center>
    <span>
      <p class="text-center"><v-icon large dark>mdi-check-outline</v-icon></p>
      <v-row
         align="center"
         no-gutters
       >
         <v-col cols="2">
         <v-avatar
           slot="offset"
           class="ml-auto d-block"
           size="50"
         >
           <img src="https://i.ibb.co/fMQjbXc/logo.png">
         </v-avatar>
        </v-col>
        <v-col cols="10">
          <v-chip
            :color="`white lighten-4`"
            class="ml-0 mb-10 pa-2"
            label
            large
          >
            <span v-if="userDetails.paragraphs_count" style="white-space:normal">
              Félicitation! Vous en êtes déjà à {{userDetails.paragraphs_count}} paragraphe<span v-if="userDetails.paragraphs_count > 1">s</span> sur cet article. Encore X paragraphe pour finir cet article!
            </span>
          </v-chip>
        </v-col>
      </v-row>

      <v-row
         v-if="userDetails.paragraphs_count"
         class="spacer"
         align="center"
         no-gutters
       >
         <v-col cols="2">
           <v-avatar
             slot="offset"
             class="ml-auto d-block"
             size="50"
           >
             <img src="https://i.ibb.co/fMQjbXc/logo.png">
           </v-avatar>
        </v-col>
        <v-col cols="10">
          <v-chip
            :color="`white lighten-4`"
            class="ml-0 mb-10 pa-2"
            label
            large
          >
            <span style="white-space:normal">Vous avez écrit {{userDetails.paragraphs_count * 5}} questions-réponses depuis le début
            </span>
          </v-chip>
        </v-col>
      </v-row>


      <v-row
         v-if="userDetails.paragraphs_count"
         class="spacer"
         align="center"
         no-gutters
       >
         <v-col cols="2">
           <v-avatar
             slot="offset"
             class="ml-auto d-block"
             size="50"
           >
             <img src="https://i.ibb.co/fMQjbXc/logo.png">
           </v-avatar>
        </v-col>
        <v-col cols="10">
          <v-chip
            :color="`white lighten-4`"
            class="ml-0 mb-10 pa-2"
            label
            large
          >
            <span style="white-space:normal">Le prochain paragraphe n'attend plus que vous!!!
            </span>
          </v-chip>
        </v-col>
      </v-row>

    </span>
    <Fireworks :boxHeight="'100%'" :boxWidth="'100%'"/>
  </v-layout>
</template>

<script>
import Fireworks from './Fireworks.vue'
import { mapState } from 'vuex'

export default {
  computed: {
    ...mapState([
      'userDetails',
    ]),
  },
  components: { Fireworks },
  methods: {
    goToAnnotation() {
      this.$store.dispatch('switchBetweenAnnotationAndBravo',false)
    },
  },
};
</script>

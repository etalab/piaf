<template>
  <v-app>
  <!--  Is always placed at the top of an application with a lower priority than v-system-bar -->
  <v-app-bar app hide-on-scroll>
    <v-flex xs12 my-0 justify-center>
      <v-row class="maxWid700 mx-auto">
        <v-col cols='11' class="pr-0 alignSelf">
          <v-progress-linear
            v-bind:value="100"
            color="#11174d"
            background-color="#1b4799"
            height="25"
            rounded
            v-bind:style="{ borderRadius: 30 + 'px' }"
          >
            <template>
              <span class="white--text">Questions-réponses enregistrées !</span>
            </template>
          </v-progress-linear>
        </v-col>
      </v-row>
    </v-flex>
  </v-app-bar>

  <!-- Sizes your content based upon application components -->
  <v-content>
    <!-- Provides the application the proper gutter -->
    <v-container fluid>
      <PiafBubble :hasFireworks=true>
        Félicitations ! Vous avez écrit <strong>{{userDetails.paragraphs_count * 5}} questions-réponses</strong> depuis votre inscription. Merci beaucoup !
        <br><br>
        Le prochain paragraphe n'attend plus que vous !!!
      </PiafBubble>
    </v-container>
    <!-- we need to put the Animation after the other components for the background to be beneath -->
    <Animation/>
  </v-content>

  <v-footer
  style="z-index:10"
  padless
  fixed
  min-height='150px'
  color='white'>
    <v-flex xs12 my-0 justify-center class="container">
      <v-row class="maxWid700 mx-auto">
        <v-col cols='12' class="px-0 textContainer">
          <v-btn
          dark
          small
          color="primary"
          v-if="!loading"
          v-on:click="goToTheme">
            Changer de thème
          </v-btn>

          <v-btn
          small
          color="primary"
          dark
          v-on:click="goToAnnotation"
          class="alignSelf"
          >Continuer
          </v-btn>
        </v-col>
      </v-row>
    </v-flex>
  </v-footer>
</v-app>
</template>

<script>
import Navbar from '../components/Navbar';
import Animation from '../components/Animation.vue';
import PiafBubble from '../components/PiafBubble.vue';
import { mapState } from 'vuex'

export default {
  name: 'App',
  components: {
    Navbar,
    Animation,
    PiafBubble,
  },
  computed: {
    ...mapState([
      'userDetails',
    ]),
  },
  methods: {
    goToAnnotation() {
      return this.$router.push('/annotation/'+this.$route.params.level)
    },
    goToTheme() {
      return this.$router.push('/annotation/'+this.$route.params.level+'/theme/')
    },
  },
  mounted () {
      this.$store.dispatch('getUserDetails')
  },
};
</script>

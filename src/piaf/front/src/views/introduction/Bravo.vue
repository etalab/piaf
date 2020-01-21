<template>
  <v-app>
  <!--  Is always placed at the top of an application with a lower priority than v-system-bar -->
  <v-app-bar app hide-on-scroll>
    <NavbarProfile :NavbarTitle="`Niveau déverouillé`"/>
  </v-app-bar>

  <!-- Sizes your content based upon application components -->
  <v-content>
    <!-- Provides the application the proper gutter -->
    <v-container fluid>
      <PiafBubble :hasFireworks=true>
        Félicitations ! Vous êtes maintenant <strong>expert du niveau {{$route.params.level}}</strong> !
        <br><br>
        <span v-if="$route.params.level == 3">Vous avez réalisé vos premières questions-réponses !!!</span>
        <span v-else>Vous pouvez passer au niveau supérieur !!!<!-- Vous pouvez continuer sur ce niveau, ou en essayer un nouveau !!! --></span>
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
        <v-col cols='12' class="pr-0 textContainer">
          <v-btn
          small
          color="primary"
          dark
          v-on:click="onClick"
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
import NavbarProfile from '../../components/NavbarProfile';
import Animation from '../../components/Animation.vue';
import PiafBubble from '../../components/PiafBubble.vue';

export default {
  name: 'App',
  components: {
    NavbarProfile,
    Animation,
    PiafBubble,
  },
  methods: {
    onClick() {
      this.$router.push('/')
    }
  },
  mounted () {
      this.$store.dispatch('getUserDetails')
  },
};
</script>

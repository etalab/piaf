<template>
  <v-app>
  <!--  Is always placed at the top of an application with a lower priority than v-system-bar -->
  <v-app-bar app hide-on-scroll>
    <NavbarProfile :NavbarTitle="NavbarTitle"/>
  </v-app-bar>

  <!-- Sizes your content based upon application components -->
  <v-content>
    <!-- Provides the application the proper gutter -->
    <v-container fluid>
      <Consignes1 v-bind:step="step" v-if="$route.params.level == 1"/>
      <Consignes2 v-bind:step="step" v-if="$route.params.level == 2"/>
      <Consignes3 v-bind:step="step" v-if="$route.params.level == 3"/>
    </v-container>
    <!-- we need to put the Animation after the other components for the background to be beneath -->
    <Animation/>
  </v-content>
  <v-footer
  style="z-index:10"
  padless
  fixed
  min-height='150px'
  color='white'
  v-if="showFooter">
    <div style="min-height: 4px;min-width:100%;position:absolute;top:0px;">
      <v-progress-linear
      :value="step / lastStep * 100"
      color="blue lighten-2"
      height=8
      ></v-progress-linear>
    </div>
    <v-flex xs12 my-0 justify-center class="container">
      <v-row class="maxWid700 mx-auto">
        <v-col cols='12' class="pr-0 textContainer">
          <v-btn
          class="mx-2"
          fab
          dark
          small
          outlined
          color="secondary"
          v-if="step > 0"
          v-on:click="step--">
            <v-icon dark>mdi-arrow-left</v-icon>
          </v-btn>

          <v-btn
          class="mx-2"
          dark
          small
          color="primary"
          v-if="step != lastStep"
          @click="step++">
            Continuer
          </v-btn>

          <v-btn
          class="mx-2"
          dark
          small
          color="primary"
          v-if="step == lastStep"
          :to="toNiveau"
          >
            Continuer
          </v-btn>
        </v-col>
      </v-row>
    </v-flex>
  </v-footer>
</v-app>
</template>

<script>
import Consignes1 from '../../components/introduction/Consignes1';
import Consignes2 from '../../components/introduction/Consignes2';
import Consignes3 from '../../components/introduction/Consignes3';
import NavbarProfile from '../../components/NavbarProfile';
import Animation from '../../components/Animation.vue';

export default {
  data: () => ({
    step: 0,
    // lastStep : 5,
  }),
  name: 'App',
  components: {
    Consignes1,
    Consignes2,
    Consignes3,
    NavbarProfile,
    Animation,
  },
  computed:{
    NavbarTitle () {
      return 'Niveau ' + this.$route.params.level
    },
    lastStep () {
      if (Number(this.$route.params.level) === 1) {
        return 7
      } else if (Number(this.$route.params.level) === 2) {
        return 7
      } else if (Number(this.$route.params.level) === 3) {
        return 3
      } else {
        return 1
      }
    },
    toNiveau(){
      return "/introduction/"+Number(this.$route.params.level)+"/play"
    },
    showFooter(){
      return (Number(this.$route.params.level) === 3 && Number(this.step) === 3 ) ? false : true
    }
  }
};
</script>

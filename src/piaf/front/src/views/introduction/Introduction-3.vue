<template>
  <v-app>
  <!--  Is always placed at the top of an application with a lower priority than v-system-bar -->
  <v-app-bar app hide-on-scroll>
    <NavbarProfile/>
  </v-app-bar>

  <!-- Sizes your content based upon application components -->
  <v-content>
    <!-- Provides the application the proper gutter -->
    <v-container fluid>
      <Consignes1 v-bind:step="step"/>
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
          @click="step++">
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
import NavbarProfile from '../../components/NavbarProfile';
import Animation from '../../components/Animation.vue';

export default {
  data: () => ({
    step: 0,
  }),
  name: 'App',
  components: {
    Consignes1,
    NavbarProfile,
    Animation,
  },
};
</script>
<style scoped>
.maxWid700{
  max-width: 700px;
}
.textContainer{
  display: flex;
  justify-content: space-around;
}
</style>

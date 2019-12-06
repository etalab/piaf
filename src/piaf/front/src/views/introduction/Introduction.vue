<template>
  <v-app>
  <!--  Is always placed at the top of an application with a lower priority than v-system-bar -->
  <v-app-bar app hide-on-scroll>
    <NavbarProfile :NavbarTitle="`Débuter sur Piaf`"/>
  </v-app-bar>

  <!-- Sizes your content based upon application components -->
  <v-content>
    <!-- Provides the application the proper gutter -->
    <v-container fluid>
      <v-container class="maxWid700 center" v-if="showFirstTime">
      <span class="font-weight-thin mb-5 white--text zind0 title">C'est la première fois que l'on vous voit sur Piaf!</span>
     <br>
     <v-btn
       class="mx-2 mt-5"
       dark
       small
       color="primary"
       @click="showFirstTime = !showFirstTime">
         Continuer
     </v-btn>

      </v-container>
      <Level v-else/>
    </v-container>
    <!-- we need to put the Animation after the other components for the background to be beneath -->
    <Animation/>
  </v-content>
</v-app>
</template>

<script>
import Level from '../../components/introduction/Level';
import NavbarProfile from '../../components/NavbarProfile';
import Animation from '../../components/Animation.vue';

export default {
  data: () => ({
    showFirstTime: true,
  }),
  name: 'App',
  components: {
    Level,
    NavbarProfile,
    Animation,
  },
};
</script>
<style scoped>
.center{
  text-align: center;
}
</style>

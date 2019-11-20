<template>
  <v-app>
  <!-- Sizes your content based upon application components -->
  <v-content>
    <!-- Provides the application the proper gutter -->
    <v-container fluid class="text-center white--text pt-10">
      <h1>Oups... Cette page n'existe pas!</h1>
      <router-link to="/" class="white--text">Retour</router-link>
    </v-container>
    <!-- we need to put the Animation after the other components for the background to be beneath -->
    <Animation/>
  </v-content>
</v-app>
</template>

<script>
import Animation from '../components/Animation.vue';

export default {
  components: {
    Animation,
  },
};
</script>

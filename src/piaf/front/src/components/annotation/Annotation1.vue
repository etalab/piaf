<template>
  <v-app>
  <!--  Is always placed at the top of an application with a lower priority than v-system-bar -->
  <v-app-bar app hide-on-scroll>
    <Navbar/>
  </v-app-bar>

  <!-- Sizes your content based upon application components -->
  <v-content>
    <!-- Provides the application the proper gutter -->
    <v-container fluid center>
      <span class="white">Nothing yet</span>
    </v-container>
    <!-- we need to put the Animation after the other components for the background to be beneath -->
    <Animation/>
  </v-content>

</v-app>
</template>

<script>

import Navbar from '../Navbar';
import Animation from '../Animation.vue';

import { mapState } from 'vuex'

export default {
  name: 'App',
  components: {
    Navbar,
    Animation,
  },
  computed: mapState([
    'currentDocument',
  ]),
};
</script>

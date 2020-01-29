<template>
  <v-app>
  <!--  Is always placed at the top of an application with a lower priority than v-system-bar -->
  <v-app-bar app hide-on-scroll>
    <Navbar/>
  </v-app-bar>

  <!-- Sizes your content based upon application components -->
  <v-content>
    <!-- Provides the application the proper gutter -->
    <v-container fluid>
      <AnnotationTask v-if="currentDocument" style="margin-bottom:150px;"/>
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
    <Footer :routeAfterValidation="`/annotation/`+$route.params.level+`/bravo`"/>
  </v-footer>
</v-app>
</template>

<script>

import Footer from '../../components/Footer';
import AnnotationTask from './AnnotationTask';
import Navbar from '../../components/Navbar';
import Animation from '../../components/Animation.vue';

import { mapState } from 'vuex'

export default {
  name: 'App',
  components: {
    AnnotationTask,
    Navbar,
    Footer,
    Animation,
  },
  computed: mapState([
    'currentDocument',
  ]),
  mounted () {
      this.$store.dispatch('getUserDetails')
      this.$store.dispatch('loadNewText')
      this.$store.dispatch('resetDefaultStore')
  },
};
</script>

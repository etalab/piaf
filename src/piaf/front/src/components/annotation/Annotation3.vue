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
  color='white'>{{restoreTrigger}}
    <Footer :routeAfterValidation="routeAfterValidation" v-on:validation="onValidation" :key="restoreTrigger"/>
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
  data(){
    return {
      restoreTrigger:0
    }
  },
  components: {
    AnnotationTask,
    Navbar,
    Footer,
    Animation,
  },
  computed: {
    ...mapState([
      'currentDocument',
    ]),
    routeAfterValidation () {
      const urlEnd = (process.env.VUE_APP_PRINT_BRAVO === 'true') ? '/bravo' : '#' + new Date().getTime()
      return '/annotation/' + this.$route.params.level + urlEnd
    },
  },
  methods: {
    onValidation(){
      if (process.env.VUE_APP_PRINT_BRAVO === 'false') {
        this.$store.dispatch('loadNewText')
        this.$store.dispatch('resetDefaultStore')
        this.restoreTrigger = this.restoreTrigger++
      }
    },
  },
  mounted () {
      this.$store.dispatch('getUserDetails')
      this.$store.dispatch('loadNewText')
      this.$store.dispatch('resetDefaultStore')
  },
};
</script>

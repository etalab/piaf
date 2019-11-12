<template>
  <v-app>
  <!-- Can be placed on the left or right side of an application and can be configured to sit next to or below v-app-bar -->
  <!-- <v-navigation-drawer app>
  </v-navigation-drawer> -->

  <!--  Is always placed at the top of an application with a lower priority than v-system-bar -->
  <v-app-bar app hide-on-scroll>
    <Navbar
    v-if="showNavbar"
    />
    <NavbarProfile
    v-else />
  </v-app-bar>

  <!-- Sizes your content based upon application components -->
  <v-content>
    <!-- Provides the application the proper gutter -->
    <v-container fluid>
      <Theme v-if="showTheme"/>
      <AnnotationTask v-if="showAnnotationTask && currentDocument" style="margin-bottom:150px;"/>
      <Bravo v-if="showBravo" style="margin-bottom:150px;"/>
    </v-container>
    <!-- we need to put the Animation after the other components for the background to be beneath -->
    <Animation v-if="showTheme || showAnnotationTask || showBravo"/>
  </v-content>

  <v-footer
  style="z-index:10"
  v-if="!showTheme"
  padless
  fixed
  min-height='150px'
  color='white'>
    <Footer/>
  </v-footer>
</v-app>
</template>

<script>
import Theme from './components/Theme';
import Footer from './components/Footer';
import AnnotationTask from './components/AnnotationTask';
import Navbar from './components/Navbar';
import NavbarProfile from './components/NavbarProfile';
import Animation from './components/Animation.vue';
import Bravo from './components/Bravo.vue';
import { mapState } from 'vuex'

export default {
  name: 'App',
  components: {
    Theme,
    AnnotationTask,
    Navbar,
    NavbarProfile,
    Footer,
    Animation,
    Bravo,
  },
  computed: mapState([
    // attacher `this.currentTheme` à `store.state.currentTheme`
    'currentTheme',
    'showTheme',
    'showFooter',
    'showNavbar',
    'showAnnotationTask',
    'showBravo',
    'currentDocument',
  ]),
  mounted () {
      this.$store.dispatch('getUserDetails')
  },
};
</script>

<style>
.v-application {
   background-color: transparent !important;
   font-family: "cooperhewitt light" !important;
    .title {
       font-family: "cooperhewitt medium" !important;
    }
}
html, .v-application {
  font-size: 14px;
}
@media (min-width:700px) {
  html, .v-application {
    font-size: 18px;
  }
}
strong{
  font-family: "cooperhewitt medium" !important;
}
.bold{
  font-family: "cooperhewitt medium" !important;
}
.v-tooltip__content{
  background-color: #616161 !important;
  opacity: 1 !important;
}
</style>

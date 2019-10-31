<template>
  <v-app>
  <!-- Can be placed on the left or right side of an application and can be configured to sit next to or below v-app-bar -->
  <!-- <v-navigation-drawer app>
  </v-navigation-drawer> -->

  <!--  Is always placed at the top of an application with a lower priority than v-system-bar -->
  <v-app-bar app>
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
      <AnnotationTask v-if="showAnnotationTask && currentDocument"/>
    </v-container>
  </v-content>

  <v-footer
  v-if="showFooter"
  padless
  fixed
  min-height='150px'
  color='#8bcbff'>
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
import { mapState } from 'vuex'

export default {
  name: 'App',
  components: {
    Theme,
    AnnotationTask,
    Navbar,
    NavbarProfile,
    Footer,
  },
  computed: mapState([
    // attacher `this.currentTheme` à `store.state.currentTheme`
    'currentTheme',
    'showTheme',
    'showFooter',
    'showNavbar',
    'showAnnotationTask',
    'currentDocument',
  ]),
  mounted () {
      this.$store.dispatch('getUserDetails')
  },
};
</script>

<style>
.v-application {
   font-family: "cooperhewitt light" !important;
    .title {
       font-family: "cooperhewitt medium" !important;
    }
}
strong{
  font-family: "cooperhewitt medium" !important;
}
.bold{
  font-family: "cooperhewitt medium" !important;
}
</style>

<template>
  <v-app>
  <!-- Can be placed on the left or right side of an application and can be configured to sit next to or below v-app-bar -->
  <v-navigation-drawer app>
  </v-navigation-drawer>

  <!--  Is always placed at the top of an application with a lower priority than v-system-bar -->
  <v-app-bar app>
    <Navbar />
  </v-app-bar>

  <!-- Sizes your content based upon application components -->
  <v-content>
    <!-- Provides the application the proper gutter -->
    <v-container fluid>
      <Theme v-if="showTheme"/>
      <AnnotationTask v-if="showAnnotationTask && currentDocument"/>
    </v-container>
  </v-content>
</v-app>
</template>

<script>
import Theme from './components/Theme';
import AnnotationTask from './components/AnnotationTask';
import Navbar from './components/Navbar';
import { mapState } from 'vuex'

export default {
  name: 'App',
  components: {
    Theme,
    AnnotationTask,
    Navbar,
  },
  computed: mapState([
    // attacher `this.currentTheme` à `store.state.currentTheme`
    'currentTheme',
    'showTheme',
    'showAnnotationTask',
    'currentDocument',
  ]),
  data: () => ({
  }),
};
</script>

<style>
.v-application {
   font-family: "cooperhewitt light" !important;
    .title {
       font-family: "cooperhewitt medium" !important;
    }
}
</style>

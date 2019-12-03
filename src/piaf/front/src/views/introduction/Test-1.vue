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
      <Test1content
        v-bind:question="currentTest.question"
        v-bind:text="currentTest.text"
        :key="currentTest.id"
      />
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
          <span>Cette question ({{step + 1}}/{{lastStep}}) est-elle valide ?</span>
        </v-col>
      </v-row>
      <v-row class="maxWid700 mx-auto">
        <v-col cols='12' class="pr-0 textContainer">

          <v-btn
          class="mx-2"
          fab
          dark
          small
          outlined
          color="error"
          v-on:click="onClick(false)">
            <v-icon dark>mdi-close</v-icon>
          </v-btn>

          <v-btn
          class="mx-2"
          fab
          dark
          small
          outlined
          color="success"
          v-on:click="onClick(true)">
            <v-icon dark>mdi-check</v-icon>
          </v-btn>
        </v-col>
      </v-row>
    </v-flex>
  </v-footer>
</v-app>
</template>

<script>
import Test1content from '../../components/introduction/Test1content';
import NavbarProfile from '../../components/NavbarProfile';
import Animation from '../../components/Animation.vue';

export default {
  data: () => ({
    step: 0,
    lastStep : 5,
    tests: [
      {
        id : 0,
        question : "Quel est le titre du Tintin numéro un ?",
        text : "Dès le premier album, Tintin au pays des Soviets, Tintin est un reporter travaillant pour Le Petit Vingtième, le journal publiant ses aventures."
      },
      {
        id : 1,
        question : "Quel est le métier de Tintin ?",
        text : "Dès le premier album, Tintin au pays des Soviets, Tintin est un reporter travaillant pour Le Petit Vingtième, le journal publiant ses aventures."
      }
    ]
  }),
  components: {
    Test1content,
    NavbarProfile,
    Animation,
  },
  computed: {
    currentTest() {
      const findIdFunction = (obj) => obj.id == this.step;
      let index = this.tests.findIndex(findIdFunction);
      return this.tests[index]
    },
  },
  methods: {
    onClick(){
      console.log('to be changed with the async call for recording the results');
    },
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

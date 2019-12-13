<template>
  <v-app>
  <v-app-bar app hide-on-scroll>
    <NavbarProfile :NavbarTitle="NavbarTitle"/>
  </v-app-bar>
  <v-content>
    <v-container fluid>
        <v-layout
          text-center
          wrap
        >
          <v-flex xs12 my-5>
            <div>
              <div v-if="currentDocument && annotations">
                <v-card
                  max-width="700"
                  class="mx-auto"
                >
                  <TextInteractive
                    v-bind:text="currentDocument.text"
                    v-bind:currentQuestionIndex="currentQuestionIndex"
                    ref="annotator"
                   />

                 </v-card>
               </div>
             </div>
           </v-flex>
         </v-layout>
    </v-container>
    <Animation/>
  </v-content>
  <v-footer
  style="z-index:10"
  padless
  fixed
  min-height='150px'
  color='white'>
    <Footer
      v-on:validation="level3completed"
      :routeAfterValidation="`/introduction/`+$route.params.level+`/bravo`"/>
  </v-footer>
  </v-app>
</template>

<script>
import TextInteractive from '../TextInteractive';
import Footer from '../Footer';
import Animation from '../Animation.vue';
import NavbarProfile from '../../components/NavbarProfile';
import {playMixin} from './mixin.js';
import { mapState } from 'vuex'

export default {
  mixins: [playMixin],
  components: {
    TextInteractive,
    Footer,
    Animation,
    NavbarProfile,
  },
  computed:{
    ...mapState([
      'currentDocument',
      'currentQuestionIndex',
      'annotations',
    ]),
    NavbarTitle () {
      return 'Niveau ' + this.$route.params.level
    },
  },
  methods:{
    level3completed(){
      this.sendScore(100,3)
    }
  }
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

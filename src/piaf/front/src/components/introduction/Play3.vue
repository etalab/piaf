<template>
  <v-app>
  <v-app-bar app hide-on-scroll>
    <Navbar/>
  </v-app-bar>
  <v-content>
    <v-container fluid>
        <v-layout
          text-center
          wrap
          style="margin-bottom:150px;"
        >
           <v-flex xs12 my-5>
             <div>
               <div v-if="currentDocument && annotations">
                 <v-card
                   max-width="700"
                   class="mx-auto"
                 >
                   <v-card-text style="font-size:1em;line-height:1.7;">
                     <TextTitle/>
                     <br>
                     <v-alert
                       dense
                       outlined
                       type="error"
                       v-show="showErrorMessage"
                     >
                       La réponse est <strong>trop longue</strong>, elle doit faire moins de 200 caractères
                     </v-alert>
                     <TextInteractive
                       v-bind:text="currentDocument.text"
                       v-bind:currentQuestionIndex="currentQuestionIndex"
                       ref="annotator"
                      />
                  </v-card-text>
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
import TextTitle from '../TextTitle';
import Footer from '../Footer';
import Animation from '../Animation.vue';
import Navbar from '../../components/Navbar';
import {playMixin} from './mixin.js';
import { mapState } from 'vuex'

export default {
  mixins: [playMixin],
  components: {
    TextInteractive,
    TextTitle,
    Footer,
    Animation,
    Navbar,
  },
  computed:{
    ...mapState([
      'currentDocument',
      'highlitedText',
      'currentQuestionIndex',
      'annotations',
    ]),
    NavbarTitle () {
      return 'Niveau ' + this.$route.params.level
    },
    showErrorMessage () {
      return typeof this.highlitedText === 'string' && this.highlitedText.length > 200
    },
  },
  methods:{
    level3completed(){
      this.sendScore(100,3)
    }
  }
};
</script>

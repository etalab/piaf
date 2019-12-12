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
    <Footer/>
  </v-footer>
  <!-- <v-footer
  style="z-index:10"
  padless
  fixed
  min-height='150px'
  color='white'>
    <v-flex xs12 my-0 justify-center class="container">
      <v-row class="maxWid700 mx-auto">
        <v-col cols='12' class="pr-0 textContainer">
          <span>Quelle est la bonne réponse ?</span>
        </v-col>
      </v-row>
      <v-row class="maxWid700 mx-auto">
        <v-col cols='12' class="pr-0 textContainer">
          <span class="first last mx-2 pa-2 aligned"
            v-for="(answer) in currentTest.answers"
            :key="answer"
            v-on:click="onClick(answer)">{{answer}}</span>
        </v-col>
      </v-row>
    </v-flex>
  </v-footer> -->
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
    toNiveau(){
      return "/introduction/"+Number(this.$route.params.level)+"/play"
    },
    NavbarTitle () {
      return 'Niveau ' + this.$route.params.level
    },
    // currentTest() {
    //   const findIdFunction = (obj) => obj.step == this.step;
    //   let index = this.tests.findIndex(findIdFunction);
    //   return this.tests[index]
    // },
    isLastStep() {
      return this.step + 1 === this.tests.length
    },
  },
  methods:{
    async onClick(answer){
      const findIdFunction = (obj) => obj.step == this.step;
      let index = this.tests.findIndex(findIdFunction);
      this.tests[index].answer = answer

      if (this.isLastStep) {
        let score = this.tests.reduce((acc,obj) => (obj.answer == obj.exp) ? acc+1 : acc,0)
        // eslint-disable-next-line
        console.log('do the async call',score);
        let scoreUpdate = await this.sendScore(score,1)
        // eslint-disable-next-line
        console.log(scoreUpdate,'now we can redirect to level');
        // this.$router.push('/introduction')
      } else {
        this.step++
      }
    },
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

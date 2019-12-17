<template>
  <v-app>
  <v-app-bar app hide-on-scroll>
    <NavbarProfile :NavbarTitle="NavbarTitle"/>
  </v-app-bar>
  <v-content>
    <v-container fluid>
      <v-container class="maxWid700">
        <Play1content
          v-bind:question="currentTest.question"
          v-bind:text="currentTest.text"
          :key="currentTest.step"
        />
      </v-container>
    </v-container>
    <Animation/>
  </v-content>
  <v-footer
  style="z-index:10"
  padless
  fixed
  min-height='150px'
  color='white'>
    <div style="min-height: 4px;min-width:100%;position:absolute;top:0px;">
      <v-progress-linear
      :value="(!networkIssueMessage) ? step / tests.length * 100 : 100"
      color="blue lighten-2"
      ></v-progress-linear>
    </div>
    <v-flex xs12 my-0 justify-center class="container">

      <PlayFooterTitle
      :title="`Quelle est la bonne réponse ?`"
      :networkIssueMessage="networkIssueMessage"/>

      <PlayFooterLoading
      :loading="loading"
      :networkIssueMessage="networkIssueMessage"
      v-on:resubmit="submitAnswers"/>

      <v-row class="maxWid700 mx-auto" v-if="!loading && !networkIssueMessage">
        <v-col cols='12' class="pr-0 textContainer">
          <span class="first last mx-2 pa-2 aligned"
            v-for="(answer) in currentTest.answers"
            :key="answer"
            v-on:click="onClick(answer)">{{answer}}</span>
        </v-col>
      </v-row>
    </v-flex>
  </v-footer>
  </v-app>
</template>

<script>
import Play1content from '../../components/introduction/Play1content';
import PlayFooterLoading from '../../components/introduction/PlayFooterLoading';
import PlayFooterTitle from '../../components/introduction/PlayFooterTitle';
import Animation from '../Animation.vue';
import NavbarProfile from '../../components/NavbarProfile';
import {playMixin} from './mixin.js';

export default {
  mixins: [playMixin],
  data: () => ({
    step: 0,
    tests: [
      {
        step : 1,
        exp : 'Tintin au pays des Soviets',
        question : "Quel est le premier album de Tintin ?",
        text : "Dès le premier album, Tintin au pays des Soviets, Tintin est un reporter travaillant pour Le Petit Vingtième, le journal publiant ses aventures.",
        answers:['Dès le premier album, Tintin au pays des Soviets','Tintin au pays des Soviets']
      },
      {
        step : 0,
        exp : 'Tintin',
        question : "Qui est journaliste pour le petit Vingtième ?",
        text : "Tintin est un reporter travaillant pour Le Petit Vingtième, le journal publiant ses aventures.",
        answers:['Tintin','Tintin est un reporter travaillant pour Le Petit Vingtième']
      }
    ]
  }),
  components: {
    Play1content,
    PlayFooterLoading,
    PlayFooterTitle,
    Animation,
    NavbarProfile,
  },
  computed:{
    toNiveau(){
      return "/introduction/"+Number(this.$route.params.level)+"/play"
    },
    NavbarTitle () {
      return 'Niveau ' + this.$route.params.level
    },
    currentTest() {
      const findIdFunction = (obj) => obj.step == this.step;
      let index = this.tests.findIndex(findIdFunction);
      return this.tests[index]
    },
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
        await this.submitAnswers()
      } else {
        this.step++
      }
    },
    async submitAnswers(){
      this.loading = true
      let score = this.tests.reduce((acc,obj) => (obj.answer == obj.exp) ? acc+1 : acc,0)
      score = 100 * score / this.tests.length
      let scoreUpdate = await this.sendScore(score,2)
      this.loading = false
      if (scoreUpdate) {
        this.$router.push('/introduction/'+this.$route.params.level+'/bravo')
      } else {
        this.networkIssueMessage = true
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
.aligned{
  display: flex;
  align-items: center;
  cursor: pointer;
}
span.first {
  color: #ffffff;
  background-color: #4169e1;
  border-top-left-radius: 4px;
  border-bottom-left-radius: 4px;
}
span.last {
  color: #ffffff;
  background-color: #4169e1;
  border-top-right-radius: 4px;
  border-bottom-right-radius: 4px;
}
span.selected {
  color: #ffffff;
  background-color: #4169e1;
}
</style>

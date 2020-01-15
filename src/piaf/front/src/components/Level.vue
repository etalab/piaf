<template>
  <span class="maxWid700 mx-auto">
    <v-container v-if="currentLevel == 1">
    <span class="font-weight-thin mb-5 white--text zind0 title">Bienvenue sur Piaf ! Vous allez constituer des couples de questions - réponses pour entrainer les intelligences artificelles en français</span>
    </v-container>

    <LevelBtn
    text='Niveau'
    :level='level.level'
    :active='level.level == currentLevel'
    :level_completed='userDetails.level_completed'
    :locked='level.level > currentLevel'
    :title='level.title'
    :levelClass="levelClassMethod(level)"
    :iconType="levelIconMethod(level)"
    v-for="(level) in levels" :key="level.level"
    />
  </span>
</template>

<script>
import LevelBtn from './LevelBtn.vue';
import { mapState } from 'vuex'

export default {
  components: {
    LevelBtn,
  },
  data: () => ({
     levels: [
       {
         color: 'green',
         level: 1,
         title: 'Questions',
         text: 'Comment poser une bonne question ?',
       },
       {
         color: 'pink',
         level: 2,
         title: 'Réponses',
         text: 'Comment trouver une bonne réponse ?',
       },
       {
         color: 'cyan',
         level: 3,
         title: 'Questions-Réponses',
         text: 'Votre première annotation réelle !',
       },
     ],
  }),
  methods: {
    levelClassMethod(level) {
      if (level.level > this.currentLevel) {
        return 'btngrey'
      } else if (level.level == this.currentLevel) {
        return 'btnyellow'
      } else if (level.level < this.currentLevel) {
        return 'btnorange'
      }else {
        return 'btngrey'
      }
    },
    levelIconMethod(level) {
      if (level.level > this.currentLevel) {
        return 'mdi-lock'
      } else if (level.level == this.currentLevel) {
        return 'mdi-lock-open'
      } else if (level.level < this.currentLevel) {
        return 'mdi-check'
      }else {
        return 'mdi-lock'
      }
    },
  },
  computed: {
    ...mapState([
      'userDetails',
    ]),
    currentLevel() {
      if(this.userDetails.level_completed === undefined)
        return 1
      return (Number(this.userDetails.level_completed) == 3) ? 3 : Number(this.userDetails.level_completed) + 1
    },
  },
  mounted () {
    this.$store.dispatch('getUserDetails')
  },
};
</script>

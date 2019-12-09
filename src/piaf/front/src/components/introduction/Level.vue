<template>
  <span class="maxWid700 mx-auto">
    <LevelBtn
    text='Niveau'
    :level='level.level'
    :active='level.level == currentLevel'
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

export default {
  components: {
    LevelBtn,
  },
  data: () => ({
     currentLevel: 1,
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
};
</script>
<style scoped>
.maxWid700{
  max-width: 700px;
}
</style>

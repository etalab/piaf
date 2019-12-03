<template>
  <v-stepper v-model="currentLevel" vertical class="maxWid700 mx-auto">
    <span v-for="(level) in levels" :key="level.level">
      <v-stepper-step
        :step="level.level"
        :complete="level.level < currentLevel"
        class="title">
        {{level.title}}
      </v-stepper-step>
      <v-stepper-content :step="level.level" class="mt-n5">
        <v-card color="white lighten-1" class="mb-3 noshadow">{{level.text}}</v-card>
        <v-btn color="primary" @click="onClick">Commencer</v-btn>
      </v-stepper-content>
    </span>
  </v-stepper>
</template>

<script>
export default {
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
    onClick(){
      this.$router.push('introduction-' + this.currentLevel)
    },
  },
};
</script>
<style scoped>
.noshadow{
  box-shadow: none;
}
.maxWid700{
  max-width: 700px;
}
</style>

<template>
  <span class="maxWid700 mx-auto">
    <!-- <span class="justify-center d-flex subtitle pa-2"> Il y a trois niveaux à passer avant d'être expert de Piaf
    </span>
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
    </span> -->

    <v-card
      class="mx-auto ma-5 rounded"
      max-width="130"
      max-height="130"
      raised
      v-for="(level) in levels" :key="level.level"
      @click="onClick(level)"
    >
      <v-list-item three-line class="pa-0"
      v-bind:class="{
        'bgdYellowDark': level.level > currentLevel,
        'bgdYellow': level.level == currentLevel,
        'bgdYellowDone': level.level < currentLevel }">
        <v-list-item-content class="pt-0">
          <v-list-item-avatar
            tile
            size="60"
            class="ma-0 rounded-top"
          >
            <v-icon x-large dark class="threeD" v-if="level.level < currentLevel">mdi-check</v-icon>
            <v-icon x-large dark class="threeD" v-if="level.level == currentLevel">mdi-lock-open</v-icon>
            <v-icon x-large dark class="threeD" v-if="level.level > currentLevel">mdi-lock</v-icon>
          </v-list-item-avatar>
          <v-list-item-title class="title mb-1 text-center white--text threeD bold">Niv {{level.level}}</v-list-item-title>
          <v-list-item-subtitle class="text-center grey--text">{{level.title}}</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

    </v-card>
  </span>
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
    onClick(level){
      if (level.level == this.currentLevel) {
        this.$router.push('introduction/' + this.currentLevel)
      }
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
.center{
  display: flex;
  justify-content: center;
  flex-direction: column;
}
.rounded{
  border-radius: 35px;
}
.rounded-top{
  border-radius: 15px 15px 0px 0px;
}
.bgdYellow{
  background-color: #fff032;
}
.bgdYellowDark{
  background-color: #9e9e9e;
}
.bgdYellowDone{
  background-color: #fffab4;
}

.threeD{
  text-shadow: 0.5px 0.5px 0 #989898, 0.5px -0.5px 0 #989898, -0.5px 0.5px 0 #989898, -0.5px -0.5px 0 #989898, 0.5px 0px 0 #989898, 0px 0.5px 0 #989898, -0.5px 0px 0 #989898, 0px -0.5px 0 #989898;
}
</style>

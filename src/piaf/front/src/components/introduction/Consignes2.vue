<template>
  <v-container class="maxWid700">
    <span v-if="step == 0">
      <v-layout justify-center>
        <span class="font-weight-thin mb-2 white--text zind0 title">La meilleure réponse</span>
      </v-layout>
      <v-card max-width="700" class="mx-auto">
        <v-card-text  class="pa-2 mt-5 consigneText">
          <span class="black--text bold">Le rire apparaît chez l'être humain <span class="first">aux </span> <span class="selected"> alentours du quatrième ou cinquième </span><span class="last">mois</span></span>
        </v-card-text>
      </v-card>
      <v-layout justify-center>
        <span class="ml-1 font-weight-thin mt-5 mb-4 white--text zind0 questionClass"> À quel âge l'homme commence t-il à rire ?</span>
      </v-layout>
      <v-layout justify-center>
        <span class="font-weight-thin mt-5 white--text zind0">Ce sera à vous d'évaluer si les mots surlignés sont une bonne réponse.</span>
      </v-layout>
    </span>
    <span v-if="[1,2,3,4].indexOf(step) !== -1">
      <v-layout justify-center>
        <span class="font-weight-thin white--text zind0 title">Qu'est ce qu'une bonne réponse?</span>
      </v-layout>
      <v-layout justify-center v-if="step == 1">
        <span class="font-weight-thin mt-10 mb-5 white--text zind0">C'est une réponse courte. Pas la peine de surgligner la phrase complète, quelques mots suffisent.</span>
      </v-layout>
      <v-card max-width="700" class="mx-auto" v-if="[2].indexOf(step) !== -1">
        <v-card-text  class="pa-2 mt-5 consigneText">
          <span class="black--text bold">Le rire <span class="first redBackground">apparaît chez l'être humain aux </span> <span class="selected redBackground"> alentours du quatrième ou cinquième </span><span class="last redBackground">mois</span></span>
        </v-card-text>
      </v-card>
      <v-card max-width="700" class="mx-auto" v-if="[3].indexOf(step) !== -1">
        <v-card-text  class="pa-2 mt-5 consigneText">
          <span class="black--text bold">Le rire apparaît chez l'être humain <span class="first">aux </span> <span class="selected"> alentours du quatrième ou cinquième </span><span class="last">mois</span></span>
        </v-card-text>
      </v-card>
      <v-card max-width="700" class="mx-auto" v-if="[4].indexOf(step) !== -1">
        <v-card-text  class="pa-2 mt-5 consigneText">
          <span class="black--text bold">Le rire apparaît chez l'être humain aux alentours du <span class="first">quatrième</span> <span class="selected"> ou cinquième </span><span class="last">mois</span></span>
        </v-card-text>
      </v-card>
      <v-layout justify-center v-if="[2,3,4].indexOf(step) !== -1">
        <span class="font-weight-thin mt-1 zind0 questionClass mt-3 white--text">À quel âge l'homme commence t-il à rire ?
        </span>
      </v-layout>
      <v-layout justify-center v-if="[2].indexOf(step) !== -1">
        <span class="font-weight-thin mt-10 white--text zind0">Ici, on a <strong>trop de mots</strong>, on pourrait faire plus court.
        </span>
      </v-layout>
      <v-layout justify-center v-if="[3].indexOf(step) !== -1">
        <span class="font-weight-thin mt-5 white--text zind0">C'est mieux : il n'y a plus trop de mots superflus.</span>
      </v-layout>
      <v-layout justify-center v-if="[4].indexOf(step) !== -1">
        <span class="font-weight-thin mt-5 white--text zind0">C'est encore mieux : il n'y a plus du tout de mots superflus.</span>
      </v-layout>
    </span>
    <span v-if="step == 5">
      <v-layout justify-center>
        <h1 class="font-weight-thin mb-5 white--text zind0 title">Le saviez-vous ?</h1>
      </v-layout>
      <v-layout justify-center>
        <span class="font-weight-thin mb-5 white--text zind0">La raison qui nous pousse à faire court est simple : nous souhaitons que l'IA nous apporte une réponse concise, et pas le paragraphe complet.</span>
      </v-layout>
    </span>
  </v-container>
</template>

<script>
export default {
  props: {
    step: Number
  },
};
</script>
<style scoped>
.maxWid700{
  max-width: 700px;
}
.redBackground{
  background-color: #e04141 !important;
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
.consigneText {
  font-size:1.2em;
  /* line-height:1.0; */
}
</style>

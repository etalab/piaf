<template>
  <v-container class="maxWid700">
    <span v-if="step == 0">
      <v-layout justify-center>
        <span class="font-weight-thin mb-5 white--text zind0 title">Niveau 2 : les réponses</span>
      </v-layout>
      <v-layout justify-center>
        <span class="font-weight-thin mb-5 white--text zind0">Voici quelques recommandations pour de bonnes réponses</span>
      </v-layout>
    </span>
    <span v-if="step == 1">
      <v-layout justify-center>
        <span class="font-weight-thin mb-5 white--text zind0 title">Dans le texte</span>
      </v-layout>
      <v-layout justify-center>
        <span class="font-weight-thin mb-5 white--text zind0">Il faut impérativement que la réponses soit dans le texte.</span>
      </v-layout>
      <v-layout justify-center>
        <span class="font-weight-thin mb-5 white--text zind0">Pour le moment, on n'entraîne notre IA à trouver des réponses. Décider si oui ou non il y a un réponse dans le texte ce sera pour plus tard !</span>
      </v-layout>
    </span>
    <span v-if="step == 2">
      <v-layout justify-center>
        <h1 class="font-weight-thin mb-5 white--text zind0 title">Faire court</h1>
      </v-layout>
      <v-layout justify-center>
        <span class="font-weight-thin mb-5 white--text zind0">Pas de blabla : on veut des réponses courtes.</span>
      </v-layout>
      <v-layout justify-center>
        <span class="font-weight-thin mb-5 white--text zind0">En effet, nous souhaitons que l'IA nous apporte une réponse concise, pas un roman à lire.</span>
      </v-layout>
    </span>
    <span v-if="step == 3">
      <v-layout justify-center>
        <h1 class="font-weight-thin mb-5 white--text zind0 title">Exemples</h1>
      </v-layout>
      <v-layout justify-center>
        <span class="font-weight-thin mb-5 white--text zind0">Pour illustrer, regardons ensemble une question-réponse. Nous verrons un exemple de bonne réponse, et un de mauvaise réponse</span>
      </v-layout>
    </span>
    <span v-if="step == 4 || step == 5 || step == 6">
      <v-card max-width="700" class="mx-auto">
        <v-card-text style="font-size:1em;line-height:1.7;">
          <span class="black--text bold" v-if="step == 4">Le rire apparaît chez l'être humain aux alentours du quatrième ou cinquième mois</span>
          <span class="black--text bold" v-if="step == 5">Le rire apparaît chez l'être humain <span class="first">aux </span> <span class="selected"> alentours du quatrième ou cinquième </span><span class="last">mois</span></span>
          <span class="black--text bold" v-if="step == 6"><span class="first redBackground">Le rire apparaît chez l'être humain aux </span> <span class="selected redBackground"> alentours du quatrième ou cinquième </span><span class="last redBackground">mois</span></span>
        </v-card-text>
      </v-card>
      <v-layout justify-center>
        <span class="font-weight-thin mb-5 white--text zind0 font-italic">A partir de quel âge un Homme peut-il rire ?</span>
      </v-layout>
      <v-layout justify-center v-if="step == 5">
        <span class="font-weight-thin mt-5 white--text zind0">La réponse surlignée en bleu dans le texte est une bonne réponse</span>
      </v-layout>
      <v-layout justify-center v-if="step == 6">
        <span class="font-weight-thin mt-5 white--text zind0">En revanche, cette réponse est trop longue
        </span>
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
</style>

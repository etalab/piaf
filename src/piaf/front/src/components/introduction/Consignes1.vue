<template>
  <v-container class="maxWid700">
    <span v-if="step == 0">
      <v-layout justify-center>
        <span class="font-weight-thin mb-5 white--text zind0 title">Niveau 1 : les questions</span>
      </v-layout>
      <v-layout justify-center>
        <span class="font-weight-thin mb-5 white--text zind0">Vous aller lire un texte comme :</span>
      </v-layout>
      <v-card max-width="700" class="mx-auto">
        <v-card-text style="font-size:1em;line-height:1.7;">
          <span class="black--text bold">Le rire apparaît chez l'être humain aux alentours du quatrième ou cinquième mois</span>
        </v-card-text>
      </v-card>
      <v-layout justify-center>
        <span class="font-weight-thin mb-5 white--text zind0">Vous verrez une question comme :</span>
      </v-layout>
      <v-layout justify-center v-if="step == 5">
        <span class="font-weight-thin mb-5 white--text zind0 font-italic">A partir de quel âge un Homme peut-il rire ?</span>
      </v-layout>
      <v-layout justify-center>
        <span class="font-weight-thin mb-5 white--text zind0">Voici quelques recommandations pour vous aider à poser de bonnes questions</span>
      </v-layout>
    </span>
    <span v-if="step == 1">
      <v-layout justify-center>
        <span class="font-weight-thin mb-5 white--text zind0 title">Reformuler</span>
      </v-layout>
      <v-layout justify-center>
        <span class="font-weight-thin mb-5 white--text zind0">On veut utiliser des mots différents du texte.</span>
      </v-layout>
      <v-layout justify-center>
        <span class="font-weight-thin mb-5 white--text zind0">Sinon, on se retrouvera avec une IA qui cherche bêtement les mots en communs entre une question et le texte. Alors que nous, nous voulons une IA qui comprenne une question et soit capable d'y répondre, peu importe si les termes exacts se trouvent dans le texte !</span>
      </v-layout>
    </span>
    <span v-if="step == 2">
      <v-layout justify-center>
        <h1 class="font-weight-thin mb-5 white--text zind0 title">Simple, mais pas trop</h1>
      </v-layout>
      <v-layout justify-center>
        <span class="font-weight-thin mb-5 white--text zind0">On veut des questions simples : on ne cherche pas à piéger les machines.</span>
      </v-layout>
      <v-layout justify-center>
        <span class="font-weight-thin mb-5 white--text zind0">Mais pas trop simple non plus : c'est un jeu pour les 5 ans et plus !</span>
      </v-layout>
    </span>
    <span v-if="step == 3">
      <v-layout justify-center>
        <h1 class="font-weight-thin mb-5 white--text zind0 title">Exemples</h1>
      </v-layout>
      <v-layout justify-center>
        <span class="font-weight-thin mb-5 white--text zind0">Pour illustrer, regardons ensemble deux textes. Pour chaque texte, nous vous montrerons un exemple de bonne question, et un de mauvaise question</span>
      </v-layout>
    </span>
    <span v-if="step == 4 || step == 5 || step == 6">
      <v-card max-width="700" class="mx-auto">
        <v-card-text style="font-size:1em;line-height:1.7;">
          <span class="black--text bold">Le rire apparaît chez l'être humain aux alentours du quatrième ou cinquième mois</span>
        </v-card-text>
      </v-card>
      <v-layout justify-center v-if="step == 5">
        <span class="font-weight-thin mt-5 white--text zind0">Ceci est une <b>bonne</b> question</span>
      </v-layout>
      <v-layout justify-center v-if="step == 5">
        <span class="font-weight-thin mb-5 green--text zind0 font-italic">A partir de quel âge un Homme peut-il rire ?</span>
      </v-layout>
      <v-layout justify-center v-if="step == 6">
        <span class="font-weight-thin mt-5 white--text zind0">En revanche, cette question contient trop de mots en commun avec le texte
        </span>
      </v-layout>
      <v-layout justify-center v-if="step == 6">
        <span class="font-weight-thin mb-5 zind0"><i class="red--text">A partir de quand le rire apparaît chez l'être humain ?</i>
        </span>
      </v-layout>
    </span>
    <span v-if="step == 7 || step == 8 || step == 9">
      <v-card max-width="700" class="mx-auto">
        <v-card-text style="font-size:1em;line-height:1.7;">
          <span class="black--text bold">Contrairement aux langues, rire ne s'apprend pas. C'est inné chez l'espèce humaine.</span>
        </v-card-text>
      </v-card>
      <v-layout justify-center v-if="step == 8">
        <span class="font-weight-thin mt-5 white--text zind0">Ceci est une <b>bonne</b> question</span>
      </v-layout>
      <v-layout justify-center v-if="step == 8">
        <span class="font-weight-thin mb-5 green--text zind0 font-italic">Un humain doit-il être formé pour rire ?</span>
      </v-layout>
      <v-layout justify-center v-if="step == 9">
        <span class="font-weight-thin mt-5 white--text zind0">En revanche, cette question n'a pas de réponse que l'on peut surligner dans le texte
        </span>
      </v-layout>
      <v-layout justify-center v-if="step == 9">
        <span class="font-weight-thin mb-5 zind0"><i class="red--text">Comment s'appelle l'étude du rire ?</i>
        </span>
      </v-layout>
    </span>
    <span v-if="step == 10">
      <v-layout justify-center>
        <h1 class="font-weight-thin mb-5 white--text zind0 title">Fautes d'orthographes</h1>
      </v-layout>
      <v-layout justify-center>
        <span class="font-weight-thin mb-5 white--text zind0">Ce n'est pas grave si l'on fait des fautes d'orthographes. Il vaut mieux éviter bien sûr, mais ce n'est pas grave. Plus on pose des questions proches de la réalité, mieux notre IA pourra nous comprendre !</span>
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

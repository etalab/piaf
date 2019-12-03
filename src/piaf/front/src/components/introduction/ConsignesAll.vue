<template>
  <v-container class="maxWid700">
    <span v-if="step == 0">
      <v-layout justify-center>
        <span class="font-weight-thin mb-5 white--text zind0">C'est la première fois que l'on vous voit sur Piaf! On est super content de vous compter parmi nous.</span>
      </v-layout>
      <v-layout justify-center>
        <span class="font-weight-thin mb-5 white--text zind0">Commençons par une minute où on vous montre comment faire</span>
      </v-layout>
    </span>
    <span v-if="step == 1">
      <v-layout justify-center>
        <h1 class="font-weight-thin mb-5 white--text zind0">3 règles pour les questions</h1>
      </v-layout>
      <v-layout justify-center>
        <span class="font-weight-thin mb-5 white--text zind0">Éviter les mots en commun avec le texte. Il vaut mieux utiliser des synonymes</span>
      </v-layout>
      <v-layout justify-center>
        <span class="font-weight-thin mb-5 white--text zind0">Faire simple : on cherche pas les questions pièges</span>
      </v-layout>
      <v-layout justify-center>
        <span class="font-weight-thin mb-5 white--text zind0">Mais pas trop simple : un enfant de 5 ans ne doit pas pouvoir y répondre</span>
      </v-layout>
    </span>
    <span v-if="step == 2">
      <v-layout justify-center>
        <h1 class="font-weight-thin mb-5 white--text zind0">2 règles pour les réponses</h1>
      </v-layout>
      <v-layout justify-center>
        <span class="font-weight-thin mb-5 white--text zind0">Courtes</span>
      </v-layout>
      <v-layout justify-center>
        <span class="font-weight-thin mb-5 white--text zind0">Présentes dans le texte</span>
      </v-layout>
    </span>
    <span v-if="step == 3">
      <v-layout justify-center>
        <h1 class="font-weight-thin mb-5 white--text zind0">Voilà, c'est fini pour les consignes</h1>
      </v-layout>
      <v-layout justify-center>
        <span class="font-weight-thin mb-5 white--text zind0">Vous comprendrez mieux avec quelques examples de bonnes questions-réponses.</span>
      </v-layout>
      <v-layout justify-center>
        <span class="font-weight-thin mb-5 white--text zind0">Une bonne question (en italique) <br>Une bonne réponse (en bleu dans le texte)</span>
      </v-layout>
    </span>
    <span v-if="step == 4 || step == 5">
      <v-layout justify-center>
        <span class="font-weight-thin mb-5 white--text zind0 font-italic">A partir de quel âge un Homme peut-il rire ?</span>
      </v-layout>
      <v-card max-width="700" class="mx-auto">
        <v-card-text style="font-size:1em;line-height:1.7;">
          <span class="black--text bold">Le rire apparaît chez l'être humain <span class="first">aux </span> <span class="selected">alentours du quatrième ou cinquième </span><span class="last">mois</span>
          </span>
        </v-card-text>
      </v-card>
      <v-layout justify-center v-if="step == 5">
        <span class="font-weight-thin mb-5 white--text zind0 mt-12">En revanche, la question suivante n'est pas valide: elle contient trop de mots en commun avec le texte (la réponse)
        </span>
      </v-layout>
      <v-layout justify-center v-if="step == 5">
        <span class="font-weight-thin mb-5 zind0"><i class="red--text">A partir de quand le rire apparaît chez l'être humain ?</i>
        </span>
      </v-layout>
    </span>
    <span v-if="step == 6">
      <v-layout justify-center>
        <span class="font-weight-thin mb-5 white--text zind0 font-italic">Un humain doit-il être formé pour rire ?</span>
      </v-layout>
      <v-card max-width="700" class="mx-auto">
        <v-card-text style="font-size:1em;line-height:1.7;">
          <span class="black--text bold">Contrairement aux langues, <span class="first">rire </span> <span class="selected">ne s'apprend </span><span class="last">pas</span>. C'est inné chez l'espèce humaine.
          </span>
        </v-card-text>
      </v-card>
    </span>
    <span v-if="step == 7">
      <v-layout justify-center>
        <h1 class="font-weight-thin mb-5 white--text zind0">À vous</h1>
      </v-layout>
      <v-layout justify-center>
        <span class="font-weight-thin mb-5 white--text zind0">Dans un premier temps, Piaf vous propose de dire si oui ou non ces questions-réponses sont valides, ça vous permettra de vous ajuster!</span>
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

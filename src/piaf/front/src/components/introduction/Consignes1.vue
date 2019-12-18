<template>
  <v-container class="maxWid700">
    <span v-if="[0,1].indexOf(step) !== -1">
      <v-layout justify-center>
        <span class="font-weight-thin mb-2 white--text ">Vous allez lire un texte comme :</span>
      </v-layout>
      <v-card max-width="700" class="mx-auto">
        <v-card-text class="pa-2 consigneText">
          <span class="black--text bold">Le rire apparaît chez l'être humain aux alentours du quatrième ou cinquième mois</span>
        </v-card-text>
      </v-card>
      <v-layout justify-center v-if="step == 1">
        <span class="font-weight-thin mt-5 mb-0 white--text ">Puis une question à propos de ce texte comme :</span>
      </v-layout>
      <v-layout justify-center v-if="step == 1">
        <span class="font-weight-thin mb-4 white--text  questionClass">À quel âge l'homme commence t-il à rire ?</span>
      </v-layout>
      <v-layout justify-center v-if="step == 1">
        <span class="font-weight-thin mt-5 white--text ">Ce sera à vous d'évaluer si la question est pertinente.</span>
      </v-layout>
    </span>
    <span v-if="[2].indexOf(step) !== -1">
      <v-layout justify-center>
        <span class="font-weight-thin white--text  title">Qu'est ce qu'une question pertinente&nbsp;?</span>
      </v-layout>
      <v-layout justify-center v-if="step == 2">
        <span class="font-weight-thin mt-10 mb-5 white--text ">C'est une question qui utilise des mots différents du texte. On reformule le plus possible avec nos propres mots.</span>
      </v-layout>
    </span>
    <span v-if="[3,4].indexOf(step) !== -1">
      <v-layout justify-center v-if="[3].indexOf(step) !== -1">
        <span class="font-weight-thin white--text  title">Voyons un example&nbsp;:</span>
      </v-layout>
      <v-card max-width="700" class="mx-auto mt-3" v-if="[3,4].indexOf(step) !== -1">
        <v-card-text class="pa-2 consigneText">
          <span class="black--text bold">Le rire apparaît chez l'être humain aux alentours du quatrième ou cinquième mois</span>
        </v-card-text>
      </v-card>
      <v-layout justify-center v-if="[3,4].indexOf(step) !== -1">
        <span class="font-weight-thin mt-5  questionClass red--text"><span class="white--text">Aux alentours de quand le rire apparaît-il chez l'être humain ?</span>
        </span>
      </v-layout>
      <v-layout justify-center v-if="[3,4].indexOf(step) !== -1">
        <span class="font-weight-thin mt-1 white--text "><v-icon dark small>mdi-arrow-right-bold</v-icon> Ici, on a trop de mots en commun avec le texte : il faut reformuler
        </span>
      </v-layout>
      <v-layout justify-center v-if="[4].indexOf(step) !== -1">
        <span class="font-weight-thin mt-5 white--text "><v-icon dark small>mdi-arrow-right-bold</v-icon> Voilà une bonne reformulation : </span>
      </v-layout>
      <v-layout justify-center v-if="[4].indexOf(step) !== -1">
        <span class="font-weight-thin green--text  questionClass"><span class="white--text">À quel âge un bébé commence t-il à rire ?</span></span>
      </v-layout>
    </span>
    <span v-if="step == 6">
      <v-layout justify-center>
        <h1 class="font-weight-thin mb-5 white--text  title">Le saviez-vous ?</h1>
      </v-layout>
      <v-layout justify-center>
        <span class="font-weight-thin mb-5 white--text ">Quelques <strong>fautes d'orthographes</strong> dans vos questions&nbsp;?<br><br>Il vaut mieux éviter bien sûr, mais pas d'inquiétude. Plus nos questions sont proches de ce que nous écrivons dans la vie de tous les jours, mieux notre IA pourra nous comprendre !</span>
      </v-layout>
    </span>
    <span v-if="step == 5">
      <v-layout justify-center>
        <h1 class="font-weight-thin mb-5 white--text  title">Le saviez-vous ?</h1>
      </v-layout>
      <v-layout justify-center>
        <span class="font-weight-thin mb-5 white--text ">Qu'est ce que reformuler apporte ? Nous voulons une IA qui comprenne une question et soit capable d'y répondre. Si on ne reformulait pas, notre IA chercherait bêtement les mots en commun entre une question et le texte.</span>
      </v-layout>
    </span>
    <span v-if="step == 7">
      <v-layout justify-center>
        <h1 class="font-weight-thin mb-5 white--text  title">À vous de jouer</h1>
      </v-layout>
      <v-layout justify-center>
        <span class="font-weight-thin mb-5 mt-5 white--text ">Vous allez nous dire si les questions suivantes vous semblent être pertinentes.</span>
      </v-layout>
      <v-layout justify-center>
        <span class="font-weight-thin mb-5 white--text ">Souvenez-vous du maître mot : <strong style="text-transform: uppercase;">reformuler</strong>.</span>
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

<template>
  <v-container class="maxWid700">
    <span v-if="step == 0">
      <v-layout justify-center>
        <span class="font-weight-thin mb-2 white--text zind0">Vous allez lire un texte comme :</span>
      </v-layout>
      <v-card max-width="700" class="mx-auto">
        <v-card-text style="font-size:1em;line-height:1.0;" class="pa-2">
          <span class="black--text bold">Le rire apparaît chez l'être humain aux alentours du quatrième ou cinquième mois</span>
        </v-card-text>
      </v-card>
      <v-layout justify-center>
        <span class="font-weight-thin mt-5 mb-0 white--text zind0">Puis une question comme :</span>
      </v-layout>
      <v-layout justify-center>
        <span class="font-weight-thin mb-4 white--text zind0 questionClass">À quel âge l'homme commence t-il à rire ?</span>
      </v-layout>
      <v-layout justify-center>
        <span class="font-weight-thin mt-5 white--text zind0">Ce sera à vous d'évaluer si la question est intéressante.</span>
      </v-layout>
    </span>
    <span v-if="[1].indexOf(step) !== -1">
      <v-layout justify-center>
        <span class="font-weight-thin white--text zind0 title">Qu'est ce qu'une question intéressante&nbsp;?</span>
      </v-layout>
      <v-layout justify-center v-if="step == 1">
        <span class="font-weight-thin mt-10 mb-5 white--text zind0">C'est une question qui utilise des mots différents du texte. On reformule le plus possible avec nos propres mots.</span>
      </v-layout>
    </span>
    <span v-if="[2,3].indexOf(step) !== -1">
      <v-layout justify-center>
        <span class="font-weight-thin white--text zind0 title">Voyons un example&nbsp;:</span>
      </v-layout>
      <v-layout justify-center v-if="step == 1">
        <span class="font-weight-thin mt-10 mb-5 white--text zind0">C'est une question qui utilise des mots différents du texte. On reformule le plus possible avec nos propres mots.</span>
      </v-layout>
      <v-card max-width="700" class="mx-auto mt-3" v-if="[2,3].indexOf(step) !== -1">
        <v-card-text style="font-size:1em;line-height:1.0;" class="pa-2">
          <span class="black--text bold">Le rire apparaît chez l'être humain aux alentours du quatrième ou cinquième mois</span>
        </v-card-text>
      </v-card>
      <v-layout justify-center v-if="[2,3].indexOf(step) !== -1">
        <span class="font-weight-thin mt-5 zind0 questionClass red--text"><span class="white--text">Aux alentours de quand le rire apparaît-il chez l'être humain ?</span>
        </span>
      </v-layout>
      <v-layout justify-center v-if="[2,3].indexOf(step) !== -1">
        <span class="font-weight-thin mt-1 white--text zind0">Ici, on a trop de mots en commun avec le texte : il faut reformuler
        </span>
      </v-layout>
      <v-layout justify-center v-if="[3].indexOf(step) !== -1">
        <span class="font-weight-thin mt-5 white--text zind0">Voilà une bonne reformulation : </span>
      </v-layout>
      <v-layout justify-center v-if="[3].indexOf(step) !== -1">
        <span class="font-weight-thin green--text zind0 questionClass"><span class="white--text">À quel âge un bébé commence t-il à rire ?</span></span>
      </v-layout>
    </span>
    <span v-if="step == 5">
      <v-layout justify-center>
        <h1 class="font-weight-thin mb-5 white--text zind0 title">Le saviez-vous ?</h1>
      </v-layout>
      <v-layout justify-center>
        <span class="font-weight-thin mb-5 white--text zind0">Les <strong>fautes d'orthographes</strong> sont tolérées. <br><br>Il vaut mieux éviter bien sûr, mais rien de grave. Plus on pose des questions proches de la réalité, mieux notre IA pourra nous comprendre !</span>
      </v-layout>
    </span>
    <span v-if="step == 4">
      <v-layout justify-center>
        <h1 class="font-weight-thin mb-5 white--text zind0 title">Le saviez-vous ?</h1>
      </v-layout>
      <v-layout justify-center>
        <span class="font-weight-thin mb-5 white--text zind0">Qu'est ce que reformuler apporte ? Nous voulons une IA qui comprenne une question et soit capable d'y répondre. Si on ne reformulait pas, notre IA chercherait bêtement les mots en commun entre une question et le texte.</span>
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

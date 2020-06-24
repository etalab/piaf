<template>
  <v-container>
    <v-layout justify-center>
      <span class="font-weight-thin mb-5 white--text zind0">Pour annoter, choisissez une catégorie</span>
    </v-layout>
    <v-layout
      text-center
      wrap
    >
      <v-layout row justify-center>
        <v-flex xs6 sm4 md3
          v-for="(theme) in themes"
          v-on:click="setCurrentTheme(theme)"
          :key="theme.name"
        >
          <div class="my-2 d-flex flex-column align-center">
            <v-btn fab large dark v-bind:color="theme.color" v-bind:disabled="theme.empty">
              <v-icon>{{theme.logo}}</v-icon>
            </v-btn>
            <span class="font-weight-thin white--text zind0">{{theme.name}}</span>
          </div>
        </v-flex>
      </v-layout>

    </v-layout>

    <v-layout justify-center v-if="userDetails.is_certified" class="mt-10">
      <span class="font-weight-thin white--text zind0">Plus d'idées pour faire des questions-réponses ?</span>
      <v-btn
      class="mx-2"
      dark
      small
      color="primary"
      v-on:click="$router.push('/annotation/2')">
        Répondre à des questions
      </v-btn>
    </v-layout>

    <v-layout justify-center>
      <v-tooltip left v-bind:open-on-click=true open-delay=1000 max-width=90%>
        <template v-slot:activator="{ on }">
            <span v-on="on" class="font-weight-thin mt-10 white--text zind0">
              Qu'est-ce qu'une bonne question ?
              <v-icon fab small dark >mdi-information-outline</v-icon>
            </span>
        </template>
        <span>Une bonne question sur un paragraphe, c’est une question participe à saisir la variété des vocabulaires, des formulations et des raisonnements qui peuvent survenir dans des questions sur ce paragraphe. C’est donc très large ! La seule limite est que le paragraphe sur lequel porte la question contienne toute l’information nécessaire à la réponse.<br><br> Prenons un exemple : dans le paragraphe <i>"À la fin du mois d’avril 1881, Nietzsche, à Gênes, travaille à la correction des épreuves d’ Aurore avec Peter Gast"</i> (extrait de la page Wikipédia “Biographie de Friedrich Nietzsche”), de bonnes questions peuvent être <i>“Avec qui Nietzche travaille-t-il en 1881 ?”</i>, assez simple, mais aussi <i>“Quel est le nom du livre co-écrit par Nitzche et Gast ?”</i>, qui fait appel à plus de raisonnement et de vocabulaire que ce qui est déjà écrit dans le paragraphe.<br> Une mauvaise question, par contre, serait par exemple <i> “Quel ouvrage est publié par Nietzche 19 ans avant sa mort ?” </i> parce qu’il est nécessaire pour répondre de connaître la date de mort de Nietzche.
        </span>
      </v-tooltip>
    </v-layout>
    <v-layout justify-center>
      <v-tooltip left v-bind:open-on-click=true open-delay=1000 max-width=90%>
        <template v-slot:activator="{ on }">
            <span v-on="on" class="font-weight-thin mt-5 white--text zind0">
              Pourquoi m’a-t-on proposé cet article ?
              <v-icon fab small dark >mdi-information-outline</v-icon>
            </span>
        </template>
        <span>Pour réaliser cette annotation, nous avons sélectionné au préalable un ensemble d’envion 25 000 articles Wikipédia “importants” sur l’internet francophone. “Important” signifie qu’ils possèdent les scores PageRank les plus élevés parmi les pages Wikipédia francophones. Par la suite, nous en avons extrait les paragraphes assez longs pour être compréhensibles, mais pas trop longs non plus (entre 500 et 1000 charactères). Enfin, lorsque vous sélectionnez un thème, nous vous présentons des paragraphes sur ce thème.<br><br> Toutes ces étapes mènent parfois à des résultats étonnants : par exemple des paragraphes sortis de tout contexte, ou sur des sujets sans intérêt à vos yeux, qui découlent de la sélection “à l’aveugle” que nous venons de décrire. Mais il y a un but derrière cela : construire une base de questions-réponses sur des thèmes, des vocabulaires et des styles variés !
        </span>
      </v-tooltip>
    </v-layout>
  </v-container>
</template>

<script>
import { mapState } from 'vuex'

export default {
  computed: {
    ...mapState([
      'themes',
      'userDetails',
    ]),
  },
  methods: {
    setCurrentTheme(theme){
      if(!theme.empty){
        this.$store.commit('setCurrentTheme', theme.name)
        this.$router.push('/annotation/'+this.$route.params.level)
      }
    },
  },
  mounted () {
      this.$store.dispatch('loadDatasetInfo')
  },
};
</script>
<style scoped>
.zind0{
  z-index: 0;
}
</style>

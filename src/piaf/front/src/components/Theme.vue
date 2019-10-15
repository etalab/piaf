<template>
  <v-container>
    <v-layout
      text-center
      wrap
    >

      <v-flex xs12>
        <h1 class="display-2 font-weight-bold">
          Thème
        </h1>
      </v-flex>

      <v-layout row justify-center>
        <v-flex xs6 sm4 md3
          v-for="(theme, i) in themes"
          v-on:click="setCurrentTheme(theme.name)"
        >
          <div class="my-2">
            <v-btn fab large dark v-bind:color="theme.color">
              <v-icon>{{theme.logo}}</v-icon>
            </v-btn>
          </div>
        </v-flex>
      </v-layout>

    </v-layout>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    themes: [
      {
        name: "Histoire",
        logo: "mdi-book-open-page-variant",
        color: "primary"
      },
      {
        name: "Géographie",
        logo: "mdi-map-search",
        color: "warning"
      },
      {
        name: "Société",
        logo: "mdi-city-variant",
        color: "error"
      },
      {
        name: "Sport",
        logo: "mdi-basketball",
        color: "success"
      },
      {
        name: "Religion",
        logo: "mdi-christianity",
        color: "secondary"
      },
      {
        name: "Art",
        logo: "mdi-palette",
        color: "info"
      },
      {
        name: "Sciences",
        logo: "mdi-telescope",
        color: "accent"
      }
    ]
  }),
  methods: {
    setCurrentTheme(theme){
      this.$store.commit('setCurrentTheme', theme)
      this.$store.dispatch('switchFromThemeToAnnotationTask')
    },
  },
};
</script>

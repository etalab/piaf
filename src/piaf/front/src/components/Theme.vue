<template>
  <v-container>
    <v-layout
      text-center
      wrap
    >

      <v-layout row justify-center>
        <v-flex xs6 sm4 md3
          v-for="(theme) in themes"
          v-on:click="setCurrentTheme(theme.name)"
        >
          <div class="my-2 d-flex flex-column align-center">
            <v-btn fab large dark v-bind:color="theme.color">
              <v-icon>{{theme.logo}}</v-icon>
            </v-btn>
            <span class="font-weight-thin grey--text">{{theme.name}}</span>
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
        name: "Arts",
        logo: "mdi-palette",
        color: "info"
      },
      {
        name: "Sciences",
        logo: "mdi-telescope",
        color: "accent"
      },
      {
        name: "Mystère",
        logo: "mdi-help-circle",
        color: "black"
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

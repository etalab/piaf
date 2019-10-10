<template>
  <v-container>
    <v-layout
      text-center
      wrap
    >

      <v-flex xs12>
        <h1 class="display-2 font-weight-bold">
          Annotation
        </h1>
      </v-flex>

      <v-layout row justify-center>
        <v-flex xs6 sm4 md3
          v-for="(theme, i) in themes"
          v-on:click="setTheme(theme.name)"
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

  }),
  methods: {
    setTheme(theme){
      this.$store.commit('setTheme', theme)
    },
  },
};
</script>

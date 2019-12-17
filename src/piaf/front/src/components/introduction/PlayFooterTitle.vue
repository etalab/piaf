<template>
  <v-row class="maxWid700 mx-auto">
    <v-col cols='12' class="pr-0 textContainer bold red--text" v-if="networkIssueMessage">
      Pas de connexion
    </v-col>
    <v-col cols='12' class="pr-0 textContainer" v-else>
      <span>{{title}}</span>
    </v-col>
  </v-row>
</template>

<script>
export default {
  props: {
    networkIssueMessage: Boolean,
    title: String,
  }
};
</script>

<style scoped>
.textContainer{
  display: flex;
  justify-content: space-around;
}
</style>

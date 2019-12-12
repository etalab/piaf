<template>
  <v-container class="maxWid700">
    <span>
      <v-card max-width="700" class="mx-auto">
        <v-card-text style="font-size:1em;line-height:1.7;">
          <span class="black--text bold">{{text}}</span>
        </v-card-text>
      </v-card>
      <v-layout justify-center>
        <span class="font-weight-thin mt-5 white--text zind0 questionClass">{{question}}</span>
      </v-layout>
    </span>
  </v-container>
</template>

<script>
export default {
  props: {
    question: String,
    text: String,
  },
};
</script>
<style scoped>
.maxWid700{
  max-width: 700px;
}
</style>

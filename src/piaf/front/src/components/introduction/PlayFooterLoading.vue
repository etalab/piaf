<template>
  <span>
    <v-row class="maxWid700 mx-auto textContainer" v-if="loading">
      <v-progress-circular
      indeterminate
      color="primary"
      ></v-progress-circular>
    </v-row>

    <v-row class="maxWid700 mx-auto textContainer" v-if="networkIssueMessage && !loading">
      <v-col cols='12' class="pr-0 textContainer">
        <v-btn
        small
        color="primary"
        dark
        class="alignSelf"
        @click="$emit('resubmit')"
        >Ré-essayer
        </v-btn>
      </v-col>
    </v-row>
  </span>
</template>

<script>
export default {
  props: {
    loading: Boolean,
    networkIssueMessage: Boolean,
  }
};
</script>

<style scoped>
.maxWid700{
  max-width: 700px;
}
.textContainer{
  display: flex;
  justify-content: space-around;
}
</style>

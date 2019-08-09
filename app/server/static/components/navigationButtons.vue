<template lang="pug">
  div.columns.is-gapless.is-mobile.is-vertical-center
    div.column.is-1
      div.columns.is-gapless.is-mobile.is-vertical-center(
        v-on:click="reduceCurrentQuestionIndex"
        v-if="currentQuestionIndex > 0"
      )
        i.fas.fa-chevron-left.is-flex.is-justifycontentcenter.has-text-grey-light

    div.column.is-2.has-text-centered(
      v-for="index in [0,1,2,3,4]"
      )
        a.is-rounded.button.is-inline-block(
          v-bind:class="questionClass(index)"
          v-on:click="setCurrentQuestionIndex(index)"
        ) {{index + 1}}
    div.column.is-1
</template>

<script>
export default {
  props: ['currentQuestionIndex','questionClass'],

  methods: {
    setCurrentQuestionIndex(index){
      this.$emit('setCurrentQuestionIndex', index);
    },
    reduceCurrentQuestionIndex(index){
      this.$emit('reduceCurrentQuestionIndex', index);
    },
  },
}
</script>

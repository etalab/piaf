<template lang="pug">
  div.columns.is-gapless.is-mobile.is-vertical-center.mt20
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
      div.columns.is-gapless.is-mobile.is-vertical-center.is-justifycontentright(
        v-on:click="increaseCurrentQuestionIndex"
        v-if="((currentQuestionIndex + 1) < currentNumberOfQuestion) || (currentQuestionIndex + 1 == currentNumberOfQuestion && currentNumberOfAnswer == currentNumberOfQuestion)"
      )
        i.fas.fa-chevron-right.is-flex.has-text-grey-light
</template>

<script>
export default {
  props: ['currentQuestionIndex', 'currentNumberOfQuestion', 'currentNumberOfAnswer', 'questionClass'],

  methods: {
    setCurrentQuestionIndex(index){
      this.$emit('setCurrentQuestionIndex', index);
    },
    reduceCurrentQuestionIndex(index){
      this.$emit('reduceCurrentQuestionIndex', index);
    },
    increaseCurrentQuestionIndex(index){
      this.$emit('increaseCurrentQuestionIndex', index);
    },
  },
}
</script>

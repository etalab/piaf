<template lang="pug">
  section.todoapp.is-transparentbackground(v-if="currentQuestion")
    header.header.card-content
      div.columns.is-gapless.is-mobile.is-vertical-center
          p.column.is-11.new-todo.has-text-left.is-paddingless.is-shadowless {{ currentQuestion.text }}
          a.column.is-1.is-rounded.button.is-inline-block.doneButton {{ buttonMessage }}
</template>

<script>
export default {
  props: ['currentQuestion','buttonMessage'],

  methods: {
    // reduceCurrentQuestionIndex(index){
    //   this.$emit('reduceCurrentQuestionIndex', index);
    // },
  },
}
</script>

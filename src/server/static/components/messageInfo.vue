<template lang="pug">
  article.message.is-link.is-paddingless(
    v-if="messageInfo && displayMessageInfo"
  )
    div.message-header.project-thumbnail
      div.content.text.is-marginless {{ messageInfo }}
      button.delete(
        aria-label="delete"
        v-on:click="displayMessageInfo = !displayMessageInfo"
      )
</template>

<script>
export default {
  data: () => ({
    displayMessageInfo: true,
  }),
  props: ['messageInfo'],
}
</script>

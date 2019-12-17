<template>
  <v-container>
    <v-layout
      text-center
      wrap
    >

      <v-flex xs12 my-5>
        <div>
          <div v-if="currentDocument && annotations">
            <v-card
              max-width="700"
              class="mx-auto"
            >
              <v-card-text style="font-size:1em;line-height:1.7;">
                <TextTitle/>
                <br>
                <v-alert
                  dense
                  outlined
                  type="error"
                  v-show="showErrorMessage"
                >
                  La réponse est <strong>trop longue</strong>, elle doit faire moins de 200 caractères
                </v-alert>
                <TextInteractive
                  v-bind:text="currentDocument.text"
                  v-bind:currentQuestionIndex="currentQuestionIndex"
                  ref="annotator"
                 />
             </v-card-text>
            </v-card>
          </div>
        </div>
      </v-flex>
      </v-layout>

  </v-container>
</template>

<script>
import { mapState } from 'vuex'
import { mapGetters } from 'vuex'
import TextInteractive from './TextInteractive.vue';
import TextTitle from './TextTitle.vue';

export default {
  components: { TextInteractive, TextTitle },
  computed: {
    ...mapState([
      'currentDocument',
      'annotations',
      'currentQuestionIndex',
      'highlitedText'
    ]),
    ...mapGetters([
      'currentDocumentChapitresInfo',
    ]),
    currentAnnotation () {
      return this.$store.getters.currentAnnotation
    },
    showErrorMessage () {
      return typeof this.highlitedText === 'string' && this.highlitedText.length > 200
    },
  },
};
</script>

<style scoped>
.maxWid700{
  max-width: 700px;
}
</style>

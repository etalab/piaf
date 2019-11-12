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
                <v-tooltip left v-bind:open-on-click=true open-delay=1000>
                  <template v-slot:activator="{ on }">
                    <span v-on="on">
                      <span v-html="currentDocument.title" class="black--text bold"></span>
                      <v-icon fab small dark class="black--text ml-1" >mdi-information-outline</v-icon>
                    </span>
                  </template>
                  <span>Titre de l'article Wikipédia dont est extrait ce texte</span>
                </v-tooltip>
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
import TextInteractive from './TextInteractive.vue';

export default {
  components: { TextInteractive },
  computed: {
    ...mapState([
      'currentDocument',
      'annotations',
      'currentQuestionIndex',
      'highlitedText'
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

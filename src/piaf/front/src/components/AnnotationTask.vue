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
                      <span class="black--text bold">
                      <!-- we need to add 1 to take the current paragraph into account -->
                      {{currentDocument.count_completed_paragraphs + 1}} / {{currentDocument.count_pending_paragraphs + currentDocument.count_completed_paragraphs}}
                      </span>
                      <v-icon fab small dark class="black--text ml-1" >mdi-information-outline</v-icon>
                    </span>
                  </template>
                  <span><strong>"{{currentDocument.title}}"</strong> est le titre de l'article Wikipédia dont est extrait ce paragraphe.
                    <span v-if="currentDocumentChapitresInfo.total == 1">
                      Cet article est composé de {{currentDocument.count_pending_paragraphs + currentDocument.count_completed_paragraphs}} paragraphes, et vous en êtes au numéro  {{currentDocument.count_completed_paragraphs + 1}} </strong>.
                    </span>
                    <span v-else>
                      Cet article est découpé en <strong>{{currentDocumentChapitresInfo.total}} chapitres, et vous en êtes au numéro {{currentDocumentChapitresInfo.total - currentDocumentChapitresInfo.toDo + 1}}</strong>. Dans ce chapitre, vous en êtes au <strong>paragraphe {{currentDocument.count_completed_paragraphs + 1}} / {{currentDocument.count_pending_paragraphs + currentDocument.count_completed_paragraphs}}</strong>.
                    </span>
                  <br><br>
                  <strong>Qu'est ce qu'un chapitre ?</strong><br>
                  Pour rendre le travail d'annotation plus agréable, nous avons regroupé les paragraphes en groupe de 5 : les chapitres. Par exemple, un article wikipedia de 8 paragraphes sera découpé en deux chapitres : le premier de 5 paragraphes, et le second de 3 paragraphes.
                  <br><br>
                  <strong>Combien de question faut-il par paragraphe ?</strong><br>
                  Pour chaque paragraphe, il faudra trouver 5 questions-réponses.
                  </span>
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
import { mapGetters } from 'vuex'
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

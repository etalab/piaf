<template>
  <v-tooltip left v-bind:open-on-click=true open-delay=1000>
    <template v-slot:activator="{ on }">
      <span v-on="on">
        <span v-html="currentDocument.title" class="black--text bold"></span>
        <span class="black--text bold" v-if="$route.params.level == 3">
        <!-- we need to add 1 to take the current paragraph into account -->
        {{currentDocument.count_completed_paragraphs + 1}} / {{currentDocument.count_pending_paragraphs + currentDocument.count_completed_paragraphs}}
        </span>
        <v-icon fab small dark class="black--text ml-1" v-if="$route.params.level == 3">mdi-information-outline</v-icon>
      </span>
    </template>
    <span><strong>"{{currentDocument.title}}"</strong> est le titre de l'article Wikipédia dont est issu le paragraphe ci-dessous que vous allez annoter.<br><br>
      <strong>Pourquoi mon article wikipédia est-il divisé en paragraphe ?</strong><br>
      Afin de respecter le protocole scientifique de PIAF ainsi que pour faciliter l’annotation, chaque article wikipédia a été divisé en paragraphe. Chaque paragraphe est numéroté selon sa position dans l’article.

      Ici {{currentDocument.count_completed_paragraphs + 1}} / {{currentDocument.count_pending_paragraphs + currentDocument.count_completed_paragraphs}} signifie que c’est le <span v-if="currentDocument.count_completed_paragraphs == 1">premier paragraphe</span><span v-else>paragraphe numéro {{currentDocument.count_completed_paragraphs + 1}} </span> de l’article sur {{currentDocument.count_pending_paragraphs + currentDocument.count_completed_paragraphs}}.

      <br><br>
      <strong>Combien faut il de questions par paragraphe ?</strong><br>
      Pour chaque paragraphe, il faudra créer 5 couples de “question-réponse”. Ainsi, pour l’ensemble de l’article il vous faudra faire 5 questions-réponses * 5 paragraphes = 25 questions-réponses.

      <br><br>
      <strong>Mais alors faut-il que je fasse 25 questions réponses?</strong><br>
      Pas d’inquiétude ! La seule règle est de compléter un paragraphe soit 5 questions réponses. Si vous vous arrêtez avant, nous ne pourrons malheureusement pas enregistrer vos annotations. Une fois validée, vous pourrez repartir pour un nouveau paragraphe !
      <br><br>


      <strong>J'ai déjà eu "{{currentDocument.title}}", est-ce normal ?</strong><br>
      Cette page Wikipedia était trop longue pour tenir en 5 paragraphes. On a donc créé <span v-if="currentDocumentChapitresInfo.total == 1"> un article</span><span v-else> {{currentDocumentChapitresInfo.total}} articles</span>  portant le même titre, mais avec les textes suivants (vous en êtes au numéro {{currentDocumentChapitresInfo.total - currentDocumentChapitresInfo.toDo + 1}}).
      <br><br>
    </span>
  </v-tooltip>
</template>

<script>
import { mapState } from 'vuex'
import { mapGetters } from 'vuex'

export default {
  computed: {
    ...mapState([
      'currentDocument',
    ]),
    ...mapGetters([
      'currentDocumentChapitresInfo',
    ]),
  },
};
</script>

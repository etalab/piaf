<template>
  <div>
    <span
      oncopy="return false"
      oncut="return false"
      v-for="r in chunks"
      v-bind:class="getChunkClass(r)"
      v-bind:style="getChunkStyle(r)"
      v-touch:tap="setSelectedRange"
      v-touch:start="setSelectedRange"
      v-touch:end="setSelectedRange"
      v-touch:moving="setSelectedRange"
    >
     {{ textPart(r) }}
     <button v-if="r.label==1" v-on:click="removeAnswer(r)">
       <v-icon fab small dark v-bind:color="white">mdi-close</v-icon>
     </button>
    </span>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  data: () => ({
    editMode: false,
  }),

  computed: {
    ...mapState([
      'currentDocument',
      'annotations',
      'currentQuestionIndex'
    ]),
    entityPositionsOrempty () {
      return this.$store.getters.answersForTextInteraction
    },
    // entityPositions() {
    //   // return [this.annotations[this.currentQuestionIndex].answer]
    //   return this.annotations
    //   .map(annotation => annotation.answer)
    //   .filter(answer => typeof answer === 'object')
    // },
    // entityPositionsOrempty() {
    //   return (this.editMode) ? [] : this.entityPositions;
    // },

    sortedEntityPositions() {
      /* eslint-disable vue/no-side-effects-in-computed-properties */
      return this.entityPositionsOrempty.sort((a, b) => a.index - b.index);
      /* eslint-enable vue/no-side-effects-in-computed-properties */
    },

    chunks() {
      const res = [];
      let left = 0;
      let e;
      for (let i = 0; i < this.sortedEntityPositions.length; i++) {
        e = this.sortedEntityPositions[i];
        e.label = 1;
        e.startOffset = e.index
        e.endOffset = e.startOffset + e.text.length

        const l = this.makeEmptyChunk(left, e.startOffset);

        res.push(l);
        res.push(e);
        left = e.endOffset;
      }
      const l = this.makeEmptyChunk(left, this.currentDocument.text.length);
      res.push(l);

      return res;
    },

  },

  methods: {
    getChunkClass(chunk) {
      if (chunk.label === 0) {
        return {};
      }
      return [
        { tag: '#ffffff' },
      ];
    },

    getChunkStyle(chunk) {
      if (chunk.label === 0) {
        return {};
      }
      return {
        color: '#ffffff',
        backgroundColor: '#4169e1',
        paddingRight: '1px',
        paddingLeft: '1px',
        borderRadius: '4px',
        marginRight: '-2px',
        marginLeft: '-2px',
      };
    },


    setSelectedRange() {
      console.log('setSelectedRange');
      let start;
      let end;
      let text;
      if (window.getSelection) {
        const range = window.getSelection().getRangeAt(0);
        const preSelectionRange = range.cloneRange();
        preSelectionRange.selectNodeContents(this.$el);
        preSelectionRange.setEnd(range.startContainer, range.startOffset);
        start = [...preSelectionRange.toString()].length;
        end = start + [...range.toString()].length;
        text = range.toString()
      } else if (document.selection && document.selection.type !== 'Control') {
        const selectedTextRange = document.selection.createRange();
        const preSelectionTextRange = document.body.createTextRange();
        preSelectionTextRange.moveToElementText(this.$el);
        preSelectionTextRange.setEndPoint('EndToStart', selectedTextRange);
        start = [...preSelectionTextRange.text].length;
        end = start + [...selectedTextRange.text].length;
        text = selectedTextRange.text
      }
      this.$store.commit('setStartOffset', start)
      this.$store.commit('setEndOffset', end)
      this.$store.commit('setHighlitedText', text)
    },

    textPart(r) {
      return [...this.currentDocument.text].slice(r.startOffset, r.endOffset).join('');
    },

    makeEmptyChunk(startOffset, endOffset) {
      const chunk = {
        id: 0,
        label: 0,
        startOffset: startOffset,
        endOffset: endOffset,
      };
      return chunk;
    },

    removeAnswer(r){
      let newAnnotations = this.annotations
      console.log('ici i faudra match le R avec sa reponse au cas ou on soit plus sur le bon index');
      newAnnotations[this.currentQuestionIndex].answer = {}
      this.$store.commit('setEndOffset', newAnnotations)
    },
  },

};
</script>

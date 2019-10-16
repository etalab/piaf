<template>
  <div class="alignLeft">
    <span
      oncopy="return false"
      oncut="return false"
      v-for="r in chunks"
      v-bind:style="getChunkStyle(r)"
      v-touch:tap="setSelectedRange"
      v-touch:start="setSelectedRange"
      v-touch:end="setSelectedRange"
      v-touch:moving="setSelectedRange"
    >{{ textPart(r) }}<button v-if="r.label==1" v-on:click="removeAnswer()" class="removeBtn">
       <v-icon fab small dark size=12 >mdi-close</v-icon>
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

    // sortedEntityPositions() {
    //   let answers = this.entityPositionsOrempty.map(anno => {anno.isCurrentAnswer = 0; return anno})
    //   answers[this.currentQuestionIndex].isCurrentAnswer = 1
    //   return answers.sort((a, b) => a.index - b.index);
    // },

    sortedEntityPositions() {
      let arr = this.entityPositionsOrempty[this.currentQuestionIndex]
      arr.isCurrentAnswer = 1
      return [arr]
    },

    chunks() {
      const res = [];
      let left = 0;
      let e;
      for (let i = 0; i < this.sortedEntityPositions.length; i++) {
        e = this.sortedEntityPositions[i];
        if (e.text) {
          e.label = (e.isCurrentAnswer === 1) ? 1 : 2;
          e.startOffset = e.index
          e.endOffset = e.startOffset + e.text.length

          const l = this.makeEmptyChunk(left, e.startOffset);

          res.push(l);
          res.push(e);
          left = e.endOffset;
        }
      }
      const l = this.makeEmptyChunk(left, this.currentDocument.text.length);
      res.push(l);

      return res;
    },

  },

  methods: {
    getChunkStyle(chunk) {
      if (chunk.label === 0) {
        return {};
      }else if (chunk.label === 2) {
        return {
          backgroundColor: '#94afff',
          borderRadius: '4px',
          paddingRight: '0px',
          paddingLeft: '0px',
          marginRight: '-4px',
          marginLeft: '-4px',
        };
      }

      return {
        color: '#ffffff',
        backgroundColor: '#4169e1',
        paddingRight: '0px',
        paddingLeft: '0px',
        borderRadius: '4px',
        marginRight: '-2px',
        marginLeft: '-2px',
      };
    },


    setSelectedRange() {
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

    removeAnswer(){
      this.$store.dispatch('removeAnswer')
    },
  },

  mounted () {
      this.$store.dispatch('loadNewText')
  },

};
</script>
<style scoped>
.alignLeft{
  text-align: left;
}
.removeBtn{
  margin-left: -10px;
  position: absolute;
  margin-top: -6px;
  background-color: #4169e1;
  border-radius: 15px;
}
.removeBtn i{
  font-size: 12px;
}
</style>

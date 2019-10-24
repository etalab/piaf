<template>
  <div id="container">
    <div class="alignLeft paragraph" ref="paragraph">
      <div v-on:mouseenter="setSelectedRange">
      {{this.currentDocument.text}}
      </div>
    </div>
    <v-btn v-on:click="onClick" class="tooltip" id="validate" ref="validate" v-show="highlitedText">
      Valider
    </v-btn>
    <button v-on:click="unselect" id="unselect" ref="unselect" v-show="highlitedText">
      X
    </button>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import SelectText from '@vinyll/selecttext'

export default {
  data: () => ({
    editMode: false,
    highlitedText: false,
  }),

  computed: {
    ...mapState([
      'currentDocument',
    ]),
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

    onClick() {
      this.$store.dispatch('addNewHighlitedText')
      this.$store.commit('setShowFooter',true)
    },

    unselect() {
      this.selector.selectionChanged([])
    },

    moveValidateButton() {
      const button = this.$refs.validate
      const paragraph = this.$refs.paragraph
      const answer = paragraph.querySelector('.selected.last')
      button.$el.style.left = `${answer.offsetLeft}px`
      button.$el.style.top = `${answer.offsetTop}px`
    },

    moveUnselectButton() {
      const button = this.$refs.unselect
      const paragraph = this.$refs.paragraph
      const answer = paragraph.querySelector('.selected.last')
      button.style.left = `${answer.offsetLeft + answer.offsetWidth}px`
      button.style.top = `${answer.offsetTop}px`
    },

    setSelectedRange() {
      let start;
      let end;
      let text;

      const paragraph = this.$refs.paragraph
      this.selector = new SelectText(paragraph)
      this.selector.onSelect = (range) => {
        this.highlitedText = Boolean(range.length)
        let { start, end } = range
        text = paragraph.textContent.substr(end, start - end + 1)
        this.moveValidateButton()
        this.moveUnselectButton()
        if (!this.highlitedText) return
      }

      this.$store.commit('setStartOffset', start)
      this.$store.commit('setEndOffset', end)
      this.$store.commit('setHighlitedText', text)
    },

    textPart(r) {
      return [...this.currentDocument.text].slice(r.startOffset, r.endOffset).join('');
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

<style>
.paragraph span {
  cursor: pointer;
  user-select: none;
}
.paragraph span:hover {
  background-color: #d4e6ff;
}
.paragraph span.selected.first {
  border-top-left-radius: 4px;
  border-bottom-left-radius: 4px;
}
.paragraph span.selected.last {
  border-top-right-radius: 4px;
  border-bottom-right-radius: 4px;
}
.paragraph span.selected {
  color: #ffffff;
  background-color: #4169e1;
}

#container {
  position: relative;
}
#container #validate,
#container #unselect {
  position: absolute;
}

.tooltip { /* This is for the tooltip text */
   background-color: #555;
   text-align: center;
   padding: 10px;
   border-radius: 10px; /* Defines tooltip text position */
   position: absolute;
   z-index: 1;
   min-width: 100px;
   bottom: -50px;
   left: 50%;
   margin-left: -50px;
   margin-top: 30px;
   background-color: #555 !important;
   color: white !important;
}

#unselect {
  background-color: #555;
  color: white;
  padding: 3px;
  font-size: .9em;
  border-radius: 10px;
}

.tooltip::after {
 content: " ";
 position: absolute;
 bottom: 100%; /* This will position the arrow at the top of the tooltip */
 left: 50%;
 margin-left: -10px;
 border-width: 10px;
 border-style: solid;
 border-color: transparent transparent #555 transparent;
 box-shadow: none !important;
}

</style>

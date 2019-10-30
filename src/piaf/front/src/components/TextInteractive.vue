<template>
  <div id="TextInteractive" v-bind:class="{ showErrorMessage: showErrorMessage }">
    <div class="alignLeft paragraph" ref="paragraph">
      <span
      oncopy="return false"
      oncut="return false"
      v-on:mouseenter="setSelectedRange"
      >
      {{this.currentDocument.text}}
      </span>
    </div>
    <!-- <v-btn v-on:click="onClick" class="tooltip" absolute ref="validate" v-show="highlitedText">
      Valider
    </v-btn> -->
    <v-btn v-on:click="removeAnswer" absolute outlined class="delete pa-0" ref="delete" v-show="highlitedText && highlitedText.length > 0">
      <v-icon fab x-small dark>mdi-close</v-icon>
    </v-btn>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import SelectText from '@vinyll/selecttext'

export default {
  data: () => ({
    editMode: false,
  }),

  computed: {
    ...mapState([
      'currentDocument',
      'highlitedText',
      'currentQuestionIndex',
      'startOffset'
    ]),
    showErrorMessage () {
      return typeof this.highlitedText === 'string' && this.highlitedText.length > 200
    },
  },

  methods: {
    setSelectedRange() {
      let start;
      let end;
      let text;

      const paragraph = this.$refs.paragraph
      this.selector = new SelectText(paragraph)
      this.selector.onSelect = (range) => {
        if (range.length) {
          start = range[0]
          end = range[1]
          text = paragraph.textContent.substr(range[0], range[1] - range[0] + 1)

          this.$store.commit('setStartOffset', start)
          this.$store.commit('setEndOffset', end)
          this.$store.commit('setHighlitedText', text)
        } else {
          this.$store.dispatch('removeAnswer')
        }
      }
    },

    removeAnswer(){
      this.$store.dispatch('removeAnswer')
      this.setSelectedRange()
    },

    // onClick() {
    //   this.$store.dispatch('addNewHighlitedText')
    //   this.$store.commit('setShowFooter',true)
    // },

    // moveValidateButton() {
    //   const button = this.$refs.validate
    //   const paragraph = this.$refs.paragraph
    //   const answer = paragraph.querySelector('.selected.last')
    //   button.$el.style.left = `${answer.offsetLeft}px`
    //   button.$el.style.top = `${answer.offsetTop}px`
    // },

    moveDeleteButton() {
      const button = this.$refs.delete
      const paragraph = this.$refs.paragraph
      const answer = paragraph.querySelector('.selected.last')
      if(answer){
        button.$el.style.left = `${answer.offsetLeft + answer.offsetWidth}px`
        button.$el.style.top = `${answer.offsetTop - 8}px`
      }
    },

  },

  watch: {
    currentQuestionIndex: function () {
      this.setSelectedRange()
      let len = typeof this.highlitedText === 'string' ? this.highlitedText.length : 0
      this.selector.addSelection(this.startOffset,len)
    },
    highlitedText: function (text) {
      if (!text) {
        this.setSelectedRange()
      }else{
        this.moveDeleteButton()
        // this.moveValidateButton()
      }
    }
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
/* .removeBtn{
  margin-left: -10px;
  position: absolute;
  margin-top: -6px;
  background-color: #4169e1;
  border-radius: 15px;
}
.removeBtn i{
  font-size: 12px;
} */

.tooltip { /* This is for the tooltip text */
   background-color: #555;
   text-align: center;
   padding: 10px;
   border-radius: 10px; /* Defines tooltip text position */
   z-index: 1;
   min-width: 100px;
   bottom: -50px;
   left: 50%;
   margin-left: -50px;
   margin-top: 30px;
   background-color: #555 !important;
   color: white !important;
}

.delete {
  background-color: #4169e1;
  color: white;
  font-size: .9em;
  border-radius: 15px;
  width: 15px !important;
  height: 15px !important;
  min-width: 15px !important;
}

.delete i{
  font-size: 12px;
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

#TextInteractive.showErrorMessage span.selected, #TextInteractive.showErrorMessage .delete {
  background-color: #de3737 !important;
}

</style>

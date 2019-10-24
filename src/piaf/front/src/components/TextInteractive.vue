<template>
  <div class="alignLeft" id="paragraph">
    <span
    oncopy="return false"
    oncut="return false"
    @click="setSelectedRange"
    >
    {{this.currentDocument.text}}
    </span>
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


    setSelectedRange() {
      let start;
      let end;
      let text;

      const container = document.querySelector('#paragraph')
      //this.$el
      const selector = new SelectText(container)
      selector.onSelect = (range) => {
        console.log('range',range);
        if (range.length) {
          start = range[0]
          end = range[1]
          text = container.textContent.substr(range[0], range[1] - range[0] + 1)

          this.$store.commit('setStartOffset', start)
          this.$store.commit('setEndOffset', end)
          this.$store.commit('setHighlitedText', text)

        } else {
          console.log('not yet defined');
        }
      }

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
#paragraph span {
  cursor: pointer;
  user-select: none;
}
#paragraph span:hover {
  background-color: #d4e6ff;
}
#paragraph span.selected.first {
  border-top-left-radius: 4px;
  border-bottom-left-radius: 4px;
}
#paragraph span.selected.last {
  border-top-right-radius: 4px;
  border-bottom-right-radius: 4px;
}
#paragraph span.selected {
  color: #ffffff;
  background-color: #4169e1;
}

</style>

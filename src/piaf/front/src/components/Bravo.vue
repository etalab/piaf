<template>
  <v-layout class="mx-n2 pa-0" justify-center :key="this.currentDocument.text">
    <span>
      <v-row
         class="spacer mt-10 rowHeight"
         align="center"
         no-gutters
      >
         <v-col cols="1"></v-col>
         <v-col cols="10">
           <div class="talk-bubble tri-right border round btm-left-in">
             <v-chip
               :color="`white lighten-4`"
               class="ml-0 pa-3 round"
               label
               large
               :style="`height:auto`"
             >
               <span style="white-space:normal" class="round">
                 Félicitations! Vous avez écrit <strong>{{userDetails.paragraphs_count * 5}} questions-réponses</strong> depuis votre inscription. Merci beaucoup!
                 <br><br>
                 Le prochain paragraphe n'attend plus que vous!!!
               </span>
             </v-chip>
           </div>
         </v-col>
      </v-row>
      <v-row
         class="spacer"
         align="center"
         no-gutters
       >
         <v-col cols="2">
         <v-avatar
           slot="offset"
           class="ml-auto d-block mt-3 mr-5"
           size="60"
         >
           <img src="https://i.ibb.co/fMQjbXc/logo.png">
         </v-avatar>
        </v-col>
        <v-col cols="10">
        </v-col>
      </v-row>

    </span>
    <Fireworks :boxHeight="'100%'" :boxWidth="'100%'"/>
  </v-layout>
</template>

<script>
import Fireworks from './Fireworks.vue'
import { mapState } from 'vuex'

export default {
  computed: {
    ...mapState([
      'userDetails',
      'currentDocument',
    ]),
  },
  components: { Fireworks },
  mounted () {
      //only necessary to update the information to display after last text was finished, anyway TextInteractive will load it again
      this.$store.dispatch('loadNewText')
      // necessary to update the information to display after last text was finished
      this.$store.dispatch('getUserDetails')

  },
};
</script>
<style scoped>
.rowHeight{
  min-height: 150px;
}
.talk-bubble {
  display: inline-block;
  position: relative;
	height: auto;
	background-color: white;
}
.border{
  border: 3px solid #666;
}
.round{
  border-radius: 30px !important;
	-webkit-border-radius: 30px;
	-moz-border-radius: 30px;
}
.tri-right.border.btm-left-in:before {
	content: ' ';
	position: absolute;
	width: 0;
	height: 0;
	left: 36px;
  right: auto;
  top: auto;
	bottom: -23px;
	border: 20px solid;
	border-color: #666 transparent transparent #666;
}
.tri-right.btm-left-in:after{
	content: ' ';
	position: absolute;
	width: 0;
	height: 0;
	left: 38px;
  right: auto;
  top: auto;
	bottom: -20px;
	border: 12px solid;
	border-color: white transparent transparent white;
}

</style>

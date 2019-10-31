<template>
  <v-flex xs12 my-0 justify-center class="container">
    <v-row class="maxWid700 mx-auto textContainer bold">
      Bravo !
    </v-row>
    <v-row class="maxWid700 mx-auto">
      <v-col
        cols='3'
        class="px-0"
      >
      </v-col>
      <v-col cols='6' class="pr-0 textContainer">

        <v-btn
        class="mx-2"
        fab
        dark
        x-small
        color="secondary"
        v-on:click="removeAnswer">
          <v-icon dark>mdi-arrow-left</v-icon>
        </v-btn>

        <v-btn
        v-if="currentQuestionIndex === 4"
        small
        color="primary"
        dark
        v-on:click="validate"
        class="alignSelf"
        >Valider mes 5 questions
        </v-btn>


        <v-btn
        v-else
        small
        color="primary"
        dark
        v-on:click="next"
        class="alignSelf"
        >Continuer
        </v-btn>

      </v-col>
      <v-col
        cols='3'
        class="px-0"
      >
      </v-col>
    </v-row>
  </v-flex>
</template>

<script>
import { mapState } from 'vuex'

export default {
  computed: {
    ...mapState([
      'currentQuestionIndex'
    ]),
  },
  methods:{
    validate(){
      let res = this.$store.dispatch('saveQAs')
      if (res) {
        this.next()
      } else {
        // eslint-disable-next-line
        console.log('error in the Q or A');
      }
    },
    next(){
      this.$store.commit('setShowFooter',false)
      return this.$store.dispatch('goToNextIndex')
    },
    removeAnswer(){
      return this.$store.dispatch('removeAnswer')
    },
  },
};
</script>

<style scoped>
/* for all */
.maxWid700{
  max-width: 700px;
}
.alignSelf{
  align-self: center;
}
.container{
}
.textContainer{
  display: flex;
  justify-content: space-around;
}
</style>

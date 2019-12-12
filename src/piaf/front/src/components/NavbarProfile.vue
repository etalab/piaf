<template>
  <v-flex xs12 my-0 justify-center>
    <v-row class="maxWid700 mx-auto">
      <v-col
        cols='1'
        class="px-0"
      >
      <v-avatar
        slot="offset"
        class="mx-auto d-block"
        size="30"
      >
        <img
          src="https://i.ibb.co/fMQjbXc/logo.png"
        >
      </v-avatar>
      </v-col>
      <v-col cols='10' class="pr-0 alignSelf bold fontSpecific" style="text-align:center;font-size:22px">
        {{NavbarTitle}}
      </v-col>
      <v-col
        cols='1'
        class="px-0"
      >
        <UserProfile />
      </v-col>
    </v-row>
  </v-flex>

</template>

<script>
import { mapState } from 'vuex'
import UserProfile from './UserProfile.vue';

export default {
  components: {
    UserProfile,
  },
  props : {
    NavbarTitle: {
      type: String,
      default: 'Edite Piaf'
    },
  },
  computed: {
    ...mapState([
      'currentQuestionIndex'
    ]),
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
.minwidth{
  min-width: 32px;
}

.fontSpecific {
  font-family: 'luckiest guy' !important;
  text-decoration: none;
  color: #333;
}
</style>

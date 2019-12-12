<template>
  <span style="position:relative; display: inline-table">
    <div class="button-wrapper flex" :class="levelClass">
      <a class="background-button"
        :class="{active : active}"
        @click="onClick()"
        :title="text + ` ` + level"></a>
    </div>
    <v-icon x-large dark class="lock" v-if="locked">mdi-lock</v-icon>
  </span>
</template>

<script>
export default {
  props: {
    text: String,
    title: String,
    active: Boolean,
    locked: Boolean,
    level: Number,
    levelClass: String,
    iconType: String,
  },
  methods: {
    onClick(){
      if (this.active) {
        this.$router.push('introduction/' + this.level)
      }
    },
  }
};
</script>
<style scoped>
a {
  position: relative;
  width: 100%;
  padding-top: 25.92%;
  display: block;
  background-size: 100% 100%;
  font-family: 'luckiest guy';
  font-size: 28px;
  margin-bottom: 20px;
  text-decoration: none;
  color: #333;
  cursor: not-allowed;
}

a.active{
  cursor: pointer;
}

a.background-button {
  background-image: url(https://s3-us-west-2.amazonaws.com/s.cdpn.io/323909/yellow-shadow.png);
  background-size: contain;
}

a.background-button:after {
    content: attr(title);
    width: 100%;
    height: 100%;
    position: absolute;
    top: 0;
    left: 0;
    display: block;
    background-image: url(https://s3-us-west-2.amazonaws.com/s.cdpn.io/323909/yellow-top.png);
    background-size: contain;
    transition: all 0.3s;
    display: flex;
    justify-content: center;
    align-items: center;
}
a.background-button.active:hover:after {
    -webkit-transform: translate(2.5%, 10%);
    transform: translate(2.5%, 10%);
    text-shadow: 2px 2px 1px white;
    color: black;
}

.button-wrapper {
  width: 200px;
  display: inline-block;
  margin: 20px;
}

.btngreen {
    -webkit-filter: hue-rotate(72deg);
    filter: hue-rotate(72deg);
}
.btnyellow {
}
.btngrey {
    -webkit-filter: hue-rotate(153deg);
    filter: hue-rotate(153deg);
    filter: grayscale(1)
}
.btnorange {
    -webkit-filter: hue-rotate(324deg);
    filter: hue-rotate(324deg);
}
/* ackowledgment: https://codepen.io/DeeDee23/pen/dNEwem */
.lock{
  text-shadow: 0.5px 0.5px 0 #989898, 0.5px -0.5px 0 #989898, -0.5px 0.5px 0 #989898, -0.5px -0.5px 0 #989898, 0.5px 0px 0 #989898, 0px 0.5px 0 #989898, -0.5px 0px 0 #989898, 0px -0.5px 0 #989898;
  position: absolute;
  top: 0px;
  right: 10px;
}
</style>

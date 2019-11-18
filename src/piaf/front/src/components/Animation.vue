<template>
  <div class="home-top absolute">
    <div class="svg-container absolute">
      <svg class="home-top__gradient-back absolute" viewBox="0 0 1412 692">
        <path fill-rule="evenodd" transform="translate(-10, 70) scale(1.05)" opacity="0.059" fill="rgb(255, 255, 255)" d="M4,8 C4,8 224,-33 468,68 C711,171 868,270 1155,248 C1270,238 1411,165 1412,165 L1412,692 L0,692 L4,8 Z"/>
      </svg>
      <svg class="home-top__gradient-front absolute" viewBox="0 0 1415 623">
        <defs>
          <linearGradient id="PSgrad_0" x1="0%" x2="71.934%" y1="0%" y2="69.466%" gradientTransform="rotate(44)">
            <stop offset="0%" stop-color="rgb(14,7,54)" stop-opacity="1" />
            <stop offset="100%" stop-color="rgb(10,5,40)" stop-opacity="0" />
          </linearGradient>
        </defs>
        <g transform="translate(-20, 40) scale(1.05)">
          <path fill="url(#PSgrad_0)" d="M11,7 C11,7 260,-40 738,126 C1021,231 1415,171 1415,171 L1415,623 L0,623 L0,14 L11,7 Z"/>
        </g>
      </svg>
    </div>
  </div>
</template>

<script>
export default {
  mounted () {
    document.addEventListener("DOMContentLoaded", function() {
      const anime = require('animejs')
      anime.default({
        targets: '.home-top__gradient-front path',
        d: 'M11,0 C11,-10 260,-60 738,136 C1021,251 1415,171 1415,171 L1415,623 L0,623 L0,14 L11,7 Z',
        duration: 2000,
        loop: true,
        direction: 'alternate',
        easing: 'linear'
      });
      anime.default({
        targets: '.home-top__gradient-back path',
        d: 'M4,8 C4,-20 224,-33 468,58 C711,171 868,290 1155,268 C1270,258 1411,165 1412,165 L1412,692 L0,692 L4,8 Z',
        duration: 2500,
        loop: true,
        direction: 'alternate',
        easing: 'linear'
      });
    });
  },
}
</script>
<style scoped>
.absolute{
  position: absolute;
}
.svg-container{
  display: contents;
  /* display: block; */
}
.home-top {
  overflow: hidden;
  content: "";
  width: 100%;
  height: 100%;
  bottom: 0;
  right: 0;
  background: linear-gradient(44deg, #130c47 0%,#1d4b9f 87%,#8760e9 100%);
  transform: rotateX(180deg);
  z-index: -1;
}
svg{
  min-height: 150%;
  min-width: 700px;
  width: 100%;
  bottom: 0px;
  transform: rotateY(180deg);
  transform: rotateX(180deg);
}
</style>

<template>
  <router-view/>
</template>

<style>
.v-application {
   background-color: transparent !important;
   font-family: "cooperhewitt light" !important;
    .title {
       font-family: "cooperhewitt medium" !important;
    }
}
html, .v-application {
  font-size: 14px;
}
@media (min-width:700px) {
  html, .v-application {
    font-size: 18px;
  }
}
strong{
  font-family: "cooperhewitt medium" !important;
}
.bold{
  font-family: "cooperhewitt medium" !important;
}
.v-tooltip__content{
  background-color: #616161 !important;
  opacity: 1 !important;
}
</style>

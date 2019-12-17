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
.questionClass{
  background-color: #00000024;
  border-radius: 5px;
  padding-left: 5px;
  padding-right: 5px;
  border: solid 1px;
  font-size: 1.2em;
  /* font-style: italic !important; */
}
.maxWid700{
  max-width: 700px;
}
.textContainer{
  display: flex;
  justify-content: space-around;
}
.alignSelf{
  align-self: center;
}
</style>

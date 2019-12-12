<template>
  <span>
    <Play1 v-if="$route.params.level == 1"/>
    <Play2 v-if="$route.params.level == 2"/>
    <Play3 v-if="$route.params.level == 3"/>
  </span>
</template>

<script>
import Play1 from '../../components/introduction/Play1';
import Play2 from '../../components/introduction/Play2';
import Play3 from '../../components/introduction/Play3';

export default {
  components: {
    Play1,
    Play2,
    Play3,
  },
};
</script>

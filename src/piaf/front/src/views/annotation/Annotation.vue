<template>
  <span>
    <Annotation1 v-if="$route.params.level == 1"/>
    <Annotation2 v-if="$route.params.level == 2"/>
    <Annotation3 v-if="$route.params.level == 3"/>
  </span>
</template>

<script>
import Annotation1 from '../../components/annotation/Annotation1';
import Annotation2 from '../../components/annotation/Annotation2';
import Annotation3 from '../../components/annotation/Annotation3';

export default {
  components: {
    Annotation1,
    Annotation2,
    Annotation3,
  },
};
</script>

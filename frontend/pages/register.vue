<template>
  <register/>
</template>

<script lang="ts">
import Vue from 'vue'
import Register from '~/components/register.vue';


export default Vue.extend({
    name: 'IndexPage',
    components: { Register }
})
</script>

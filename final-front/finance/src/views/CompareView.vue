<template>
  <main>
    <h1>비교</h1>
    <nav>
      <RouterLink to="/deposit">예금</RouterLink> 
      <RouterLink to="/saving" class="nav-link">적금</RouterLink>
    </nav>
  </main>
</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>

<style scoped>

</style>
<template>
  <main>
    <h1>비교</h1>
    <nav>
      <div class="box">
        <RouterLink to="/deposit" class="nav-link">예금</RouterLink> 
      </div>
      <div class="box">
        <RouterLink to="/saving" class="nav-link">적금</RouterLink>
      </div>
    </nav>
  </main>
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>
nav{
  display: flex;
  flex-direction: row;
}

.box{
  padding-left: 20px;
}
</style>
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
  <p class="mb-0 bg-light text-center py-2 fixed-bottom" style="width: 100%; font-size: small;" >&copy; 2023 Finew All Rights Reserved. 본 사이트의 콘텐츠는 저작권법의 보호를 받는 바 무단 전재, 복사, 배포 등을 금합니다.</p>

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
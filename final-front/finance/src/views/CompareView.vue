<template>
  <main class="container">
    <h1 class="headers">예금 적금 비교</h1>
    <div class="wrapper">
      <div class="box">
        <router-link to="/deposit" class="nav-link">
          <img class="img1" src="@/assets/compare1.jpg">
        </router-link>
      </div>
      <div class="box">
        <router-link to="/saving" class="nav-link">
          <img class="img2" src="@/assets/compare2.jpg">
        </router-link>
      </div>
    </div>
  </main>
  <RouterView />
  <p class="mb-0 bg-light text-center py-2" style="width: 100%; font-size: small;" >&copy; 2023 Finew All Rights Reserved. 본 사이트의 콘텐츠는 저작권법의 보호를 받는 바 무단 전재, 복사, 배포 등을 금합니다.</p>

</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>
nav{
  display: flex;
  flex-direction: row;
}
.box:hover {
  transform: scale(1.05);
  transition: transform 0.2s ease-in-out;
}
.wrapper{
  display: flex;
  justify-content: center;
  margin-bottom: 80px;
}
.img1{
  width:100%;
  border-top-left-radius: 100px;
  border-bottom-left-radius: 100px;
}

.img2{
  width:100%;
  border-top-right-radius: 100px;
  border-bottom-right-radius: 100px;
}

.headers{
  color: #255580;
  font-weight: bold;
  margin-top: 50px;
  margin-bottom: 40px;
  display: flex;
  justify-content: center;
}
.container{
  font-family: 'Noto Sans KR', sans-serif; /* Noto Sans KR 글씨체 적용 */
  margin-bottom: 40px;
}
</style>
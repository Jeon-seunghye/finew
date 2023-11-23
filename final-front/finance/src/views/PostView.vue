
<template>
  <div>
    <div class="title">
      <p>자 유 게 시 판</p>
    </div>
    <div class="container">
      <button @click="router.push({ name: 'create' })" class="create-button">글쓰기</button>
    </div>
    <ArticleList />
  </div>
  <p class="mb-0 bg-light text-center py-2 fixed-bottom" style="width: 100%; font-size: small;" >&copy; 2023 Finew All Rights Reserved. 본 사이트의 콘텐츠는 저작권법의 보호를 받는 바 무단 전재, 복사, 배포 등을 금합니다.</p>

</template>

<script setup>
import { useRouter } from 'vue-router';
import ArticleList from '../components/ArticleList.vue';
const router = useRouter()
</script>

<style scoped>
  .create-button {
    font-family: 'Noto Sans KR', sans-serif; /* Noto Sans KR 글씨체 적용 */
    padding: 12px;
    background-color: #2980b9; /* 짙은 파란색 */
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
    float: right;
    margin-right: 20px;
    margin-bottom: 10px;
    opacity: 70%;
    height: 26px;
    font-size: small;
    display: flex;
    align-items: center;
  }

  .create-button:hover {
    background-color: #1f618d; /* 더 어두운 파란색 */
  }
  .title{
    font-size: xx-large;
    font-weight: 900;
    text-align: center;
    background-image: url('@/assets/bg1.jpg');
    background-size: cover;
    height: 150px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Arial', sans-serif;
    color: white;
    /* text-shadow: -1px 0 #1f618d, 0 1px #1f618d, 1px 0 #1f618d, 0 -1px #1f618d; */
    margin-bottom: 20px;
  }
</style>
<template>
  <a class="icon-link icon-link-hover boardlist" style="--bs-link-hover-color-rgb: 25, 135, 84;" href="/board">
    ← 게시글 목록
    <svg class="bi" aria-hidden="true"></svg>
  </a>
  <div class="container">
    <h1>게시글 등록</h1>
    <form @submit.prevent="submitData">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model.trim="title">

      <label for="content">내용 : </label>
      <input type="text" id="content" v-model.trim="content">

      <button @submit.prevent="submitData" class="create-button">등록하기</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useArticleStore } from '@/stores/article.js'

const store = useArticleStore()

const title = ref('')
const content = ref('')

const submitData = function () {
  const article = {
    title: title.value,
    content: content.value
  }
  store.createArticle(article)
  title.value = ''
  content.value = ''
}

</script>

<style scoped>
  .boardlist{
    margin-top: 20px;
    margin-left: 20px;
  }
  .container{
    margin-top: 30px;
    font-family: 'Noto Sans KR', sans-serif;
  }

  h1 {
    color: #333;
  }

  form {
    margin-top: 20px;
  }

  label {
    display: block;
    margin-bottom: 5px;
  }

  input[type="text"] {
    width: 100%;
    padding: 5px;
    margin-bottom: 10px;
  }

  .create-button {
    font-family: 'Noto Sans KR', sans-serif; /* Noto Sans KR 글씨체 적용 */
    padding: 12px;
    background-color: #cfe2f3;
    color: #333;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
    float: right;
    margin-right: 10px;
    margin-bottom: 10px;
    opacity: 70%;
    height: 26px;
    font-weight: bold;
    font-size: small;
    display: flex;
    align-items: center;
  }
</style>
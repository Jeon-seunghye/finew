
<template>
  <div>
    <h1 class="post-title">{{ article.title }}</h1>
    <p class="post-content">{{ article.content }}</p>
    <p>제목 : {{ article.title }}</p>
    <p>내용 : {{ article.content }}</p>
    <p>작성일 : {{ article.created_at }}</p>
    <p>수정일 : {{ article.updated_at }}</p>
    <button @click="deleteArticle" class="delete-button">게시글 삭제</button>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue';
import { useArticleStore } from '@/stores/article';
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const store = useArticleStore();
const article = ref({})
const router = useRouter();

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/articles/${route.params.id}/`
  })
    .then((res) => {
      // console.log(res.data)
      article.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
})

const deleteArticle = () => {
  axios({
    method: 'delete',
    url: `${store.API_URL}/articles/${route.params.id}/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then(() => {
      // Redirect to the board or home page after deletion
      router.push({ name: 'board' })
    })
    .catch((err) => {
      console.log(err)
    })
}

</script>

<style scoped>
.post-title {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 28px;
  margin-top: 20px;
  margin-bottom: 20px;
  text-align: center;
  color: #3498db;
}

.post-content {
  font-size: 18px;
  color: #2c3e50;
  margin-top: 10px;
}
</style>


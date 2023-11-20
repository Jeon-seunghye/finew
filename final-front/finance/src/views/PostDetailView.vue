
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
  <hr>
  <div>
    <h3>댓글</h3>
    <form @submit.prevent="createComment">
      <label for="">댓글 내용 :</label>
      <input type="text" v-model.trim="content" />
      <input type="submit" value="댓글작성" />
    </form>

    <div v-for="comment in article.comment_set">
      <p>{{ comment.content }}</p>
      <input type="submit" value="삭제" @click="deleteComment(comment.id)" />

    </div>

  </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue';
import { useArticleStore } from '@/stores/article';
import { useRoute, useRouter } from 'vue-router'
import { computed } from 'vue';

const store = useArticleStore();
const route = useRoute()
const router = useRouter();
const token = store.token
const article = ref({})
const content = ref('')


onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/articles/${route.params.id}/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
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

  // 댓글 전부 가져오기
  onMounted(() => {
    store.getComments()
  })


// 댓글 생성
const createComment = function () {
  axios({
    method : 'post',
    url: `${store.API_URL}/articles/${article.value.id}/comments/`,
    data : {
      content : content.value
    },
    headers: {
        Authorization: `Token ${token}`
    }
  })
  .then((res)=>{
      console.log(res.data)
      article.value.comment_set.push(res.data)
      content.value = ''
    })
    .catch((err)=>{
      console.log(err);
    })
}

  // 댓글 삭제
  const deleteComment = (commentId) => {
  axios({
    method: 'delete',
    url: `${store.API_URL}/articles/comments/${commentId}/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then(() => {
      // Redirect to the board or home page after deletion
      router.push({ name: 'postdetail' })
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


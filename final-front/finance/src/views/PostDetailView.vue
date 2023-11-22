
<template>
  <div>
    <a class="icon-link icon-link-hover boardlist" style="--bs-link-hover-color-rgb: 25, 135, 84;" href="/board">
      ← 게시글 목록
      <svg class="bi" aria-hidden="true"></svg>
    </a>
    <h1 class="post-title">{{ article.title }}</h1>
    <div class="contents">
      <p class="post-content">내용 <br><br>{{ article.content }}</p>
      <div class="date">
        <p>작성일 : {{ formatDate(article.created_at) }}</p>
        <p>수정일 : {{ formatDate(article.updated_at) }}</p>
      </div>
    </div>
    <div class="buttons">
        <router-link :to="{ name: 'postUpdate', params: { id: article.id } }">
          <button class="update-button">게시글 수정</button>
        </router-link>
      <button @click="deleteArticle" class="delete-button">게시글 삭제</button>
    </div>
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
      alert('게시글 삭제가 불가능합니다.');
      console.log(err)
    })
}


// 댓글 전부 가져오기
onMounted(() => {
  store.getComments()
})

const formatDate = (date) => {
  const formattedDate = new Date(date);
  const year = formattedDate.getFullYear();
  const month = (formattedDate.getMonth() + 1).toString().padStart(2, '0');
  const day = formattedDate.getDate().toString().padStart(2, '0');
  const hours = formattedDate.getHours().toString().padStart(2, '0');
  const minutes = formattedDate.getMinutes().toString().padStart(2, '0');
  
  return `${year}-${month}-${day} ${hours}:${minutes}`;
};

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
.boardlist{
  margin-top: 20px;
  margin-left: 20px;
}
.update-button{
  margin: 5px;
  border: 1px solid lightgray;
  border-radius: 10%;
  opacity: 70%;
  color: gray;
  font-size: 15px;
}
.delete-button{
  margin: 5px;
  border: 1px solid lightgray;
  border-radius: 10%;
  opacity: 70%;
  color: gray;
  font-size: 15px;
}
.post-title {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 28px;
  margin-top: 20px;
  margin-bottom: 20px;
  text-align: center;
  color: #3498db;
}
.contents{
  margin-left: 40px;
  text-align: left;
}
.post-content {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 20px;
  color: #2c3e50;
  margin-top: 10px;
}
.date{
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 15px;
}
.buttons{
  text-align: right;
  margin-right: 40px;
}
</style>


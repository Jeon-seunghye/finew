
<template>
  <div>
    <a class="icon-link icon-link-hover boardlist" style="--bs-link-hover-color-rgb: 25, 135, 84;" href="/board">
      ← 게시글 목록
      <svg class="bi" aria-hidden="true"></svg>
    </a>
    <h1 class="post-title">{{ article.title }}</h1>
    <div class="contents">
      <h5 >내용</h5><br>
      <p class="post-content">{{ article.content }}</p>
      <div class="date">
        <br>
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
  <div class="contents">
    <h3>댓글 &nbsp;{{ article.comment_count }}</h3>
    <form @submit.prevent="createComment">
      <label for="">내용 &nbsp;</label>
      <input class="commenting" type="text" v-model.trim="content" />
      <input class="creating" type="submit" value="댓글작성" />
    </form>
    <br>
    <div v-for="(comment, index) in article.comment_set" :key="comment.id">
      <span><b>No. {{ index + 1 }} &nbsp;|</b></span> 
      <span style="margin-left: 15px;">{{ comment.content }}</span>
      <input class="deletebtn" type="submit" value="삭제" @click="deleteComment(comment.id)" />
      <hr style="margin-right: 40px;">
    </div>
  </div>
  <p class="mb-0 bg-light text-center py-2 fixed-bottom" style="width: 100%; font-size: small;" >&copy; 2023 Finew All Rights Reserved. 본 사이트의 콘텐츠는 저작권법의 보호를 받는 바 무단 전재, 복사, 배포 등을 금합니다.</p>

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
  font-size: 35px;
  margin-top: 20px;
  margin-bottom: 20px;
  text-align: center;
  color: #3498db;
}
.contents{
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 15px;
  margin-left: 40px;
  text-align: left;
}
.post-content {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 30px;
  color: #2c3e50;
  margin-top: 5px;;
}
.date{
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 15px;
}
.buttons{
  text-align: right;
  margin-right: 40px;
}
.commenting{
  width: 400px;
}
.creating{
  margin-left: 30px;
  opacity: 70%;
  background-color: lightslategray;
  border-color: lightslategray;
  border-radius: 5px;
  color: white;
  font-weight: 500;
}
.deleting{
  display: flex;
}

.deletebtn{
  margin-left: 30px;
  opacity: 60%;
  background-color: #6bb4e4;
  border-color: #6bb4e4;
  border-radius: 5px;
  color: white;
  font-weight: 500;
}
</style>


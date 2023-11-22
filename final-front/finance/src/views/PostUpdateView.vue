<template>
  <div>
    <a class="icon-link icon-link-hover boardlist" style="--bs-link-hover-color-rgb: 25, 135, 84;" href="/board">
      ← 게시글 목록
      <svg class="bi" aria-hidden="true"></svg>
    </a>
    <div class="container">
      <h2 class="headers">게시글 수정</h2>
      <div v-bind="article in store.articles" :key="article.pk">
        <form @submit.prevent="updateArticle" class="submits">
          <label class="title" for="title">제목</label>
          <input v-model.trim="article.title" id="title" type="text" required />
          <label class="content" for="content">내용</label>
          <textarea v-model.trim="article.content" id="content" rows="4" required></textarea>
          <div>
            <button type="submit" class="update-button">수정</button>
          </div>
        </form>
  
      </div>
    </div>
    
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios';
import { useArticleStore } from '@/stores/article';

const router = useRouter();
const route = useRoute();
const store = useArticleStore();
const article = ref({ title: '', content: '' });

console.log(route.params)

onMounted(() => {
  // Fetch the article details when the component is mounted
  axios
    .get(`${store.API_URL}/articles/${route.params.id}/`, {
      headers: {
        Authorization: `Token ${store.token}`,
      },
    })
    .then((res) => {
      article.value = res.data;
    })
    .catch((err) => {
      console.error(err);
    });
});

const updateArticle = () => {
  axios
    .put(
      `${store.API_URL}/articles/${route.params.id}/`,
      {
        title: article.value.title,
        content: article.value.content,
      },
      {
        headers: {
          Authorization: `Token ${store.token}`,
        },
      }
    )
    .then(() => {
      alert('게시글이 업데이트 되었습니다.');
      router.push({ name: 'board' });
    })
    .catch((err) => {
      alert('게시글 수정이 불가능합니다.');
      console.log(err)
      router.push({ name: 'board' });
    });
};
</script>

<style scoped>

  .headers{
    color: #255580;
    font-weight: bold;
  }
  .boardlist{
    font-family: 'Noto Sans KR', sans-serif; /* Noto Sans KR 글씨체 적용 */
    margin-top: 20px;
    margin-left: 20px;
  }
  .container{
    font-family: 'Noto Sans KR', sans-serif; /* Noto Sans KR 글씨체 적용 */
    margin-top: 20px;
  }
  
  .update-button{
    font-family: 'Noto Sans KR', sans-serif; /* Noto Sans KR 글씨체 적용 */
    padding: 12px;
    background-color: #cfe2f3;
    color: #333;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
    float: right;
    margin-top: 20px;
    margin-bottom: 10px;
    opacity: 70%;
    height: 26px;
    font-weight: bold;
    font-size: small;
    display: flex;
    align-items: center;
  }
  .submits{
    display: flex;
    flex-direction: column;
  }
  .title{
    margin-top: 20px;
    margin-bottom: 5px;
  }
  .content{
    margin-top: 20px;
    margin-bottom: 5px;
  }

</style>

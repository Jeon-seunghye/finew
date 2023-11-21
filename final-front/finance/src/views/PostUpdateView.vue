<template>
  <div>
    <h2>수정하기</h2>
    <div v-bind="article in store.articles" :key="article.pk">
      {{ article.title }}
      {{ article.id }}
      <form @submit.prevent="updateArticle">
        <label for="title">Title:</label>
        <input v-model.trim="article.title" id="title" type="text" required />
        <label for="content">Content:</label>
        <textarea v-model.trim="article.content" id="content" rows="4" required></textarea>
        <button type="submit">Update Article</button>
      </form>
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
      router.push({ name: 'board' });
    });
};
</script>

<style scoped>
/* Add any necessary styles for your form */
</style>

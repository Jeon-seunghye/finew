<template>
  <div>
    <ul>
      <div
        v-for="article in store.articles"
        :key="article.pk"
      >
        <h3>{{ article.id }}번 게시글</h3>
        <p>작성자 : {{ article.user.username }}</p>
        <p>제목 : {{ article.title }}</p>
        <router-link :to="{ name: 'postdetail', params: { id: article.id } }">
          <button class="view-detail-button">게시글 상세 보기</button>
        </router-link>
        <hr>
      </div>
    </ul>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useArticleStore } from '@/stores/article'
const store = useArticleStore()

onMounted(() => {
  store.getArticles()
})
</script>

<style scoped>
.view-detail-button {
  font-family: 'Noto Sans KR', sans-serif;
  padding: 8px;
  background-color: #3498db; /* 파란색 */
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.view-detail-button:hover {
  background-color: #2980b9; /* 더 어두운 파란색 */
}
</style>

<template>
  <div>
    <h1 class="board-title">Board</h1>
    <button @click="router.push({ name: 'create' })" class="create-button">새 글 쓰기</button>
    <ArticleList />
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import ArticleList from '../components/ArticleList.vue';
const router = useRouter()
</script>

<style scoped>
.board-title {
  font-family: 'Noto Sans KR', sans-serif; /* Noto Sans KR 글씨체 적용 */
  font-size: 28px;
  margin-top: 20px;
  margin-bottom: 20px;
  text-align: center;
  color: #3498db; /* 파란색 */
}

.create-button {
  font-family: 'Noto Sans KR', sans-serif; /* Noto Sans KR 글씨체 적용 */
  padding: 12px;
  background-color: #2980b9; /* 짙은 파란색 */
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
  display: block; /* 버튼을 블록 레벨로 표시하여 가로 중앙 정렬 */
  margin: 0 auto; /* 가로 중앙 정렬 */
}

.create-button:hover {
  background-color: #1f618d; /* 더 어두운 파란색 */
}

/* 게시글 목록 스타일링 */
.article-list {
  list-style: none;
  padding: 0;
}

.article-item {
  background-color: #ecf0f1; /* 연한 회색 */
  border: 1px solid #bdc3c7; /* 연한 은색 */
  border-radius: 5px;
  margin-bottom: 10px;
  padding: 15px;
}

.article-title {
  font-size: 18px;
  color: #2c3e50; /* 어두운 회색 */
}

.article-content {
  margin-top: 10px;
  color: #34495e; /* 더 어두운 회색 */
}
</style>
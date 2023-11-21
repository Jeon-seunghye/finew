<template>
  <div class="container cmargin">
    <ul>
      <table class="table">
        <thead class="tablehead table-primary">
          <tr>
            <th scope="col">#</th>
            <th scope="col">작성자</th>
            <th scope="col">제목</th>
            <th scope="col">상세 보기</th>
          </tr>
        </thead>
        <tbody class="table-group-divider">
          <tr v-for="(article, index) in store.articles" :key="article.pk">
            <td scope="row">{{ index + 1 }}</td>
            <td>{{ article.user.username }}</td>
            <td>{{ article.title }}</td>
            <td>
              <router-link :to="{ name: 'postdetail', params: { id: article.id } }">
                <button class="view-detail-button">상세 보기</button>
              </router-link>
              <router-link :to="{ name: 'postdetail', params: { id: article.id } }">
                <img class="imgTag" src="src/assets/comments.png" >
              </router-link>
              {{ article.comment_count }}
            </td>
          </tr>
        </tbody>
      </table>
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

.cmargin{
  margin-top: 10px;
}
.imgTag{
  margin-left: 20px;
  width: 20px;
}

.view-detail-button {
  font-family: 'Noto Sans KR', sans-serif;
  padding: 8px;
  background-color: #3498db; /* 파란색 */
  color: white;
  border: none;
  border-radius: 5px;
  opacity: 40%;
  cursor: pointer;
  transition: background-color 0.3s;
}

.view-detail-button:hover {
  background-color: #2980b9; /* 더 어두운 파란색 */
}
</style>
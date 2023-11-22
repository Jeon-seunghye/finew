<template>
  <div class="container cmargin">
    <ul>
      <table class="table">
        <thead class="tablehead table-primary">
          <tr>
            <th scope="col">#</th>
            <th scope="col">제목</th>
            <th scope="col">작성자</th>
            <th scope="col">작성 날짜</th>
            <th scope="col">상세 보기</th>
          </tr>
        </thead>
        <tbody class="table-group-divider">
          <tr v-for="(article, index) in store.articles" :key="article.pk">
            <td scope="row">{{ index + 1 }}</td>
            <td>{{ article.title }}</td>
            <td>{{ article.user.username }}</td>
            <td>{{ formatDate(article.created_at) }}</td>
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

const formatDate = (date) => {
  const formattedDate = new Date(date);
  const year = formattedDate.getFullYear();
  const month = (formattedDate.getMonth() + 1).toString().padStart(2, '0'); // Adding 1 because months are zero-based
  const day = formattedDate.getDate().toString().padStart(2, '0');
  return `${year}-${month}-${day}`;
};

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
.table tbody tr:hover {
  background-color: #3498db; /* Light gray background on hover */
}
</style>
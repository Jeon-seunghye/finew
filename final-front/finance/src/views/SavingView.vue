<template>
  <div id="nav">
    <h1>적금</h1>
    <hr>
    <div>
      <h3>검색</h3>
      <div>
        <select name="bank_name" id="bank_name">
          <option v-for="saving in savings" :key="saving.id">
            {{ saving.kor_co_nm }}
          </option>
        </select>
      </div>
      <div>
        <button>검색</button>
      </div>
    </div>
    <br>

    <div>
      <h1>목록</h1>
      <hr>
      <div v-for="saving in savings" :key="saving.id">
        <p>공시 제출일 : {{ saving.dcls_month }}</p>
        <p>금융회사명 : {{ saving.kor_co_nm }}</p>
        <p>상품명 : {{ saving.fin_prdt_nm }}</p>
        <button class="view-detail-button" @click="goDetail(saving.fin_prdt_cd)">게시글 상세 보기</button>
        <hr>
      </div>

    </div>
  </div>
</template>



<script setup>
  import { useArticleStore } from '@/stores/article.js'
  import { onMounted } from 'vue';
  import { useRouter } from 'vue-router';
  const store = useArticleStore()
  const router = useRouter()

  // 적금 정보 가져오기
  onMounted(() => {
    store.getSaving()
  })

  const savings = store.savings

  // 상세보기 페이지로 가즈아
  const goDetail = function (fin_prdt_cd) {
    router.push({name: 'savingdetail', params:{fin_prdt_cd:fin_prdt_cd}})
  }



</script>
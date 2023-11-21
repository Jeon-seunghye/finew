<template>
  <div id="nav">
    <h1>예금</h1>
    <hr>
    <div>
      <h3>검색</h3>
      <div>
        <select name="bank_name" id="bank_name">
          <option v-for="deposit in deposits" :key="deposit.id">
            {{ deposit.kor_co_nm }}
          </option>
        </select>
      </div>
      <div>
        <select name="save_term" id="save_term">
          <option>6</option>
          <option>12</option>
          <option>24</option>
          <option>36</option>
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
      <div v-for="deposit in deposits" :key="deposit.id">
        <p>공시 제출일 : {{ deposit.dcls_month }}</p>
        <p>금융회사명 : {{ deposit.kor_co_nm }}</p>
        <p>상품명 : {{ deposit.fin_prdt_nm }}</p>
        <button class="view-detail-button" @click="goDetail(deposit.fin_prdt_cd)">게시글 상세 보기</button>
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

  // 예금 정보 가져오기
  onMounted(() => {
    store.getDeposit()
  })

  const deposits = store.deposits

  // 상세보기 페이지로 가즈아
  const goDetail = function (fin_prdt_cd) {
    router.push({name: 'depositdetail', params:{fin_prdt_cd:fin_prdt_cd}})
  }



</script>
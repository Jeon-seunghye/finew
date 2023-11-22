<template>
  <div id="nav">
    <h1>예금</h1>
    <hr>
    <div>
      <h3>검색</h3>
      <div>
        <select v-model="selectedBank" name="bank_name" id="bank_name">
          <option v-for="bankName in setBankNames" :key="bankName">
            {{ bankName }}
          </option>
        </select>
      </div>
      <div>
        <button @click="search">검색</button>
      </div>
    </div>

    <br>

    <div>
      <h1>목록</h1>
      <hr>
      <div v-for="deposit in filteredDeposits" :key="deposit.id">
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
  import { onMounted, ref, computed } from 'vue';
  import { useRouter } from 'vue-router';
  const store = useArticleStore()
  const router = useRouter()

  // 예금 정보 가져오기
  onMounted(() => {
    store.getDeposit()
  })


  // 은행명 중복 제거
  const setBankNames = computed(() => {
    const bankNameSet = new Set()
    store.deposits.forEach(deposit => bankNameSet.add(deposit.kor_co_nm))
    return Array.from(bankNameSet)
  })


  // 검색에 사용되는 변수
  const selectedBank = ref('') // 선택된 은행명을 저장할 변수
  const filteredDeposits = ref([])  // 필터링된 예금을 저장할 배열
  // 검색하는 함수
  const search = function () {
    // 선택된 은행명에 맞는 예금상품만 필터링
    if (selectedBank.value !== '') {
      filteredDeposits.value = store.deposits.filter(deposit => deposit.kor_co_nm === selectedBank.value)
    } else {
      // 선택된 은행명이 없으면 모든 예금상품을 보여줌 (근데 그래도 검색 버튼은 눌러야 함.)
      filteredDeposits.value = store.deposits
    }
  }


  // 상세보기 페이지로 이동하는 함수
  const goDetail = function (fin_prdt_cd) {
    router.push({name: 'depositdetail', params: {fin_prdt_cd: fin_prdt_cd}})
  }


</script>

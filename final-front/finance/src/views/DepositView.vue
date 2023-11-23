<template>
  <div id="nav">
    <div class="contain">
      <a href="/deposit" class="headers1">예금</a>
      <a href="/saving" class="headers2">적금</a>
    </div>
    <hr>
    <div>
      <div class="form-group">
        <h3 style="margin-left: 60px;">은행 검색</h3>
      </div>
      <div class="contain2">
        <select v-model="selectedBank" name="bank_name" id="bank_name" class="form-control">
          <option v-for="bankName in setBankNames" :key="bankName">
            {{ bankName }}
          </option>
        </select>
        <button @click="search" class="btn btn-primary search">검색</button>
      </div>
    </div>

    <br>

    <div style="margin-inline: 40px; padding-inline: 50px;">
      <h1>목록</h1>
      <hr>
      <table class="table table-hover">
        <thead>
          <tr>
            <th>공시 제출일</th>
            <th>금융회사명</th>
            <th>상품명</th>
            <th></th>
          </tr>
        </thead>
        <tbody class="table-group-divider">
          <tr class="lineup" v-for="deposit in filteredDeposits" :key="deposit.id">
            <td>{{ deposit.dcls_month }}</td>
            <td>{{ deposit.kor_co_nm }}</td>
            <td>{{ deposit.fin_prdt_nm }}</td>
            <td>
              <button class="btn btn-secondary" style="opacity: 70%;" @click="goDetail(deposit.fin_prdt_cd)">게시글 상세 보기</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <p class="mb-0 bg-light text-center py-2" style="width: 100%; font-size: small;" >&copy; 2023 Finew All Rights Reserved. 본 사이트의 콘텐츠는 저작권법의 보호를 받는 바 무단 전재, 복사, 배포 등을 금합니다.</p>
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
    search()
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

<style>
  .headers1{
    color: #255580;
    font-weight: bold;
    margin-top: 50px;
    margin-bottom: 40px;
    display: flex;
    justify-content: center;
    font-size: xxx-large;
    margin-right: -100px;
  }
  .headers2{
    color: #255580;
    opacity: 50%;
    font-weight: bold;
    margin-top: 50px;
    margin-bottom: 40px;
    display: flex;
    justify-content: center;
    font-size: x-large;
    margin-left: -100px;
  }
  .contain2{
    display: flex;
    margin-left: 60px;
    margin-right: 60px;
    flex-direction: row;
  }

  .contain{
    display: flex;
    align-items: baseline;
    justify-content: space-evenly;
  }

  .search{
    margin-left: 30px;
    width: 100px;
  }
  tr th,
  tr td{
    text-align: center;
  }
</style>
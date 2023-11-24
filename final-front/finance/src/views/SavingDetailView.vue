<template>
  <div>
    <a class="icon-link icon-link-hover boardlist" style="--bs-link-hover-color-rgb: 25, 135, 84; margin-top: 20px; margin-left: 30px;" href="/saving">
      ← 적금 목록
      <svg class="bi" aria-hidden="true"></svg>
    </a>
    <div class="container">
      <div class="info-container">
        <h1 class="header">적금 상세</h1>
        <p><strong>공시 제출일 :</strong> {{ selectedSaving.dcls_month }}</p>
        <p><strong>금융회사명 :</strong> {{ selectedSaving.kor_co_nm }}</p>
        <p><strong>상품명 :</strong> {{ selectedSaving.fin_prdt_nm }}</p>
        <p><strong>상품 코드 :</strong> {{ fin_prdt_cd }}</p>
        <p><strong>가입 방법 :</strong> {{ selectedSaving.join_way }}</p>
        <p><strong>가입 대상 :</strong> {{ selectedSaving.join_member }}</p>
        <p><strong>우대 조건 :</strong> {{ selectedSaving.spcl_cnd }}</p>
        <p><strong>기타 유의사항 :</strong> {{ selectedSaving.etc_note }}</p>
      </div>
      <div class="option-container">
        <div v-for="(option, index) in selectedSaving.savingoption_set" :key="option.id" class="option-item">
          <h3 style="margin-left: 40px;">{{ index + 1 }}번 옵션</h3>
          <div class="option-details">
            <p><strong>저축 기간 :</strong> {{ option.save_trm }}개월</p>
            <p><strong>저축 금리 유형 :</strong> {{ option.intr_rate_type_nm }}</p>
            <p><strong>저축 금리 :</strong> {{ option.intr_rate }}[%]</p>
            <p><strong>최고 우대금리 :</strong> {{ option.intr_rate2 }}[%]</p>
            <button @click="store.addSavingCart(option.id)" class="option-button btn">
              {{ isAdded(option.id) ? '가입취소' : '가입하기' }}
            </button>
          </div>
          <hr class="option-divider">
        </div>
      </div>
    </div>
  </div>
  <p class="mb-0 bg-light text-center py-2" style="width: 100%; font-size: small;" >&copy; 2023 Finew All Rights Reserved. 본 사이트의 콘텐츠는 저작권법의 보호를 받는 바 무단 전재, 복사, 배포 등을 금합니다.</p>
</template>



<script setup>
  import axios from 'axios'
  import { useRoute, useRouter } from 'vue-router';
  import { useArticleStore } from '@/stores/article.js'
  import { ref, onMounted, computed } from 'vue';
  
  const store = useArticleStore()
  const route = useRoute()

  const fin_prdt_cd = ref(route.params.fin_prdt_cd)


  // 상품코드랑 같은 정보 갖고오기
  const selectedSaving = ref({})
  const getSelectedSaving = function () {
    const selectedThing = store.savings.find(data => data.fin_prdt_cd === fin_prdt_cd.value)
    if (selectedThing) {
      selectedSaving.value = selectedThing
    }
  }

  // 적금 정보 가져오기
  onMounted(() => {
    store.getSaving()
    getSelectedSaving()
    store.getFinancialProducts()
  })
  
  // 예금 가입 유무 확인
  const isAdded = function (optionId) {
    return store.financial_products.some(product => product.savings === optionId)
  }
  

</script>


<style scoped>
.container{
  font-family: 'Noto Sans KR', sans-serif; /* Noto Sans KR 글씨체 적용 */
  margin-top: 40px;
  display: flex;
}
.header {
  margin-bottom: 40px;
  color: #255580;
  font-weight: bold;
}

.info-container {
  margin-bottom: 20px;
  width: 400px;
}
.option-container {
  display: flex;
  flex-wrap: wrap;
  margin-top: 60px;
  margin-left: 70px;
}

.option-item {
  width: 50%;
  padding: 10px;
  box-sizing: border-box;
}

.option-details {
  margin-top: 20px;
  margin-bottom: 10px;
  margin-left: 40px;
}

.option-button {
  opacity: 70%;
  margin-left: 40px;
  padding: 8px 12px;
  background-color: #007bff;
  color: #fff;
  border: none;
  cursor: pointer;
  margin-top: 10px;
  margin-bottom: 10px;
  border-radius: 5px;
}

.option-divider {
  margin-top: 10px;
}


.btn:hover {
  background-color: #0056b3;
}
</style>
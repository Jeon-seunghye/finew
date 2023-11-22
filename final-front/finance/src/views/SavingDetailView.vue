<template>
  <div>
    <h1>적금 상세</h1>
    <div>
      <p>공시 제출일 : {{ selectedSaving.dcls_month }}</p>
      <p>금융회사명 : {{ selectedSaving.kor_co_nm }}</p>
      <p>상품명 : {{ selectedSaving.fin_prdt_nm }}</p>
      <p>상품 코드 : {{ fin_prdt_cd }}</p>
      <p>가입 방법 : {{ selectedSaving.join_way }}</p>
      <p>가입 대상 : {{ selectedSaving.join_member }}</p>
      <p>우대 조건 : {{ selectedSaving.spcl_cnd }}</p>
      <p>기타 유의사항 : {{ selectedSaving.etc_note }}</p>
    </div>
    <hr>
    <div v-for="(option, index) in selectedSaving.savingoption_set" :key="option.id">
      <h3>{{ index + 1 }}번 옵션</h3>
      <p>저축 기간 : {{ option.save_trm }}개월</p>
      <p>저축 금리 : {{ option.intr_rate }}[%]</p>
      <p>최고 우대금리 : {{ option.intr_rate2 }}[%]</p>
      <button @click="store.addSavingCart(option.id)">
        {{ isAdded(option.id) ? '가입취소' : '가입하기' }}
      </button>
      <hr>
    </div>
  </div>
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
</style>
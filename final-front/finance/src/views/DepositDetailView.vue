<template>
  <div>
    <h1>예금 상세</h1>
    <div>
      <p>공시 제출일 : {{ selectedDeposit.dcls_month }}</p>
      <p>금융회사명 : {{ selectedDeposit.kor_co_nm }}</p>
      <p>상품명 : {{ selectedDeposit.fin_prdt_nm }}</p>
      <p>상품 코드 : {{ fin_prdt_cd }}</p>
      <p>가입 방법 : {{ selectedDeposit.join_way }}</p>
      <p>가입 대상 : {{ selectedDeposit.join_member }}</p>
      <p>우대 조건 : {{ selectedDeposit.spcl_cnd }}</p>
      <p>기타 유의사항 : {{ selectedDeposit.etc_note }}</p>
    </div>
    <hr>
    <div v-for="(option, index) in selectedDeposit.depositoption_set" :key="option.id">
      <h3>{{ index + 1 }}번 옵션</h3>
      <p>저축 기간 : {{ option.save_trm }}개월</p>
      <p>저축 금리 : {{ option.intr_rate }}[%]</p>
      <p>최고 우대금리 : {{ option.intr_rate2 }}[%]</p>
      <button @click="addCart(`${selectedDeposit.fin_prdt_nm} (${option.save_trm})`)">가입하기</button>
      <hr>
    </div>

  </div>
</template>



<script setup>
  import { useRoute, useRouter } from 'vue-router';
  import { useArticleStore } from '@/stores/article.js'
  import { ref, onMounted } from 'vue';
  const store = useArticleStore()
  const route = useRoute()

  const fin_prdt_cd = ref(route.params.fin_prdt_cd)

  // 예금 정보 가져오기
  onMounted(() => {
    store.getDeposit()
    getSelectedDeposit()
  })
  
  const deposits = store.deposits
  
  // 이제 상품코드랑 같은 정보 갖고오기
  const selectedDeposit = ref({})
  const getSelectedDeposit = function () {
    const selectedThing = deposits.find(data => data.fin_prdt_cd === fin_prdt_cd.value)
    if (selectedThing) {
      selectedDeposit.value = selectedThing
    }
  }

  // 가입하기(financial_product 필드에 추가 -> `${selectedDeposit.fin_prdt_nm} (${option.save_trm})`)
  const addCart = function (product) {
    
  }

</script>


<style scoped>
</style>
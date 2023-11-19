<template>
  <div>
    <h1>환율 계산기</h1>

    <div style="text-align: center;">
      <label for="selectTemp">화폐? 선택:</label>
      <select id="selectTemp" v-model="selectedTemp" @change="setSelectedTemp(selectedTemp)">
        <option v-for="exchange_rate1 in exchange_rates" :key="exchange_rate1.id">
          {{ exchange_rate1.cur_unit }} : {{ exchange_rate1.cur_nm }}
        </option>
      </select>
      <input type="number" placeholder="입력" v-model="inputTemp">
      

      <h3>확인용</h3>
      <p>입력 화폐 : {{ selectedTemp }}</p>
      <p>입력 값 : {{ inputTemp }}</p>
      <p>팔 때 : {{ selectedTts }}</p>
      <p>살 때 : {{ selectedTtb }}</p>

    
    </div>

  </div>
</template>



<script setup>

  import { ref } from 'vue';
  import { useArticleStore } from '@/stores/article.js'
  import { onMounted } from 'vue';
  const store = useArticleStore()

  // 환율 정보 onMounted로 가져오기
  onMounted(() => {
    store.getExchangeRate()
  })
  
  // 환율 전체 정보
  const exchange_rates = store.exchange_rates

  // 선택한 것
  const selectedTemp = ref(null)
  // 선택한 것 업데이트
  const setSelectedTemp = function (currency) {
    selectedTemp.value = currency
    getTtsTtb()
  }


  // 선택한 것의 tts
  const selectedTts = ref(null)
  // 선택한 것의 ttb
  const selectedTtb = ref(null)
  // 선택한 것의 tts, ttb 갖고오는 함수
  const getTtsTtb = function () {
    const selectedCurrency = exchange_rates.find(rate => `${rate.cur_unit} : ${rate.cur_nm}` === selectedTemp.value);
    console.log(selectedCurrency)
    if (selectedCurrency) {
      selectedTts.value = selectedCurrency.tts;
      selectedTtb.value = selectedCurrency.ttb;
    }
  };

  // 입력한 금액?
  const inputTemp = ref(null)
  // 환율 계산하는 함수 (이어서 만들기)
  const calculateExchange = function () {}





</script>







<style scoped>
</style>
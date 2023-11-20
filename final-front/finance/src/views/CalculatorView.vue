<template>
  <div>
    <h1>환율 계산기</h1>

    <div style="text-align: center;">
      <label for="selectTemp1">기존 : </label>
      <select id="selectTemp1" v-model="selectedTemp1" @change="setSelectedTemp1(selectedTemp1)">
        <option v-for="exchange_rate1 in exchange_rates" :key="exchange_rate1.id">
          {{ exchange_rate1.cur_unit }} : {{ exchange_rate1.cur_nm }}
        </option>
      </select>
    </div>

    <div style="text-align: center;">
      <label for="selectTemp2">변경 : </label>
      <select id="selectTemp2" v-model="selectedTemp2" @change="setSelectedTemp2(selectedTemp2)">
        <option v-for="exchange_rate2 in exchange_rates" :key="exchange_rate2.id">
          {{ exchange_rate2.cur_unit }} : {{ exchange_rate2.cur_nm }}
        </option>
      </select>
    </div>
    
    <div style="text-align: center;">
      <input type="number" placeholder="입력" v-model="inputTemp" @input="calculateExchange">
      <h1>{{ result.toFixed(2) }}</h1>
    </div>
  </div>
</template>



<script setup>

  import { ref } from 'vue';
  import { useArticleStore } from '@/stores/article.js'
  import { onMounted } from 'vue';
  import { parseExpression } from '@babel/parser';
  const store = useArticleStore()

  // 환율 정보 onMounted로 가져오기
  onMounted(() => {
    store.getExchangeRate()
  })
  
  // 환율 전체 정보
  const exchange_rates = store.exchange_rates
  // 입력한 금액?
  const inputTemp = ref()
  // 환전 금액
  const result = ref(0)

///////////////////////////////////////////////

  // 선택한 것1
  const selectedTemp1 = ref(null)
  // 선택한 것 업데이트1
  const setSelectedTemp1 = function (currency) {
    selectedTemp1.value = currency
    getDealBasRate1()
    inputTemp.value = null
    result.value = 0

  }

  // 선택한 것의 deal_bas_rate1
  let selected_deal_bas_rate_1 = ref(0)

  // 선택한 것의 deal_bas_rate 갖고오는 함수1
  const getDealBasRate1 = function () {
    const selectedCurrency = exchange_rates.find(rate => `${rate.cur_unit} : ${rate.cur_nm}` === selectedTemp1.value);
    console.log(selectedCurrency)
    if (selectedCurrency) {
      if (selectedCurrency.cur_unit.includes('(100)')) {
        selected_deal_bas_rate_1.value = parseFloat(selectedCurrency.deal_bas_r.replace(/,/g, '')) / 100
      } else {
        selected_deal_bas_rate_1.value = parseFloat(selectedCurrency.deal_bas_r.replace(/,/g, ''))
      }
    }
  };


///////////////////////////////////////////////////////////////////////

  // 선택한 것2
  const selectedTemp2 = ref(null)
  // 선택한 것 업데이트2
  const setSelectedTemp2 = function (currency) {
    selectedTemp2.value = currency
    getDealBasRate2()
    inputTemp.value = null
    result.value = 0

  }

  // 선택한 것의 deal_bas_rate2
  let selected_deal_bas_rate_2 = ref(0)

  // 선택한 것의 deal_bas_rate 갖고오는 함수2
  const getDealBasRate2 = function () {
    const selectedCurrency = exchange_rates.find(rate => `${rate.cur_unit} : ${rate.cur_nm}` === selectedTemp2.value);
    console.log(selectedCurrency)
    if (selectedCurrency) {
      if (selectedCurrency.cur_unit.includes('(100)')) {
        selected_deal_bas_rate_2.value = parseFloat(selectedCurrency.deal_bas_r.replace(/,/g, '')) / 100
      } else {
        selected_deal_bas_rate_2.value = parseFloat(selectedCurrency.deal_bas_r.replace(/,/g, ''))
      }
    }
  };
  
///////////////////////////////////////////////////////////////////////

  // 계산하는 함수
  const calculateExchange = function () {
    console.log(selected_deal_bas_rate_1.value)
    console.log(selected_deal_bas_rate_2.value)
    const calIng = selected_deal_bas_rate_1.value / selected_deal_bas_rate_2.value
    console.log(calIng)
    result.value = inputTemp.value * calIng
  }
</script>







<style scoped>
</style>
<template>
  <div class="container">
    <h1 class="headers">환율 계산기</h1>
    <hr>
    <div class="wraping">
      <div class="cover">
        <div class="selecting">
          <div class="lefting">
            <label for="selectTemp1">기존 화폐</label>
          </div>
          <div class="input-select-wrapper">
            <input type="number" placeholder="입력" v-model="inputTemp" style="width:64%;" @input="calculateExchange">
            <select id="selectTemp1" v-model="selectedTemp1" @change="setSelectedTemp1(selectedTemp1)">
              <option v-for="exchange_rate1 in exchange_rates" :key="exchange_rate1.id">
                {{ exchange_rate1.cur_unit }} : {{ exchange_rate1.cur_nm }}
              </option>
            </select>
          </div>
        </div>
      </div>

      <div class="cover">
        <div class="selecting">
          <div class="lefting">
            <label for="selectTemp2">환전할 화폐</label>
          </div>
          <div class="input-select-wrapper">
            <p class="result">{{ result.toFixed(2) }}</p>
            <select id="selectTemp2" v-model="selectedTemp2" @change="setSelectedTemp2(selectedTemp2)">
              <option v-for="exchange_rate2 in exchange_rates" :key="exchange_rate2.id">
                {{ exchange_rate2.cur_unit }} : {{ exchange_rate2.cur_nm }}
              </option>
            </select>
          </div>
        </div>
      </div>
    </div>
    
  </div>
  <p class="mb-0 bg-light text-center py-2 fixed-bottom" style="width: 100%; font-size: small;" >&copy; 2023 Finew All Rights Reserved. 본 사이트의 콘텐츠는 저작권법의 보호를 받는 바 무단 전재, 복사, 배포 등을 금합니다.</p>

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

.wraping{
  margin-top: 20px;
  background-color: whitesmoke;
  padding: 10px;
  border-radius: 10px;
}
.headers{
  color: #255580;
  font-weight: bold;
  margin-top: 40px;
  margin-bottom: 20px;
}
.container{
  font-family: 'Noto Sans KR', sans-serif; /* Noto Sans KR 글씨체 적용 */
  margin-top: 20px;
}

.cover{
  margin-block: 10px;
  margin: 20px;
  text-align: center;
}
.selecting{
  margin-bottom: 20px;
}

.lefting{
  display: flex;
}

.input-select-wrapper {
  display: flex;
  align-items: center;
  border: 1px solid black;
  border-radius: 5px;
  justify-content: space-between;
  margin-top: 10px;
  margin-left: 20px;
  margin-right: 30px;
  height: 40px;
  background-color: white;

}

.input-select-wrapper input {
  margin-left: 10px;
  padding: 5px;
  border: 1px;
}

.input-select-wrapper p {
  margin-right: 10px;
  margin-left: 10px;
  text-align: left;
  padding: 5px;
  width: 150px;
  border: 1px;
}

.input-select-wrapper select {
  padding: 5px;
  width: 228px;
  border: 1px;
}

.result {
  font-weight: bold;
  margin-top: 10px;
  font-size: 18px;
}
</style>
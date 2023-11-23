<template>
    <div>
        <h2 style="font-weight:bold; text-align:left;">- 가입 상품 금리</h2>
        
        <h2 style="margin-top: 40px; font-weight: bold;">예금 금리</h2>
        <div style="width:100%;">
            <canvas ref="depositChartCanvas"></canvas>
        </div>
        <h2 style="margin-top: 50px; font-weight: bold;">적금 금리</h2>
        <div style="width:100%">
            <canvas ref="savingChartCanvas"></canvas>
        </div>
        <!-- <div v-for="i in deposit_b_name.length" :key="i">
            <p>{{ deposit_b_name[i-1] }}</p>
            <p>{{ deposit_rate1[i-1] }}</p>
            <p>{{ deposit_rate2[i-1] }}</p>
        </div>
        <div v-for="i in saving_b_name.length" :key="i">
            <p>{{ saving_b_name[i-1] }}</p>
            <p>{{ saving_rate1[i-1] }}</p>
            <p>{{ saving_rate2[i-1] }}</p>
        </div> -->
    </div>
  </template>
  
  <script setup>
    import { ref, onMounted } from 'vue';
    import { useRoute, useRouter } from 'vue-router';
    import { RouterView } from 'vue-router';
    import axios from 'axios';
    import { useArticleStore } from '@/stores/article';
    import Chart from 'chart.js/auto';
  
    const router = useRouter();
    const route = useRoute();
    const store = useArticleStore();
    const deposit_b_name = ref([]);
    const deposit_rate1 = ref([]);
    const deposit_rate2 = ref([]);
    const saving_b_name = ref([]);
    const saving_rate1 = ref([]);
    const saving_rate2 = ref([]);
    const deposit_fin_prdt_nm = ref([]);
    const saving_fin_prdt_nm = ref([]);
    
    const depositChartCanvas = ref(null);
    const savingChartCanvas = ref(null);
  
    onMounted(() => {
        for(let i=0; i<store.deposits.length; i++){
            for(let j=0; j<store.financial_products.length; j++){
                if(store.deposits[i].depositoption_set[j]){
                  for (let k = 0; k < store.financial_products.length; k++) {
                    if(store.deposits[i].depositoption_set[j].id === store.financial_products[k].deposits){
                      deposit_b_name.value.push(store.deposits[i].kor_co_nm)
                      deposit_rate1.value.push(store.deposits[i].depositoption_set[j].intr_rate)
                      deposit_rate2.value.push(store.deposits[i].depositoption_set[j].intr_rate2)
                      deposit_fin_prdt_nm.value.push(store.deposits[i].fin_prdt_nm)
                    }
                  }
                }
            }
        }
        for(let i=0; i<store.savings.length; i++){
          for(let j=0; j<store.financial_products.length; j++){
            if(store.savings[i].savingoption_set[j]){
              for (let k = 0; k < store.financial_products.length; k++) {
  
  
              if(store.savings[i].savingoption_set[j].id === store.financial_products[k].savings){
                saving_b_name.value.push(store.savings[i].kor_co_nm)
                saving_rate1.value.push(store.savings[i].savingoption_set[j].intr_rate)
                saving_rate2.value.push(store.savings[i].savingoption_set[j].intr_rate2)
                saving_fin_prdt_nm.value.push(store.savings[i].fin_prdt_nm)
              }
            }
            }
            }
          }
          
            const depositChartData = {
              labels: deposit_fin_prdt_nm.value,
              datasets: [
                {
                  label: '일반 금리',
                  data: deposit_rate1.value,
                  backgroundColor: 'rgba(255, 99, 132, 0.2)',
                  borderColor: 'rgba(255,99,132,1)',
                  borderWidth: 1,
                },
                {
                  label: '최고 우대 금리',
                  data: deposit_rate2.value,
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            borderColor: 'rgba(54, 162, 235, 1)',
            borderWidth: 1,
          },
        ],
      };
      
      const savingChartData = {
        labels: saving_fin_prdt_nm.value,
        datasets: [
          {
            label: '일반 금리',
            data: saving_rate1.value,
            backgroundColor: 'rgba(255, 206, 86, 0.2)',
            borderColor: 'rgba(255, 206, 86, 1)',
            borderWidth: 1,
          },
          {
            label: '최고 우대 금리',
            data: saving_rate2.value,
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1,
          },
        ],
      };
      if (depositChartCanvas.value) {
        const depositCtx = depositChartCanvas.value.getContext('2d');
        new Chart(depositCtx, {
          type: 'bar',
          data: depositChartData,
          options: {
            // Add any options specific to your chart
          },
        });
      }
      
      if (savingChartCanvas.value) {
        const savingCtx = savingChartCanvas.value.getContext('2d');
        new Chart(savingCtx, {
          type: 'bar',
          data: savingChartData,
          options: {
            // Add any options specific to your chart
          },
        });
      }
    })
    
  </script>
  
  <style scoped>
  
  </style>
  
  
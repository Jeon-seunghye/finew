<template>
    <div class="container">
        <h1 class="headers">추천목록</h1>
        <a href="/compare">→ 비교하러 가기</a>
        <hr>
        <div style="margin-bottom:10px;" v-for="i in selectedProducts.length" :key="i">
          <li>{{ selectedProducts[i-1] }}</li>
        </div>
        <p class="mb-0 bg-light text-center py-2 fixed-bottom" style="width: 100%; font-size: small;" >&copy; 2023 Finew All Rights Reserved. 본 사이트의 콘텐츠는 저작권법의 보호를 받는 바 무단 전재, 복사, 배포 등을 금합니다.</p>
    </div>
</template>



<script setup>
  import { ref, onMounted } from 'vue';
  import { useRoute, useRouter } from 'vue-router';
  import axios from 'axios';
  import { useArticleStore } from '@/stores/article';
  const router = useRouter();
  const route = useRoute();
  const store = useArticleStore();



  //  선택된 상품을 담을 변수
   const selectedProducts = ref([]);

  // onMounted 내부에서 상품 추천 받기 로직을 실행
  onMounted(() => {

    // 상품 추천 받기 로직 (예금)
      for (let i = 0; i < store.deposits.length; i++) {        
        for (let j = 0; j < store.deposits[i].depositoption_set.length; j++) {
          if (
            store.deposits[i].join_way.includes(store.users.value.join_way) &&
            store.deposits[i].kor_co_nm === store.users.value.kor_co_nm &&
            store.deposits[i].depositoption_set[j].intr_rate_type_nm === store.users.value.intr_rate_type_nm
          ) {
            selectedProducts.value.push(`${store.deposits[i].kor_co_nm} : ${store.deposits[i].fin_prdt_nm} - ${store.deposits[i].depositoption_set[j].save_trm}개월`)
          }
        }
      }

    // 상품 추천 받기 로직 (적금)
      for (let i = 0; i < store.savings.length; i++) {        
        for (let j = 0; j < store.savings[i].savingoption_set.length; j++) {
          if (
            store.savings[i].join_way.includes(store.users.value.join_way) &&
            store.savings[i].kor_co_nm === store.users.value.kor_co_nm &&
            store.savings[i].savingoption_set[j].intr_rate_type_nm === store.users.value.intr_rate_type_nm
          ) {
            selectedProducts.value.push(`${store.savings[i].kor_co_nm} : ${store.savings[i].fin_prdt_nm} - ${store.savings[i].savingoption_set[j].save_trm}개월`)
          }
        }
      }
             
  });

  console.log(selectedProducts.value)
  
  // // 콘솔 확인
  //   console.log(store.users)
  //   console.log(store.users.nickname)
  //   console.log(store.users.value.kor_co_nm)
  //   console.log(store.users.value.join_way)
  //   console.log(store.users.value.intr_rate_type_nm)

  //   // console.log(store.deposits)
  //   console.log(store.deposits[0].kor_co_nm)
  //   console.log(store.deposits[0].join_way)
  //   console.log(store.deposits[0].depositoption_set[0].intr_rate_type_nm)
  // //
  
</script>


<style scoped>
.headers{
  color: #255580;
  font-weight: bold;
  margin-top: 40px;
  margin-bottom: 30px;
}
.container{
  font-family: 'Noto Sans KR', sans-serif; /* Noto Sans KR 글씨체 적용 */
  margin-top: 20px;
}
</style>
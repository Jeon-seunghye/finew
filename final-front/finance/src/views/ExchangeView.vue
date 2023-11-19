<template>
  <div>
    <h1>환율 계산기</h1>
    <div>
      <select name="contry" id="contry">
        <option value=""></option>
      </select>
    </div>
  </div>
</template>



<script setup>
  import { ref } from 'vue';
  import { useArticleStore } from '@/stores/article.js'
  import { onMounted } from 'vue';


  const store = useArticleStore()

  const selectCurrency = ref(null)
  
  onMounted(() => {
  store.getExchangeRate()
})


</script>







<style scoped>
</style>
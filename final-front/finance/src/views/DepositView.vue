<template>
  <div id="nav">
    <h1>예금</h1>

    <div>
      <h3>검색</h3>
      <div>
        <select name="bank_name" id="bank_name">
          <!-- <option v-for="deposit_base in deposit_bases" :key="deposit_bases.id">
            {{ deposit_base.dcls_month }} -->
          <!-- </option> -->
        </select>
      </div>
      <div>
        <select name="save_term" id="save_term">
          <option>

          </option>
        </select>
      </div>
      <div>
        <button>검색</button>
      </div>
    </div>

  </div>
</template>



<script setup>
  import { useArticleStore } from '@/stores/article.js'
  import { onMounted } from 'vue';

  const store = useArticleStore()

  // 예금 정보 가져오기
  onMounted(() => {
    store.getDeposit()
  })

  const deposit_bases = store.deposit_bases
  // const deposit_options = store.deposit_option
  console.log(deposit_bases)
  // console.log(deposit_options)



</script>
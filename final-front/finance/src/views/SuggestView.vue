<template>
    <div>
        <h1>추천목록</h1>
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

  console.log(store.users)
  console.log(store.users.nickname)
</script>









<style scoped>

</style>
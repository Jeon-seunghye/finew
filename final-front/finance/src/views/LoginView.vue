<template>
  <div>
    <div class="container">
      <h2>LOGIN</h2>
      <form @submit.prevent="signIn" >
        <div class="box">
            <label for="username">username &nbsp</label>
            <input type="text" id="username" v-model.trim="username">
        </div>
        <div class="box">
            <label for="password">password &nbsp</label>
            <input type="password" id="password" v-model.trim="password">
        </div>
        <div class="box" style=" text-align: center;">
          <input type="submit" style="display: inline-block;" value="LOGIN">
        </div>
      </form>
    </div>
  </div>
  <p class="mb-0 bg-light text-center py-2 fixed-bottom" style="width: 100%; font-size: small;" >&copy; 2023 Finew All Rights Reserved. 본 사이트의 콘텐츠는 저작권법의 보호를 받는 바 무단 전재, 복사, 배포 등을 금합니다.</p>

</template>



<script setup>
  import { ref } from 'vue';
  import { useArticleStore } from '@/stores/article'

  const store = useArticleStore()

  const username = ref(null)
  const password = ref(null)

  const signIn = function () {
      const payload = {
          username: username.value,
          password: password.value
      }
      store.signIn(payload)
  }

</script>



<style scoped>
  .container{
    background-color: whitesmoke;
    width:100%;
    height:100%;
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
    margin-top: 100px;
    margin: 100px auto;
    border: 2px solid lightgray;
    border-radius: 10px;
    padding-top: 20px;
    padding-bottom: 20px;
    
  }
  
  .box{
    margin-top: 10px;
  }
</style>
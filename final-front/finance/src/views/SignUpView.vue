<template>
  <div class="container">
      <h2>SIGN UP</h2>
      <form @submit.prevent="signUp">
          <div class="box">
            <!-- <label for="username">username :&nbsp</label> -->
            <input type="text" id="username" v-model.trim="username" placeholder="아이디 입력">
          </div>
          <div class="box">
            <!-- <label for="password1">password : &nbsp</label> -->
            <input type="password" id="password1" v-model.trim="password1" placeholder="비밀번호">
          </div>
          <div class="box">
            <!-- <label for="password2">password Confirmation : </label> -->
            <input type="password" id="password2" v-model.trim="password2" placeholder="비밀번호 재입력">
          </div>
          <div class="box">
            <input type="email" id="email" v-model.trim="email" placeholder="이메일">
          </div>
          <div class="box">
            <input type="nickname" id="nickname" v-model.trim="nickname" placeholder="닉네임">
          </div>
          <div class="box">
            <input type="age" id="age" v-model.trim="age" placeholder="나이">
          </div>
          <div class="box">
            <input type="money" id="money" v-model.trim="money" placeholder="잔고">
          </div>
          <div class="box">
            <input type="salary" id="salary" v-model.trim="salary" placeholder="연봉">
          </div>
          <div class="box" style=" text-align: center;">
          <input type="submit" style="display: inline-block;" value="가입하기">
        </div>
      </form>
  </div>
</template>



<script setup>
  import {ref} from 'vue'
  import { useArticleStore } from '@/stores/article'

  const store = useArticleStore()

  const username = ref(null)
  const password1 = ref(null)
  const password2 = ref(null)
  const email = ref('')
  const age = ref(null)
  const money = ref(null)
  const salary = ref(null)
  const nickname = ref(null)

  const signUp = function () {
      const payload = {
          username: username.value,
          password1: password1.value,
          password2: password2.value,
          email: email.value,
          age: age.value,
          money: money.value,
          salary: salary.value,
          nickname: nickname.value,
      }
      store.signUp(payload)
  }
</script>


<style scoped>
  .container{
    background-color: whitesmoke ;
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
    padding-top: 2px;
    padding-bottom: 2px;
  }
</style>
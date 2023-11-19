<template>
  <div class="container">
    <h2>회원 정보 수정</h2>
    <form @submit.prevent="updateMember">
      <div class="box">
        <label for="email">이메일: {{ store.username }}</label>
        <input type="email" id="email" v-model.trim="email" placeholder="이메일 입력">
      </div>
      <div class="box">
        <label for="nickname">닉네임:</label>
        <input type="text" id="nickname" v-model.trim="nickname" placeholder="닉네임 입력">
      </div>
      <div class="box">
        <label for="age">나이: &nbsp&nbsp</label>
        <input type="number" id="age" v-model.trim="age" placeholder="나이 입력">
      </div>
      <div class="box">
        <label for="money">잔고: &nbsp&nbsp</label>
        <input type="number" id="money" v-model.trim="money" placeholder="잔고 입력">
      </div>
      <div class="box">
        <label for="salary">연봉: &nbsp&nbsp</label>
        <input type="number" id="salary" v-model.trim="salary" placeholder="연봉 입력">
      </div>
      <div class="box" style="text-align: center;">
        <input type="submit" style="display: inline-block;" value="회원 정보 수정">
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useArticleStore } from '@/stores/article'

const store = useArticleStore()

const username = ref('')
const email = ref('')
const nickname = ref('')
const age = ref(null)
const money = ref(null)
const salary = ref(null)

// // 회원 정보를 가져오고 필드의 초기 값을 설정하는 메소드가 있다고 가정합니다.
// const fetchMemberInfo = async () => {
//   const memberInfo = await store.fetchMemberInfo() // 이 메소드는 스토어에서 구현해야 합니다.
//   username.value = memberInfo.username
//   email.value = memberInfo.email
//   nickname.value = memberInfo.nickname
//   age.value = memberInfo.age
//   money.value = memberInfo.money
//   salary.value = memberInfo.salary
// }

const updateMember = async () => {
  const memberData = {
    username: username.value,
    email: email.value,
    nickname: nickname.value,
    age: age.value,
    money: money.value,
    salary: salary.value,
  }
  await store.updateMember(memberData) // 이 메소드도 스토어에서 구현해야 합니다.
}
</script>

<style scoped>
.container {
  background-color: whitesmoke;
  width: 100%;
  height: 100%;
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

.box {
  margin-top: 10px;
  padding-top: 2px;
  padding-bottom: 2px;
}
</style>

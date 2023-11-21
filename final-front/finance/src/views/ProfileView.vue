<template>
  <main>
    <h1>프로필</h1>
    <!-- 사용자 정보 출력 -->
    <p>이름: {{ user.username }}</p>
    <p>나이: {{ user.age }}</p>
    <p>이메일: {{ user.email }}</p>
    <p>닉네임: {{ user.nickname }}</p>
    <p>연봉: {{ user.salary }}</p>
    <p>자산: {{ user.money }}</p>
    <p>가입한 상품: {{ user.financial_product }}</p>
    <!-- 기타 필요한 사용자 정보를 출력 -->

    <!-- 프로필 수정 버튼 -->
    <button @click="toggleProfileForm" class="delete-button">프로필 수정</button>

    <!-- 프로필 수정 폼 -->
    <form v-if="isProfileFormVisible" @submit.prevent="submitProfileForm" class="edit">
      <label for="newNick">새로운 닉네임:</label>
      <input id="newNick" v-model="newNick" />
      <label for="newAge">새로운 나이:</label>
      <input id="newAge" type="number" v-model="newAge" />
      <label for="newEmail">새로운 이메일:</label>
      <input id="newEmail" v-model="newEmail" />
      <label for="newSalary">새로운 연봉:</label>
      <input id="newSalary" v-model="newSalary" />
      <label for="newMoney">새로운 자산:</label>
      <input id="newMoney" v-model="newMoney" />

      <button type="submit">저장</button>
    </form>
  </main>
</template>

<script setup>
  import { ref , onMounted} from 'vue';
  import { useArticleStore } from '@/stores/article';

  const store = useArticleStore();
  const isProfileFormVisible = ref(false);
  const newNick = ref('');
  const newAge = ref('');
  const newEmail = ref('')
  const newSalary = ref('')
  const newMoney = ref('')


  onMounted(()=> {
    store.getUsers()
  })

  const user = store.users

  // 프로필 수정 버튼 클릭 시 폼 토글
  const toggleProfileForm = () => {
    isProfileFormVisible.value = !isProfileFormVisible.value;
  };

  // 프로필 수정 폼 제출 시 호출되는 함수
  const submitProfileForm = () => {
    // 간단한 유효성 검사
    if (newNick === '' || newAge === '' || newEmail === '' || newSalary === '' || newMoney === '') {
      alert('새로운 사용자 이름과 나이를 입력하세요.');
      return;
    }
  
  // 서버에 사용자 정보 업데이트 요청
  store.updateUsers({
    nickname: newNick,
    age: newAge,
    email: newEmail,
    money : newMoney,
    salary : newSalary,
  });

  // 폼 초기화
  newNick.value = '';
  newAge.value = '';
  newEmail.value = '';
  newMoney.value = '';
  newSalary.value = '';
  // 폼 숨기기
  isProfileFormVisible.value = false;
};
</script>

<style scoped>

.edit{
  display: flex;
  flex-direction: column;
  width: 30%;

}

</style>

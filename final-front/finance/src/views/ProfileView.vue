<!-- <template>
  <main>
    <h1>프로필</h1>
    <p>나이 : {{ store.data }}</p>
    <button @click="updateProfile" class="delete-button">프로필 수정</button>
  </main>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useArticleStore } from '@/stores/article';

const store = useArticleStore();
const user = ref({})
const updateProfile = function (payload) {
  const { username, email, age, money, salary, nickname } = payload;
  axios({
    method: 'put',  // Assuming you want to use the PUT method for updating the profile
    url: `${store.API_URL}/accounts/profile/`,
    data: {
      username,
      email,
      age,
      money,
      salary,
      nickname,
    },
    headers: {
      Authorization: `Token ${token.value}`,
    },
  })
    .then((response) => {
      console.log(response.data);
      // Update the local token if necessary
      token.value = response.data.key;
      // Redirect to the home page or another appropriate route
      router.push({ name: 'home' });
    })
    .catch((error) => {
      console.log(error);
    });
};


</script>

<style scoped>
</style> -->

<template>
  <main>
    <h1>프로필</h1>

    <!-- 사용자 정보 출력 -->
    <p>이름: {{ user.username }}</p>
    <p>나이: {{ user.age }}</p>
    <p>이메일: {{ user.email }}</p>
    <!-- 기타 필요한 사용자 정보를 출력 -->

    <!-- 프로필 수정 버튼 -->
    <button @click="toggleProfileForm" class="delete-button">프로필 수정</button>

    <!-- 프로필 수정 폼 -->
    <form v-if="isProfileFormVisible" @submit.prevent="submitProfileForm">
      <label for="newUsername">새로운 사용자 이름:</label>
      <input id="newUsername" v-model="newUsername" />
      <label for="newAge">새로운 나이:</label>
      <input id="newAge" type="number" v-model="newAge" />
      <!-- 기타 필요한 수정할 필드들을 추가 -->
      <button type="submit">저장</button>
    </form>
  </main>
</template>

<script setup>
import { ref } from 'vue';
import { useArticleStore } from '@/stores/article';

const store = useArticleStore();
const isProfileFormVisible = ref(false);
const newUsername = ref('');
const newAge = ref('');

const user = ref({}); // Assuming you have a user object in the store

// 프로필 수정 버튼 클릭 시 폼 토글
const toggleProfileForm = () => {
  isProfileFormVisible.value = !isProfileFormVisible.value;
};

// 프로필 수정 폼 제출 시 호출되는 함수
const submitProfileForm = () => {
  // 간단한 유효성 검사
  if (newUsername.trim() === '' || newAge === '') {
    alert('새로운 사용자 이름과 나이를 입력하세요.');
    return;
  }

  // 서버에 사용자 정보 업데이트 요청
  store.updateProfile({
    username: newUsername,
    age: newAge,
    // 다른 필요한 필드들을 추가로 전달할 수 있습니다.
  });

  // 폼 초기화
  newUsername.value = '';
  newAge.value = '';
  // 폼 숨기기
  isProfileFormVisible.value = false;
};
</script>

<style scoped>
/* 추가적인 스타일을 필요에 따라 추가하세요 */
</style>

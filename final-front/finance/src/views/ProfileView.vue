<template>
  <main>
    <div class="title">
      <p>회 원 정 보 수 정</p>
    </div>
    <div class="profile-container">
      <form @submit.prevent="updateUser" class="edit">
        <table class="table">
          <tbody>
            <tr>
              <td><label for="newNick">닉네임</label></td>
              <td><input v-model.trim="user.nickname" id="newNick" /></td>
            </tr>
            <tr>
              <td><label for="newAge">나이</label></td>
              <td><input v-model.trim="user.age" id="newAge" /></td>
            </tr>
            <tr>
              <td><label for="newEmail">이메일</label></td>
              <td><input v-model.trim="user.email" id="newEmail" /></td>
            </tr>
            <tr>
              <td><label for="newSalary">연봉</label></td>
              <td><input v-model.trim="user.salary" id="newSalary" /></td>
            </tr>
            <tr>
              <td><label for="newMoney">자산</label></td>
              <td><input v-model.trim="user.money" id="newMoney" /></td>
            </tr>
            <tr>
              <td colspan="2">
                <p>가입한 상품: {{ store.financial_products }}</p>
              </td>
            </tr>
          </tbody>
        </table>
        <div class="form-row center">
          <button class="buttons" type="submit">저장</button>
        </div>
      </form>
    </div>
  </main>
</template>

<script setup>
  import { ref, onMounted } from 'vue';
  import { useRoute, useRouter } from 'vue-router';
  import axios from 'axios';
  import { useArticleStore } from '@/stores/article';

  const router = useRouter();
  const route = useRoute();
  const store = useArticleStore();
  const user = ref({ nickname: '', age: '' , email: '' , salary: '' , money: ''});

  onMounted(() => {
    axios
      .get(`${store.API_URL}/user/user/`, {
        headers: {
          Authorization: `Token ${store.token}`,
        },
      })
      .then((res) => {
        user.value = res.data;
      })
      .catch((err) => {
        console.error(err);
      });
    store.getFinancialProducts()
  });

  const updateUser = () => {
    axios
      .put(
        `${store.API_URL}/user/user/`,
        {
          nickname: user.value.nickname,
          age: user.value.age,
          email: user.value.email,
          salary: user.value.salary,
          money: user.value.money,
        },
        {
          headers: {
            Authorization: `Token ${store.token}`,
          },
        }
      )
      .then(() => {
        alert('프로필이 업데이트 되었습니다.');
        router.push({ name: 'profile' });
      })
      .catch((err) => {
        console.log(err)
        alert('프로필 수정이 불가능합니다.');
        router.push({ name: 'profile' });
      });
  };

</script>



<style scoped>

  .table{
    margin-left: 20px;
    border-top: 1px solid lightgray;
  }
  form{
    text-align: center;
  }
  .profile-container {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    margin-top: 100px;
    
  }
  .buttons{
    border: 1px solid lightgray;
    background-color: whitesmoke;
    border-radius: 10%;
  }

  .edit {
    border-collapse: collapse;
    width: 80%;
  }

  .edit td {
    padding: 10px;
  }

  .center {
    text-align: center;
  }
  .title{
    font-size: xx-large;
    font-weight: 900;
    text-align: center;
    background-image: url('@/assets/bg.jpg');
    background-size: cover;
    height: 150px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Arial', sans-serif;
    color: white;
  }
  table th,
  table td {
    border-left: 1px lightgray solid;
    border-right: 1px lightgray solid;
  }
  table th:first-child,
  table td:first-child {
    border-left: 0;
  }
  table th:last-child,
  table td:last-child {
    border-right: 0;
  }
  input {
    width: 400px;
    display: flex;
    justify-content: left;
    opacity: 70%;
  }
  label {
    width: 100px;
  }
</style>
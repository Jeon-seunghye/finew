import axios from 'axios'
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'


export const useArticleStore = defineStore('article', () => {
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const router = useRouter()
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })
  // 게시글 불러오는 함수
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then(res => articles.value = res.data)
  }
  // 게시글 만드는 함수
  const createArticle = function ({ title, content}) {
    axios({
      method: 'post',
      url: `${API_URL}/api/v1/articles/`,
      data: {
        title,
        content
      },
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then((res) => {
      console.log(res)
      router.push({name:'home'})
    })
  }
  // 회원가입 함수
  const signUp = function (payload) {
    const {username, password1, password2, age, money, salary} = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username,
        password1,
        password2,
        age,
        money,
        salary
      }
    })
      .then((response) => {
        console.log(response.data)
        token.value = response.data.key
        router.push({name: 'home'})

      })
      .catch((error) => {
        console.log(error)
      })
  }
  // 로그인 함수
  const signIn = function (payload) {
    const {username, password} = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username,
        password
      }
    })
      .then((response) => {
        console.log(response.data)
        console.log(response.data.key)
        token.value = response.data.key
        router.push({name: 'home'})
      })
      .catch((error) => {
        console.log(error)
      })
  }

  return { articles, API_URL, token, isLogin, getArticles, createArticle, signUp, signIn }
}, { persist: true })

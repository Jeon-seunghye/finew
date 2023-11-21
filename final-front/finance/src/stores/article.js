import axios from 'axios'
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'


export const useArticleStore = defineStore('article', () => {
  //////// 변수 ////////
  const router = useRouter()
  
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  
  const articles = ref([])  // 전체 게시글
  const comments = ref([])  // 전체 댓글
  const exchange_rates = ref([]) // 전체 환율 정보
  
  // 로그인 유무(T/F)
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })


  //////// 함수 ////////
  // 게시글 불러오는 함수
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/articles/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then(res => articles.value = res.data)
  }

  // 게시글 생성 함수
  const createArticle = function ({title, content}) {
    axios({
      method: 'post',
      url: `${API_URL}/articles/`,
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
      router.push({name:'board'})
    })
    .catch((error) => {
      console.log(error)
    })
  }

  // 댓글 불러오는 함수
  const getComments = function () {
    axios({
      method: 'get',
      url: `${API_URL}/articles/comments/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then(res => comments.value = res.data)
  }

  // 회원가입 함수
  const signUp = function (payload) {
    const {username, password1, password2, email, age, money, salary, nickname} = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username,
        password1,
        password2,
        email,
        age,
        money,
        salary,
        nickname,
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

  // 로그아웃 함수
  const logOut = function () {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
    })
      .then((res) => {
        token.value = null
        router.push({ name: 'home' })
      })
      .catch((err) => {
        console.log(err)
      })
  }

    // 환율
    const getExchangeRate = function () {
      axios({
        method: 'get',
        url: `${API_URL}/banks/exchange_rate/`,
        headers: {
          Authorization: `Token ${token.value}`
        }
      })
      .then((res) => {
        exchange_rates.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    }


  return { articles, API_URL, token, isLogin, exchange_rates, comments, 
    getArticles, createArticle, signUp, signIn, logOut, getExchangeRate, getComments,  }
}, { persist: true })

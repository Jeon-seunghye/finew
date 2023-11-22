import { createRouter, createWebHistory, useRouter } from 'vue-router'

import HomeView from '@/views/HomeView.vue'
import LoginView from '@/views/LoginView.vue'
import SignUpView from '@/views/SignUpView.vue'
import ProfileView from '@/views/ProfileView.vue'

import PostView from '@/views/PostView.vue'
import PostCreateView from '@/views/PostCreateView.vue'
import PostDetailView from '@/views/PostDetailView.vue'
import PostUpdateView from '@/views/PostUpdateView.vue'

import CompareView from '@/views/CompareView.vue'
import DepositView from '@/views/DepositView.vue'
import DepositDetailView from '@/views/DepositDetailView.vue'
import SavingView from '@/views/SavingView.vue'
import SavingDetailView from '@/views/SavingDetailView.vue'

import CalculatorView from '@/views/CalculatorView.vue'
import MapView from '@/views/MapView.vue'



import { useArticleStore } from '@/stores/article'



const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
      beforeEnter: (to, from) => {
        const store = useArticleStore()
        if (store.isLogin === true) {
          console.log('이미로그인됨')
          return {name: 'home'}
        }
      }
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUpView,
      beforeEnter: (to, from) => {
        const store = useArticleStore()
        if (store.isLogin === true) {
          console.log('이미로그인됨')
          return {name: 'home'}
        }
      }
    },
    {
      path: '/calculator',
      name: 'calculator',
      component: CalculatorView
    },
    {
      path: '/board',
      name: 'board',
      component: PostView
    },
    {
      path: '/create',
      name: 'create',
      component: PostCreateView
    },
    {
      path: '/postdetail/:id',
      name: 'postdetail',
      component: PostDetailView,
      props: true
    },
    {
      path: '/postdetail/update/:id',
      name: 'postUpdate',
      component: PostUpdateView,
      props: true
    },
    {
      path: '/profile',
      name: 'profile',
      component: ProfileView
    },
    {
      path: '/map',
      name: 'map',
      component: MapView
    },
    {
      path: '/compare',
      name: 'compare',
      component: CompareView
    },
    {
      path: '/deposit',
      name: 'deposit',
      component: DepositView
    },
    {
      path: '/deposit/:fin_prdt_cd',
      name: 'depositdetail',
      component: DepositDetailView,
      props: true
    },
    {
      path: '/saving',
      name: 'saving',
      component: SavingView
    },
    {
      path: '/saving/:fin_prdt_cd',
      name: 'savingdetail',
      component: SavingDetailView,
      props: true
    },
    
  ]
})

export default router

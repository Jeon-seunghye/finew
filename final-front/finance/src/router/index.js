import { createRouter, createWebHistory, useRouter } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import LoginView from '@/views/LoginView.vue'
import SignUpView from '@/views/SignUpView.vue'
import CalculatorView from '@/views/CalculatorView.vue'
import PostView from '@/views/PostView.vue'
import PostDetailView from '@/views/PostDetailView.vue'
import PostCreateView from '@/views/PostCreateView.vue'
import ProfileView from '@/views/ProfileView.vue'
import MapView from '@/views/MapView.vue'
import DepositView from '@/views/DepositView.vue'
import SavingView from '@/views/SavingView.vue'
import CompareView from '@/views/CompareView.vue'
import ExchangeView from '@/views/ExchangeView.vue'

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
      path: '/postdetail',
      name: 'postdetail',
      component: PostDetailView
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
      path: '/saving',
      name: 'saving',
      component: SavingView
    },
    {
      path: '/exchange',
      name: 'exchange',
      component: ExchangeView
    },
  ]
})

export default router

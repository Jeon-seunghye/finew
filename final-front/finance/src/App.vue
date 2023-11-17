<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useArticleStore } from './stores/article'
const store = useArticleStore()
</script>

<template>
  <header>
    <!-- <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" /> -->
    <div  class="position relative">
      <nav class="navbar bg-body-tertiary sticky-top">
        <div class="container-fluid">
          <a class="navbar-brand" href="/">Finew</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasNavbar" aria-controls="offcanvasNavbar" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="offcanvas offcanvas-end" tabindex="-1" id="offcanvasNavbar" aria-labelledby="offcanvasNavbarLabel">
            <div class="offcanvas-header">
              <h5 class="offcanvas-title" id="offcanvasNavbarLabel">Menu</h5>
              <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
            </div>
            <div class="offcanvas-body">
              <ul class="navbar-nav justify-content-end flex-grow-1 pe-3">
                <li class="nav-item">
                  <a href="/" class="nav-link">Home</a>
                </li>
                <li class="nav-item">
                  <a href="/signup" class="nav-link" v-if="!store.isLogin">회원가입</a>
                </li>
                <li class="nav-item">
                  <a href="/login" class="nav-link" v-if="!store.isLogin">로그인</a>
                </li>
                <li class="nav-item">
                  <a href="/compare" class="nav-link">예적금비교</a>
                </li>
                <li class="nav-item">
                  <a href="/calculator" class="nav-link">환율계산기</a>
                </li>
                <li class="nav-item">
                  <a href="/map" class="nav-link">은행지도</a>
                </li>
                <li class="nav-item">
                  <a href="/board" class="nav-link">게시판</a>
                </li>

                <li class="nav-item dropdown">
                  <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                    회원정보
                  </a>
                  <ul class="dropdown-menu">
                    <li><a class="dropdown-item" href="#">추천목록</a></li>
                    <li><a class="dropdown-item" href="/profile">개인정보수정</a></li>
                    <li>
                      <hr class="dropdown-divider">
                    </li>
                    <li><a class="dropdown-item" href="#">Something else here</a></li>
                  </ul>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </nav>
      
    </div>
  </header>

  <RouterView />
</template>

<style scoped>

</style>

<!-- src/App.vue -->
<template>
  <div id="app">
    <!-- ❶ 글로벌 헤더 (sticky) -->
    <header class="global-header">
      <!-- 클릭 가능한 로고 -->
      <RouterLink to="/" class="logo">BaBoss Power</RouterLink>

      <!-- 네비게이션 링크들 -->
      <nav class="nav-links">
        <RouterLink to="/" class="link">Home</RouterLink>
        <RouterLink to="/articles" class="link">Community</RouterLink>
        <RouterLink to="/signup" class="link">SignUp</RouterLink>
        <RouterLink to="/login" class="link">LogIn</RouterLink>
      </nav>

      <!-- 프로필 아이콘 (필요시 로그인 유/무에 따라 교체) -->
      <!-- <RouterLink to="/profile" class="profile-icon">👤</RouterLink> -->
    </header>

    <!-- ❷ 헤더 바로 아래에 각 뷰 컴포넌트 -->
    <div class="page-container">
      <router-view />
    </div>
  </div>
</template>

<script setup>
// 특별한 스크립트 로직은 없습니다.
</script>

<style>
/* Reset & full-height */
html, body, #app {
  margin: 0;
  padding: 0;
  height: 100%;
  overflow: auto;
}

/* ❶ sticky 글로벌 헤더 */
.global-header {
  position: sticky;
  top: 0;
  left: 0;
  right: 0;
  height: 56px;
  background-color: #4e70ff;
  color: #fff;
  display: flex;
  align-items: center;
  padding: 0 16px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.1);
  z-index: 1000;
  font-family: sans-serif;
}

/* 로고 */
.global-header .logo {
  font-weight: bold;
  font-size: 1.2rem;
  color: #fff;
  text-decoration: none;
  margin-right: 2rem;
}

/* 네비게이션 링크 컨테이너 */
.global-header .nav-links {
  display: flex;
  flex: 1;
}

/* 각 링크 */
.global-header .link {
  color: #fff;
  text-decoration: none;
  margin-right: 1.5rem;
  font-size: 0.95rem;
}
.global-header .link:hover {
  text-decoration: underline;
}

/* 프로필 아이콘 위치 */
.global-header .profile-icon {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}

/* ❷ 페이지 컨테이너: 헤더 높이만큼 자동 여백 */
.page-container {
  min-height: calc(100vh - 56px);
  background: #f5f5f5;
}
</style>

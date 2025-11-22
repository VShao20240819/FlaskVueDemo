<template>
  <div class="app">
    <div class="sidebar">
      <ul>
        <li><router-link to="/">首页</router-link></li>
        <li><router-link to="/task">任务页面</router-link></li>
        <li><router-link to="/monitor">监控页面</router-link></li>
        <li><router-link to="/operation">操作页面</router-link></li>
      </ul>
    </div>
    <div class="main">
      <router-view></router-view>
    </div>
  </div>
</template>

<script setup>
</script>

<style>
.app {
  display: flex;
  height: 100vh;
}
.sidebar {
  width: 200px;
  background: #f0f0f0;
  padding: 10px;
}
.main {
  flex: 1;
  padding: 20px;
}
ul {
  list-style: none;
  padding: 0;
}
li {
  margin: 10px 0;
}
a {
  text-decoration: none;
  color: #333;
}
</style>

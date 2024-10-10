<template>
  <div class="main-container d-flex flex-row align-items-center bg-light">
    <div class="left bg-primary"></div>
    <div class="right bg-light"></div>
  </div>
</template>
<script>
export default {
  name: 'dashboardView',
  mounted() {
    console.log('dashboard is mounted')
  }
}
</script>
<style lang="css" scoped>
.main-container {
  position: absolute;
  width: 100vw;
  height: 100vh;
}
.main-container .left {
  position: relative;
  width: 20%;
  height: 100%;
}
.main-container .right {
  position: relative;
  width: 80%;
  height: 100%;
}
</style>
<template>
  <div class="main-container d-flex flex-row align-items-center bg-light">
    <LeftComponent class="left d-none d-lg-block" />
    <RightComponent class="right" />
  </div>
</template>
<script>
import LeftComponent from '@/components/dashboard/LeftComponent.vue'
import RightComponent from '@/components/dashboard/RightComponent.vue'

export default {
  name: 'dashboardView',
  components: {
    LeftComponent,
    RightComponent
  },
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
  overflow-y: scroll;
}
@media screen and (max-width: 1024px) {
  .main-container .right {
    position: absolute;
    width: 100vw;
    height: 100vh;
    top: 0;
    left: 0;
  }
}
</style>
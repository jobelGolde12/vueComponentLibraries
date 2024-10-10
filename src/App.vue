

<template>
  <!-- <div class="main-container"> -->
  <!-- <WelcomeView v-if="inWelcome" class="welcome" /> -->
  <!-- v-if="!inWelcome" -->
  <div class="view">
    <RouterView />
  </div>
  <!-- </div> -->
</template>

<script>
import { RouterView } from 'vue-router'
// import WelcomeView from './views/HomeView.vue'
export default {
  name: 'app',
  data() {
    return {
      inWelcome: true
    }
  },
  components: {
    RouterView
    // WelcomeView
  }
}
</script>

<style scoped>
@import 'bootstrap/dist/css/bootstrap.min.css';
@import './assets/global.css';
.welcome {
  position: absolute;
  width: 100vw;
  height: 100vh;
  top: 0;
  left: 0;
}
</style>

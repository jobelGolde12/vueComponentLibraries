<template>
  <div class="main-container bg-light">
    <HeaderComponent />
    <!-- hero section content  -->
    <section
      id="hero-content"
      class="d-flex flex-column align-items-center pt-5 bg-light text-dark text-center"
    >
      <HeroComponent />
    </section>

    <section id="about">
      <AboutUsComponent />
    </section>

    <section>
      <SubContent />
    </section>

    <FooterComponent />
  </div>
</template>
<script>
import HeaderComponent from '../components/welcome/HeaderComponent.vue'
import HeroComponent from '../components/welcome/HeroComponent.vue'
import FooterComponent from '../components/welcome/FooterComponent.vue'
import AboutUsComponent from '../components/welcome/AboutUsComponent.vue'
import SubContent from '../components/welcome/SubContent.vue'

export default {
  name: 'welcomeView',
  components: {
    // Link, Head
    HeaderComponent,
    HeroComponent,
    FooterComponent,
    AboutUsComponent,
    SubContent
  },
  mounted() {
    console.log('welcome mounted')
  }
}
</script>
<style lang="css" scoped>
/* @import '../../css/global.css'; */
@import '../assets/welcome.css';
</style>
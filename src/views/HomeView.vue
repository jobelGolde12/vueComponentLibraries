<template>
  <div class="main-container bg-light">
    <!-- Navagation bar -->
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

    <section id="howItsWork">
      <div class="stats-section pt-5 mt-5">
        <h1 class="text-dark text-center fw-bolder pt-5 mb-3">How It Works?</h1>
        <div class="container custom-container mt-5 pt-5">
          <div class="row justify-content-center">
            <!-- Card 1 -->
            <div class="col-lg-3 col-md-6 mb-4">
              <div class="stats-card text-center">
                <img src="../../images/announce.svg" alt="" />
                <div class="stats-title mt-3">Report a Lost Item</div>
                <div class="stats-label">
                  Post details about your missing item, including a description, last known
                  location, and contact information.
                </div>
              </div>
            </div>
            <!-- Card 2 -->
            <div class="col-lg-3 col-md-6 mb-4">
              <div class="stats-card text-center">
                <img src="../../images/found.svg" alt="" />
                <div class="stats-title mt-3">Report a Found Item</div>
                <div class="stats-label">
                  Post details of what you found to help the rightful owner claim their lost
                  property.
                </div>
              </div>
            </div>
            <!-- Card 3 -->
            <div class="col-lg-3 col-md-6 mb-4">
              <div class="stats-card text-center">
                <img src="../../images/brows.svg" alt="" />
                <div class="stats-title mt-3">Browse Lost or Found Listings</div>
                <div class="stats-label">
                  Check listings to see if your item has been found or if someone is looking for
                  what you found.
                </div>
              </div>
            </div>
            <!-- Card 4 -->
            <div class="col-lg-3 col-md-6 mb-4">
              <div class="stats-card text-center">
                <img src="../../images/claim.svg" alt="" />
                <div class="stats-title mt-3">Reclaim or Return Items</div>
                <div class="stats-label">
                  Contact the person and arrange the return once an item matches.
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <FooterComponent />
  </div>
</template>
<script>
import HeaderComponent from '../components/welcome/HeaderComponent.vue'
import HeroComponent from '../components/welcome/HeroComponent.vue'
import FooterComponent from '../components/welcome/FooterComponent.vue'
import AboutUsComponent from '../components/welcome/AboutUsComponent.vue'

export default {
  name: 'welcomeView',
  components: {
    // Link, Head
    HeaderComponent,
    HeroComponent,
    FooterComponent,
    AboutUsComponent
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
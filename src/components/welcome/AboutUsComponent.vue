<template>
  <div class="main-container">
    <div class="container text-center pt-5">
      <h1 class="text-dark fw-bolder">About Us!</h1>

      <div class="about-hero-section mt-5">
        <div class="container custom-container">
          <div class="row align-items-center mt-4">
            <div class="col-lg-6 text-left">
              <h1 class="hero-title text-start">Who We Are</h1>
              <p class="hero-subtitle text-start">
                We are a team of passionate developers and designers with a mission to simplify web
                development through powerful, reusable, and customizable Vue.js components.
              </p>
              <h5 class="text-primary text-start">Tools:</h5>
              <div class="d-flex flex-row gap-2">
                <i class="bi bi-bootstrap text-success"></i>
                <i class="bi bi-vue text-success"></i>
              </div>
            </div>
            <div class="col-lg-6 text-left about-image-container">
              <img
                src="../../assets/images/team-icon.svg"
                alt="Image kinam"
                class="d about-image"
              />
              <!-- <h5 class="text-dark">Our Mission</h5>
                          <p class="d-block text-dark">We aim to provide a simple, user-friendly online service that bridges the gap between those who have lost something and those who have found it.</p> -->
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'aboutUsComponent'
}
</script>
<style lang="css" scoped>
.main-container {
  width: 100%;
  height: 100%;
}
.about-image-container img {
  position: relative;
  width: 80%;
  height: 60%;
}
</style>
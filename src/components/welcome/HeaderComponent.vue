<template>
  <div>
    <div class="navbar d-flex flex-row justify-content-between align-items-center px-3">
      <div class="logo"><h4 class="text-dark">Logo</h4></div>
      <div class="links d-none d-lg-flex flex-row gap-4 align-items-center ms-5">
        <a href="#about" class="text-dark text-decoration-none">About</a>
        <a href="#howItsWork" class="text-dark text-decoration-none">How it's work?</a>
        <a href="#" class="text-dark text-decoration-none">Contact</a>
        <router-link to="/pricingComponent" class="text-dark text-decoration-none"
          >Pricing</router-link
        >
      </div>

      <div class="d-flex flex-row gap-3">
        <a href="#" class="btn btn-light text-decoration-none">Login</a>
        <a href="#hero-content" class="btn btn-dark text-decoration-none">Signup</a>
      </div>
      <div class="bi bi-list fs-1 fw-bolder pointer hover d-block d-lg-none"></div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'headerComponent'
}
</script>
<style lang="css" scoped>
/* @import '../'; */
a:hover {
  background: #f8f9fa;
}
</style>
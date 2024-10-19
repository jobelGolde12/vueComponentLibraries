<template>
  <div class="main-container bg-light">
    <div
      class="header py-2 px-3 container-fuild d-flex flex-row justify-content-between align-items-center"
    >
      <div class="logo ms-4">
        <h4 class="text-dark fw-semibold">Logo</h4>
      </div>

      <div class="links d-flex flex-row gap-3 d-none d-lg-block">
        <a href="#" class="text-dark text-decoration-none p-2">Home</a>
        <a href="#" class="text-dark text-decoration-none p-2">Services</a>
        <a href="#" class="text-dark text-decoration-none p-2">Contact</a>
        <a href="#" class="text-dark text-decoration-none p-2">Blogs</a>
      </div>

      <div class="action d-flex flex-row gap-3 d-none d-md-block d-lg-block">
        <div class="btn btn-light">Login</div>
        <div class="btn btn-dark">Get started</div>
      </div>

      <i class="bi bi-list fs-3 d-inline-block d-lg-none"></i>
    </div>

    <section id="hero" class="d-flex flex-row align-items-center justify-content-center">
      <div class="left">
        <h1 class="text-dark fw-bold">Lorem ipsum dolor sit amet consectetur adipisicing.</h1>
        <p class="text-dark fw-light">
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Similique explicabo rerum
          eligendi, amet at corporis?
        </p>

        <div class="link-container d-flex flex-row gap-4">
          <i class="bi bi-facebook text-success fs-4"></i>
          <i class="bi bi-instagram text-success fs-4"></i>
          <i class="bi bi-twitter text-success fs-4"></i>
        </div>

        <div class="bottom-info d-flex flex-row gap-3 mt-4 d-none d-lg-flex d-md-flex">
          <div class="card bg-light text-dark p-2">
            <h5 class="mb-0 pb-0 fw-bolder">100%</h5>
            <p class="fw-light">Lorem, ipsum.</p>
          </div>
          <div class="card bg-light text-dark p-2">
            <h5 class="mb-0 pb-0 fw-bolder">100%</h5>
            <p class="fw-light">Lorem, ipsum.</p>
          </div>
          <div class="card bg-light text-dark p-2">
            <h5 class="mb-0 pb-0 fw-bolder">100%</h5>
            <p class="fw-light">Lorem, ipsum.</p>
          </div>
        </div>
      </div>

      <div class="right">
        <div class="image-container">
          <img :src="img" alt="" />
        </div>
      </div>
    </section>
  </div>
</template>
      <script>
import img from '../../assets/images/signup-icon.svg'
export default {
  name: 'trialComponent',
  data() {
    return {
      img: img
    }
  }
}
</script>
      <style lang="css" scoped>
* {
  box-sizing: border-box;
}
.main-container {
  position: absolute;
  width: 100%;
  height: 100%;
}
#hero {
  width: 100%;
  height: 80%;
}
#hero .right,
#hero .left {
  position: relative;
  width: 45%;
  height: 80%;
}
.image-container img {
  position: absolute;
  width: 100%;
  height: 100%;
  transition: 0.5s;
}
.image-container img:hover {
  transform: scale(1.1);
}
.bottom-info .card {
  border: none;
}
@media screen and (max-width: 1024px) {
  #hero .left h1 {
    font-size: 1.5rem;
  }
}
</style>
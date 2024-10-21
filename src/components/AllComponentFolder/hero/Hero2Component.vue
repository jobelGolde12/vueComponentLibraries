<template>
  <div class="main-container">
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">Logo</a>

        <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
          <ul class="navbar-nav d-flex gap-3">
            <li class="nav-item">
              <a class="nav-link" href="#">Abous Us!</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Contact</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Community</a>
            </li>
            <li class="nav-item">
              <a class="btn btn-light" href="#">Login</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero-section d-flex justify-content-between gap-5">
      <div class="hero-text">
        <h1 class="text-light">
          Lorem ipsum <span class="text-warning fw-semibold">dolor</span> sit amet.
        </h1>
        <p class="text-light">
          Lorem, ipsum dolor sit amet consectetur adipisicing elit. Harum minima quod cumque, rerum
          voluptates tempore?
        </p>
        <div class="hero-buttons">
          <a href="#" class="btn btn-light">Get Started</a>
          <a href="#" class="btn btn-learn-more"
            >Read More <i class="bi bi-arrow-right ms-1"></i
          ></a>
        </div>
      </div>
      <div class="hero-image">
        <img :src="img" alt="Hero Image" />
      </div>
    </section>
  </div>
</template>
      <script>
import img from '../../../assets/images/everyComponentsImage/hero/hero-icon.svg'
export default {
  name: 'hero2Component',
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
  width: 100vw;
  height: 100vh;
  background-image: linear-gradient(15deg, #13547a 0%, #80d0c7 100%);
  background-size: cover;
  background-position: center;
  z-index: 1;
  overflow: hidden;
}
.navbar {
  background: transparent;
}

.navbar-brand {
  font-weight: bold;
  color: #ffffff;
}

.nav-link {
  color: #ffffff;
}

.btn-signup {
  background-color: #6a00ff;
  border-radius: 20px;
  padding: 8px 20px;
}

.hero-section {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  padding: 0 50px;
  min-height: 100vh;
}

.hero-text {
  max-width: 500px;
}

.hero-text h1 {
  font-size: 3rem;
  font-weight: bold;
}

.hero-text p {
  margin: 20px 0;
  line-height: 1.5;
}

.hero-buttons .btn {
  margin-right: 15px;
  padding: 12px 30px;
  border-radius: 30px;
}

.btn-get-started {
  background-color: #ff6b6b;
  color: #fff;
}

.btn-learn-more {
  background-color: transparent;
  color: #fff;
  border: 1px solid #fff;
}
.hero-section .hero-text,
.hero-section .hero-image {
  width: 45%;
  position: relative;
}
.hero-image img {
  max-width: 80%;
  border-radius: 20px;
  right: 0;
}
</style>
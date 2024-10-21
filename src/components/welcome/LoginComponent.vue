<template>
  <div class="main-container bg-light d-flex flex-row justify-content-center align-items-center">
    <div class="container form-container">
      <form action="#" method="POST" class="form d-flex flex-column gap-3 p-4 rounded">
        <h3 class="text-dark fw-normal text-center">Login</h3>
        <div>
          <label for="email" class="text-muted mb-1">Email:</label>
          <input
            type="text"
            placeholder="example@gmail.com"
            id="email"
            class="w-100"
            v-model="formData.email"
          />
        </div>

        <div>
          <label for="password" class="text-muted mb-1">Password:</label>
          <input
            type="password"
            placeholder="examplepass123"
            id="password"
            class="w-100"
            v-model="formData.password"
          />
        </div>

        <div><input type="submit" class="btn btn-success w-100 mb-0" value="Login" /></div>
        <p class="tex-dark text-center mt-0 pt-0 or-text">
          aready have an account? |
          <router-link to="/signupComponent" class="text-primary">signup</router-link>
        </p>
        <div
          class="choice text-center d-flex flex-column justify-content-center align-items-center"
        >
          <p class="tex-dark text-center mb-0 pb-0 or-text">or</p>

          <div
            class="container-fluid mt-2 d-flex flex-row gap-3 justify-content-center align-items-center"
          >
            <i class="bi bi-google d-inline-block fs-4 text-success pointer hover"></i>
            <i class="bi bi-facebook d-inline-block fs-4 text-success pointer hover"></i>
          </div>
        </div>
      </form>
    </div>

    <div class="container image-container d-none d-lg-block">
      <img src="../../assets/images/login-icon.svg" alt="Login image" class="rounded" />
    </div>
  </div>
</template>
<script>
export default {
  name: 'loginComponent',
  data() {
    return {
      formData: {
        email: '',
        password: ''
      }
    }
  }
}
</script>
<style lang="css" scoped>
@import '../../assets/global.css';
.main-container {
  position: absolute;
  width: 100vw;
  height: 100vh;
}
.main-container .container {
  min-width: 40%;
  height: auto;
  position: relative;
}
input {
  padding: 0.5rem 1rem;
}
form {
  background: #fff;
}
.image-container {
  overflow: hidden;
}
.image-container img {
  position: relative;
  width: 100%;
  height: 100%;
  transition: 0.5s;
}
.image-container img:hover {
  transform: scale(1.1);
}
@media screen and (min-width: 1024px) {
  .main-container .container {
    max-width: 40%;
  }
}
</style>
<template>
  <div class="main-container d-flex justify-content-center align-items-center">
    <div class="container d-flex flex-row gap-3">
      <div class="content-container">
        <h4 class="mb-2 fw-semibold">
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Veniam, minima.
        </h4>
        <p class="text-dark fw-light">
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Delectus tempore ipsam maiores
          nulla blanditiis, unde accusamus nam error non vel!
        </p>

        <p class="text-dark fw-normal">Follow me on:</p>
        <div class="d-flex flex-row gap-4">
          <i class="bi bi-facebook text-success d-block fs-5"></i>
          <i class="bi bi-instagram text-success d-block fs-5"></i>
          <i class="bi bi-twitter text-success d-block fs-5"></i>
        </div>
      </div>

      <div class="image-container p-1">
        <img :src="img" alt="Image" class="rounded" />
      </div>
    </div>
  </div>
</template>
    <script>
import img from '../../assets/images/everyComponentsImage/img1.jpg'
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
.main-container {
  position: absolute;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.1);
}
.container {
  width: 70%;
  height: 50%;
}
.container .image-container,
.container .content-container {
  position: relative;
  width: 50%;
  height: 100%;
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
</style>
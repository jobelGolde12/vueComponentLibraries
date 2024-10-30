<template>
  <div class="main-container bg-light d-flex flex-row justify-content-center align-items-center">
    <div class="card p-3 shadow-sm">
      <div class="head">
        <div class="btn btn-gradient w-100"><i class="bi bi-plus text-light fs-4"></i></div>
        <h5 class="text-dark fw-normal mt-2">My activity</h5>
        <p class="text-muted">
          <i class="bi bi-people me-2 text-primary"></i>
          Lorem ipsum dolor sit amet consectetur adipisicing.
        </p>
      </div>
      <div class="body">
        <p class="text-dark">Activity rate</p>
        <div class="loader">
          <div class="loader-inner"></div>
        </div>

        <div class="d-flex flex-row gap-1 align-items-center mt-2">
          <abbr title="My Activity">
            <i class="bi bi-heart py-1 px-2"></i>
          </abbr>
          <abbr title="My profile">
            <i class="bi bi-person text-primary py-1 px-2"></i>
          </abbr>
        </div>
      </div>
    </div>
  </div>
</template>
  <script>
export default {
  name: 'activityCard'
}
</script>
  <style lang="css" scoped>
.main-container {
  width: 100vw;
  height: 100vh;
}
.card {
  width: 30%;
  height: 50%;
  border: none;
}
.btn-gradient {
  background-color: #0093e9;
  background-image: linear-gradient(160deg, #0093e9 0%, #80d0c7 100%);
}
.loader {
  position: relative;
  width: 100%;
  height: 25%;
  background: rgba(0, 0, 0, 0.1);
  border-radius: 20px;
}
.loader-inner {
  position: relative;
  width: 30%;
  height: 100%;
  border-radius: 20px;
  background-color: #0093e9;
  background-image: linear-gradient(160deg, #0093e9 0%, #80d0c7 100%);
}
.bi-heart {
  color: red;
}
</style>
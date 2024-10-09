<template>
  <div class="main-container">
    <div class="container-fluid text-center">
      <h1 class="text-dark fw-bolder">What people say?</h1>
      <div class="container sub-content">
        <p class="text-dark">
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam explicabo delectus
          maiores expedita magnam! Asperiores minus fuga inventore eaque fugiat!
        </p>
      </div>

      <div class="row px-2 pt-3">
        <div class="col-12 col-lg-4">
          <div class="card bg-light p-3">
            <i class="bi bi-quote fs-1 text-primary"></i>
            <p>
              Lorem ipsum, dolor sit amet consectetur adipisicing elit. Libero vero odit, impedit
              quae officia labore!
            </p>

            <div class="d-flex flex-row gap-1 card-bottom align-items-center">
              <img src="../../assets/images/profile.png" alt="profile" />
              <a href="#" class="d-block fw-bold text-decoration-none text-dark"
                >Maryrose Palanca</a
              >
            </div>

            <div class="d-flex flex-row gap-2">
              <i class="bi bi-star-fill text-warning"></i>
              <i class="bi bi-star-fill text-warning"></i>
              <i class="bi bi-star-fill text-warning"></i>
              <i class="bi bi-star-fill text-warning"></i>
              <i class="bi bi-star text-warning"></i>
            </div>
          </div>
        </div>

        <div class="col-12 col-lg-4">
          <div class="card bg-light p-3">
            <i class="bi bi-quote fs-1 text-primary"></i>
            <p>
              Lorem ipsum, dolor sit amet consectetur adipisicing elit. Libero vero odit, impedit
              quae officia labore!
            </p>

            <div class="d-flex flex-row gap-1 card-bottom align-items-center">
              <img src="../../assets/images/profile.png" alt="profile" />
              <a href="#" class="d-block fw-bold text-decoration-none text-dark"
                >Maryrose Palanca</a
              >
            </div>

            <div class="d-flex flex-row gap-2">
              <i class="bi bi-star-fill text-warning"></i>
              <i class="bi bi-star-fill text-warning"></i>
              <i class="bi bi-star-fill text-warning"></i>
              <i class="bi bi-star-fill text-warning"></i>
              <i class="bi bi-star text-warning"></i>
            </div>
          </div>
        </div>

        <div class="col-12 col-lg-4">
          <div class="card bg-light p-3">
            <i class="bi bi-quote fs-1 text-primary"></i>
            <p>
              Lorem ipsum, dolor sit amet consectetur adipisicing elit. Libero vero odit, impedit
              quae officia labore!
            </p>

            <div class="d-flex flex-row gap-1 card-bottom align-items-center">
              <img src="../../assets/images/profile.png" alt="profile" />
              <a href="#" class="d-block fw-bold text-decoration-none text-dark"
                >Maryrose Palanca</a
              >
            </div>

            <div class="d-flex flex-row gap-2">
              <i class="bi bi-star-fill text-warning"></i>
              <i class="bi bi-star-fill text-warning"></i>
              <i class="bi bi-star-fill text-warning"></i>
              <i class="bi bi-star-fill text-warning"></i>
              <i class="bi bi-star text-warning"></i>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'subContent'
}
</script>
<style lang="css" scoped>
.main-container {
  width: 100vw;
  height: 100vh;
}
.sub-content {
  position: relative;
  width: 600px;
  height: auto;
}

.card-bottom img {
  position: relative;
  width: 50px;
  height: 50px;
  border-radius: 50%;
}
</style>
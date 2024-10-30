<template>
  <div class="main-container bg-light d-flex flex-row justify-content-center align-items-center">
    <div class="card p-3 shadow-sm">
      <div class="head">
        <p class="fw-light mb-0">Lorem, ipsum.</p>
        <h5 class="fw-normal">Users daily record</h5>
      </div>

      <div class="body">
        <div class="container d-flex flex-column gap-1 mt-2 px-0">
          <div class="d-flex justify-content-between align-items-center list p-2 rounded">
            <div><h5 class="text-dark fs-3">101</h5></div>
            <div class="fw-light data-text">Lorem ipsum dolor sit amet.</div>
            <div><i class="bi bi-arrow-right fs-5"></i></div>
          </div>

          <div class="d-flex justify-content-between align-items-center list p-2 rounded">
            <div><h5 class="text-dark fs-3">405</h5></div>
            <div class="fw-light data-text">Lorem ipsum dolor sit amet.</div>
            <div><i class="bi bi-arrow-right fs-5"></i></div>
          </div>

          <div class="d-flex justify-content-between align-items-center list p-2 rounded">
            <div><h5 class="text-dark fs-3">1032</h5></div>
            <div class="fw-light data-text">Lorem ipsum dolor sit amet.</div>
            <div><i class="bi bi-arrow-right fs-5"></i></div>
          </div>
        </div>

        <div class="btn btn-success mt-2 w-100"><i class="bi bi-plus text-light fs-4"></i></div>
      </div>
    </div>
  </div>
</template>
  <script>
export default {
  name: 'dashboardCard'
}
</script>
  <style lang="css" scoped>
.main-container {
  width: 100vw;
  height: 100vh;
}
.card {
  width: 30%;
  height: auto;
  border: none;
}
.data-text {
  font-size: 0.9rem;
}
.list:hover {
  background: rgba(0, 0, 0, 0.1);
  cursor: pointer;
}
</style>
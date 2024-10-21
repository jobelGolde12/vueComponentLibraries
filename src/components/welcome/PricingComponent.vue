<template>
  <div class="main-container bg-light">
    <div class="container py-5">
      <div class="pricing-header">
        <p class="text-dark">Lorem ipsum dolor sit amet.</p>
        <h2 class="text-dark fw-light mt-0 pt-0">Our Pricing Plans For You</h2>
        <p>Choose the best plan that fits your needs.</p>
      </div>

      <div class="row justify-content-center">
        <!-- Basic Package -->
        <div class="col-md-3">
          <div class="card mb-4 shadow-sm">
            <div class="pricing-card">
              <div class="icon">
                <i class="bi bi-coin text-light"></i>
              </div>
              <h4>Basic Package</h4>
              <div class="price">$50 <span style="font-size: 1rem">/ month</span></div>
            </div>
            <div class="card-body text-center">
              <ul class="features-list">
                <li><i class="bi bi-check text-success"></i> Limited Component</li>
              </ul>
              <a href="#" class="btn btn-select">Select Now</a>
            </div>
          </div>
        </div>

        <!-- Professional Package -->
        <div class="col-md-3">
          <div class="card mb-4 shadow-sm">
            <div class="pricing-card">
              <div class="icon mb-3">
                <!-- <img src="https://img.icons8.com/ios-filled/50/edit.png" alt="Edit Icon" /> -->
              </div>
              <h4>Professional Package</h4>
              <div class="price">$100 <span style="font-size: 1rem">/ month</span></div>
            </div>
            <div class="card-body text-center">
              <ul class="features-list">
                <li><i class="bi bi-check text-success"></i> Unliimited Component</li>
              </ul>
              <a href="#" class="btn btn-select">Select Now</a>
            </div>
          </div>
        </div>

        <!-- Startup Package -->
        <div class="col-md-3">
          <div class="card mb-4 shadow-sm">
            <div class="pricing-card">
              <div class="icon mb-3">
                <!-- <img src="https://img.icons8.com/ios-filled/50/anchor.png" alt="Anchor Icon" /> -->
              </div>
              <h4>Startup Package</h4>
              <div class="price">$200 <span style="font-size: 1rem">/ month</span></div>
            </div>
            <div class="card-body text-center">
              <ul class="features-list">
                <li><i class="bi bi-check text-success"></i> Unlimited Component</li>
              </ul>
              <a href="#" class="btn btn-select">Select Now</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'routerComponent'
}
</script>
<style lang="css" scoped>
.main-container {
  position: absolute;
  width: 100vw;
  height: 100vh;
  overflow: hidden;
}
.pricing-header {
  text-align: center;
  padding: 2rem;
}
.card {
  border: none;
  border-radius: 15px;
  transition: all 0.3s ease;
}
.card:hover {
  transform: scale(1.05);
}
.pricing-card {
  /* background-color: #198754;
  color: #fff; */
  padding: 1.5rem;
  text-align: center;
}
.card-body {
  background-color: white;
  border-radius: 0 0 15px 15px;
}
.price {
  font-size: 2.5rem;
  font-weight: bold;
}
.btn-select {w
  background-color: #563d7c;
  color: #fff;
  border-radius: 25px;
}
.btn-select:hover {
  background-color: #6c5cb5;
}
.features-list {
  list-style: none;
  padding-left: 0;
}
.features-list li {
  margin: 0.5rem 0;
  color: #6c757d;
}

.icon img {
  width: 30px;
}
</style>
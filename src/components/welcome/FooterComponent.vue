<template>
  <div>
    <footer id="footer" class="footer mt-5 pt-5">
      <div class="container">
        <div class="row">
          <!-- <div class="col-md-4">
  <div class="logo-section">
    <p>Find and Report Lost or Found
      Items in Bulan easily</p>
  </div>
</div> -->
          <div class="col-md-3">
            <h5>Contact Info.</h5>
            <ul class="list-unstyled">
              <li><a href="#">jobelgolde43@gmail.com</a></li>
              <li><a href="#">ruzzlegemina@gmail.com</a></li>
              <li><a href="#">Bulan, Sorsogon</a></li>
            </ul>
          </div>
          <div class="col-md-3">
            <h5>Social media</h5>
            <ul class="list-unstyled">
              <li>
                <a href="#"><i class="bi bi-facebook text-light me-1"></i>Facebook</a>
              </li>
              <li>
                <a href="#"><i class="bi bi-twitter text-light me-1"></i>Twitter</a>
              </li>
              <li>
                <a href="#"><i class="bi bi-instagram text-light me-1"></i>Instagram</a>
              </li>
            </ul>
          </div>
          <div class="col-md-3">
            <h5>Quick Links</h5>
            <ul class="list-unstyled">
              <li><a href="#hero-content">Home</a></li>

              <li><a href="#hero-content">Home</a></li>

              <li><a href="#about">About Us</a></li>
            </ul>
          </div>
          <div class="col-md-3">
            <h5>Company</h5>
            <ul class="list-unstyled">
              <li><a href="#">Terms & Conditions</a></li>
              <li><a href="#">Privacy Policy</a></li>
            </ul>
          </div>
        </div>
        <div class="row mt-5">
          <div class="col-md-4">
            <h5>Bulan Lost And Found Website</h5>
            <div class="social-icons">
              <a href="#"><i class="fab fa-facebook"></i></a>
              <a href="#"><i class="fab fa-twitter"></i></a>
              <a href="#"><i class="fab fa-linkedin"></i></a>
            </div>
          </div>
          <!-- <div class="col-md-8 text-md-end">
  <form class="subscribe-form">
    <input type="email" class="form-control" placeholder="Enter email address">
    <button class="btn btn-primary">Subscribe</button>
  </form>
</div> -->
        </div>
      </div>
    </footer>
  </div>
</template>
<script>
export default {
  name: 'footerComponent'
}
</script>
<style lang="css" scoped>
.footer {
  background-color: #1f1f1f;
  padding: 40px 0;
  color: #fff;
}

.footer h5 {
  color: #ffffff;
  font-size: 18px;
  margin-bottom: 20px;
}

.footer p {
  font-size: 14px;
  color: #999;
}

.footer .list-unstyled a,
.footer .list-unstyled .link {
  color: #999;
  text-decoration: none;
  display: block;
  margin-bottom: 8px;
}

.footer .list-unstyled a:hover {
  color: #ffffff;
}

.social-icons a {
  color: #fff;
  margin-right: 15px;
  font-size: 18px;
}

.footer p {
  font-size: 14px;
  color: #999;
  margin-top: 20px;
}
</style>
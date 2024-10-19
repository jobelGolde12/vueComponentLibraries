<template>
  <div class="main-container">
    <div class="d-flex flex-column">
      <div class="sidebar">
        <div class="sidenav-header d-flex flex-row align-items-center gap-2">
          <div class="logo pointer"></div>
          <div class="pointer">{{ user.name }}</div>
        </div>

        <router-link
          class="hover"
          to="/dashboardView"
          :class="{ 'text-success': $route.path === '/dashboardView' }"
          ><i class="bi bi-house"></i> Home</router-link
        >

        <router-link
          class="hover"
          to="/pricingComponent"
          :class="{ 'text-success': $route.path === '/pricingComponent' }"
          ><i class="bi bi-coin"></i> My plan</router-link
        >
        <a href="#"><i class="bi bi-file-earmark-text"></i> My Collections</a>

        <div class="categories bg-light">
          <p class="text-dark d-flex align-ietms-center" @click="toggleCategoriesFunc">
            Categories <i class="categories-icon bi ms-2"></i>
          </p>
          <ul class="d-flex flex-column gap-2 ms-3">
            <li>
              <router-link
                class="link"
                to="/profileComponent"
                :class="{ 'text-success': $route.path === '/profileComponent' }"
              >
                Hero Section</router-link
              >
            </li>

            <li>
              <router-link
                class="link"
                to="/profileComponent"
                :class="{ 'text-success': $route.path === '/profileComponent' }"
              >
                Headers</router-link
              >
            </li>

            <li>
              <router-link
                class="link"
                to="/profileComponent"
                :class="{ 'text-success': $route.path === '/profileComponent' }"
              >
                Footers</router-link
              >
            </li>

            <li>
              <router-link
                class="link"
                to="/profileComponent"
                :class="{ 'text-success': $route.path === '/profileComponent' }"
              >
                Navagation</router-link
              >
            </li>

            <li>
              <router-link
                class="link"
                to="/profileComponent"
                :class="{ 'text-success': $route.path === '/profileComponent' }"
              >
                Footers</router-link
              >
            </li>

            <li>
              <router-link
                class="m-0 p-0"
                to="/profileComponent"
                :class="{ 'text-success': $route.path === '/profileComponent' }"
              >
                Content Section</router-link
              >
            </li>

            <li>
              <router-link
                class="link"
                to="/profileComponent"
                :class="{ 'text-success': $route.path === '/profileComponent' }"
              >
                Forms</router-link
              >
            </li>

            <li>
              <router-link
                class="link"
                to="/profileComponent"
                :class="{ 'text-success': $route.path === '/profileComponent' }"
              >
                Cards</router-link
              >
            </li>

            <li>
              <router-link
                class="link"
                to="/profileComponent"
                :class="{ 'text-success': $route.path === '/profileComponent' }"
              >
                Modals</router-link
              >
            </li>

            <li>
              <router-link
                class="link"
                to="/profileComponent"
                :class="{ 'text-success': $route.path === '/profileComponent' }"
              >
                Carousel</router-link
              >
            </li>

            <li>
              <router-link
                class="link"
                to="/profileComponent"
                :class="{ 'text-success': $route.path === '/profileComponent' }"
              >
                List</router-link
              >
            </li>

            <li>
              <router-link
                class="link"
                to="/profileComponent"
                :class="{ 'text-success': $route.path === '/profileComponent' }"
              >
                Footers</router-link
              >
            </li>
          </ul>
        </div>

        <router-link
          to="/profileComponent"
          :class="{ 'text-success': $route.path === '/profileComponent' }"
          ><i class="bi bi-person"></i> Profile</router-link
        >
        <div class="collapse" id="preferences">
          <div class="submenu">
            <a href="#">Reporting</a>
            <a href="#">Templates</a>
            <a href="#">Integrations</a>
            <a href="#">Notifications</a>
          </div>
        </div>

        <router-link to="trialComponent" class="text-primary hover"
          >This is only for the trial component while developing</router-link
        >
      </div>
    </div>
  </div>
</template>
  <script>
// import LeftComponent from '@/components/dashboard'
export default {
  name: 'leftComponent',
  data() {
    return {
      user: {
        name: 'User'
      }
    }
  },
  methods: {
    toggleCategoriesFunc() {
      const categoriesDiv = document.querySelector('.categories')
      const icon = document.querySelector('.categories-icon')
      categoriesDiv.addEventListener('click', function () {
        categoriesDiv.classList.toggle('expanded')

        if (categoriesDiv.classList.contains('expanded')) {
          icon.classList.add('bi-caret-down-fill')
        } else {
          icon.classList.add('bi-caret-up-fill')
        }
      })
    }
  }
}
</script>
  <style lang="css" scoped>
@import '@/assets/global.css';
.main-container {
  position: absolute;
  width: 100%;
  height: 100%;
  overflow-y: scroll;
}
.main-container::-webkit-scrollbar {
  display: none;
}
.sidebar {
  width: 250px;
  height: 100vh;
  background-color: #f8f9fa;
  padding: 20px;
}
.sidebar .sidenav-header {
  position: relative;
  width: 100%;
  height: 20%;
}
.sidebar .sidenav-header .logo {
  position: relative;
  width: 35px;
  height: 35px;
  background: url('@/assets/images/profile.png');
  background-position: center;
  background-size: cover;
  border-radius: 50%;
}

.sidebar a {
  display: block;
  color: #343a40;
  padding: 10px;
  margin-bottom: 10px;
  text-decoration: none;
  border-radius: 5px;
}

.sidebar .submenu a {
  padding-left: 30px;
  font-size: 0.9rem;
}

.search-bar {
  margin-bottom: 20px;
}

.btn-account {
  margin-bottom: 20px;
}

.sidebar .collapse .submenu {
  margin-left: 20px;
}
.categories-container button {
  border: none;
}

.categories {
  width: auto;
  height: 10%;
  overflow: hidden;
  transition: height 5s ease;
  padding: 10px;
  cursor: pointer;
}

.categories ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

.categories.expanded {
  height: auto;
}
.categories ul li .link {
  margin: 0;
  padding: 0;
}
.link:hover {
  transform: translateX(5%);
  color: #198754;
}
</style>
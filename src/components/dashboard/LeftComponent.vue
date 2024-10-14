<template>
  <div class="main-container">
    <div class="d-flex flex-column">
      <div class="sidebar">
        <div class="sidenav-header d-flex flex-row align-items-center gap-2">
          <div class="logo pointer"></div>
          <div class="pointer">{{ user.name }}</div>
        </div>

        <router-link
          to="/dashboardView"
          :class="{ 'text-success': $route.path === '/dashboardView' }"
          ><i class="bi bi-house"></i> Home</router-link
        >
        <div class="dropdown my-2 categories-container">
          <button
            class="bg-light dropdown-toggle"
            type="button"
            data-bs-toggle="dropdown"
            aria-expanded="false"
          >
            <i class="bi bi-bookmarks"></i>
            Categories
          </button>

          <ul class="dropdown-menu">
            <router-link
              class="py-0"
              to="/dashboardView"
              :class="{ 'text-success': $route.path === '/dashboardView' }"
              ><i class="bi bi-house"></i> Header</router-link
            >
            <router-link
              class="py-0"
              to="/dashboardView"
              :class="{ 'text-success': $route.path === '/dashboardView' }"
              ><i class="bi bi-house"></i> Footer</router-link
            >
            <router-link
              class="py-0"
              to="/dashboardView"
              :class="{ 'text-success': $route.path === '/dashboardView' }"
              ><i class="bi bi-house"></i> Footer</router-link
            >
            <router-link
              class="py-0"
              to="/dashboardView"
              :class="{ 'text-success': $route.path === '/dashboardView' }"
              ><i class="bi bi-house"></i> Footer</router-link
            >
            <router-link
              class="py-0"
              to="/dashboardView"
              :class="{ 'text-success': $route.path === '/dashboardView' }"
              ><i class="bi bi-house"></i> Footer</router-link
            >
          </ul>
        </div>
        <a href="#"><i class="bi bi-coin"></i> Pricing</a>
        <a href="#"><i class="bi bi-file-earmark-text"></i> My Collections</a>
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
  }
}
</script>
  <style lang="css" scoped>
@import '@/assets/global.css';
.main-container {
  position: absolute;
  width: 100%;
  height: 100%;
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
/* .categories-container .dropdown-menu {
  position: relative;
  height: 50%;
  overflow: scroll;
} */
</style>
<template>
  <div>
    <h1 class="text-dark text-center mt-3">
      Create, Customize, and Reuse <br />
      <span class="text-success fw-bolder">Components</span> Effortlessly
    </h1>
    <p class="text-dark text-center">
      providing reusable, customizable components for building web applications.
    </p>

    <div
      class="action-button container d-flex flex-row align-items-center justify-content-center gap-5 pt-3 px-5"
    >
      <a href="#" class="text-decoration-none signup-link px-2 py-2 btn btn-light"
        >Sign up <i class="bi bi-arrow-right text-dark"></i
      ></a>
      <router-link
        to="/dashboardView"
        class="text-decoration-none text-light bg-dark px-2 py-2 get-started-link"
        >Get Started</router-link
      >
    </div>
  </div>
</template>
<script>
export default {
  name: 'heroComponent'
}
</script>
<style lang="css" scoped>
#hero-content h1 {
  font-size: 3rem;
}
.get-started-link {
  color: var(--clr-secondary);
}
.get-started-link:hover {
  background: rgba(0, 0, 0, 0.2);
}
.get-started-link,
.signup-link {
  border-radius: 5px;
}
</style>
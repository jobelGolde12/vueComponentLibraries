<template>
  <div class="main-container bg-light d-flex flex-row justify-content-center align-items-center">
    <div class="card p-0 shadow-sm">
      <div class="card-header bg-gradient"></div>
      <div class="card-body py-0 px-2 d-flex flex-row justify-content-between align-items-center">
        <div class="d-flex flex-column align-items-center gap-0">
          <i
            class="bi bi-house fs-4 d-block"
            @click="isHomeClickedFunc"
            :class="{ 'text-primary': isClick === true }"
          ></i>
          <div class="d-block name text-primary" v-if="isClick">Home</div>
        </div>

        <div class="d-flex flex-column align-items-center gap-0">
          <i
            class="bi bi-info-circle fs-4 d-block"
            @click="isAboutClickFunc"
            :class="{ 'text-primary': isAboutClick === true }"
          ></i>
          <div class="d-block name text-primary" v-if="isAboutClick">About</div>
        </div>

        <div
          class="plus-holder bg-gradient d-flex flex-row justify-content-center align-items-center"
        >
          <i class="bi bi-plus fs-2 d-block text-light"></i>
        </div>

        <div class="d-flex flex-column align-items-center gap-0">
          <i
            class="bi bi-person fs-4 d-block"
            @click="isProfileClickedFunc"
            :class="{ 'text-primary': isProfileClicked === true }"
          ></i>
          <div class="d-block name text-primary" v-if="isProfileClicked">Profile</div>
        </div>

        <div class="d-flex flex-column align-items-center gap-0">
          <i
            class="bi bi-coin fs-4 d-block"
            @click="myPlanIsClickedFunc"
            :class="{ 'text-primary': myPlanIsClicked === true }"
          ></i>
          <div class="d-block name text-primary" v-if="myPlanIsClicked">My plan</div>
        </div>
      </div>
    </div>
  </div>
</template>
  <script>
export default {
  name: 'dashboardCard',
  data() {
    return {
      isClick: false,
      isAboutClick: false,
      isProfileClicked: false,
      myPlanIsClicked: false
    }
  },
  methods: {
    isAboutClickFunc() {
      this.isAboutClick = true
      this.isClick = false
      this.isProfileClicked = false
      this.myPlanIsClicked = false
    },
    isHomeClickedFunc() {
      this.isClick = true
      this.isAboutClick = false
      this.isProfileClicked = false
      this.myPlanIsClicked = false
    },
    isProfileClickedFunc() {
      this.isProfileClicked = true
      this.isAboutClick = false
      this.isClick = false
      this.myPlanIsClicked = false
    },
    myPlanIsClickedFunc() {
      this.myPlanIsClicked = true
      this.isProfileClicked = false
      this.isAboutClick = false
      this.isClick = false
    }
  }
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
.bg-gradient {
  background-color: #0093e9;
  background-image: linear-gradient(160deg, #0093e9 0%, #80d0c7 100%);
}
.card-header {
  width: 100%;
  height: 50%;
  position: relative;
}
.name {
  transform: translateY(-20%);
}
.plus-holder {
  clip-path: circle(50%);
  width: 3rem;
  cursor: pointer;
}
.bi {
  cursor: pointer;
}
.name {
  font-size: 0.8rem;
  border-bottom: 2px solid #ccc;
}
.plus-holder .bi-plus {
  position: relative;
}
</style>
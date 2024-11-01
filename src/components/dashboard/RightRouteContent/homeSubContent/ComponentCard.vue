<template>
  <div>
    <!-- When user is not searcing  -->
    <div class="card-grid" v-if="SearchData.search === ''">
      <div
        class="card pointer"
        v-for="(data, index) in componentsData"
        :key="data.id"
        @click="toggleOpenComponent(data)"
      >
        <div class="card-img-top">
          <img :src="data.img" alt="Component image" />
        </div>
        <div class="card-body">
          <span class="tag">{{ data.category }}</span>
          <span class="steps">
            <i
              class="bi bi-heart-fill pointer"
              :class="{ 'text-warning ': data.isLiked == true }"
              v-if="data.isLiked == true"
              @click="toggleLikeComponentFunc(index)"
            ></i>
            <i
              class="bi bi-heart pointer"
              :class="{ 'text-warning': data.isLiked == true }"
              v-if="data.isLiked !== true"
              @click="toggleLikeComponentFunc(index)"
            ></i>
          </span>
          <div class="d-flex flex-row justify-content-between align-items-center">
            <h5 class="card-title">{{ data.title }}</h5>
            <i class="bi bi-download"></i>
          </div>
        </div>
      </div>
    </div>

    <div class="card-grid" v-if="SearchData.search !== ''">
      <div
        class="card pointer"
        v-for="(data, index) in SearchData.data"
        :key="data.id"
        @click="toggleOpenComponent(data)"
      >
        <div class="card-img-top">
          <img :src="data.img" alt="Component image" />
        </div>
        <div class="card-body">
          <span class="tag">{{ data.category }}</span>
          <span class="steps">
            <i
              class="bi bi-heart-fill pointer"
              :class="{ 'text-warning ': data.isLiked == true }"
              v-if="data.isLiked == true"
              @click="toggleLikeComponentFunc(index)"
            ></i>
            <i
              class="bi bi-heart pointer"
              :class="{ 'text-warning': data.isLiked == true }"
              v-if="data.isLiked !== true"
              @click="toggleLikeComponentFunc(index)"
            ></i>
          </span>
          <div class="d-flex flex-row justify-content-between align-items-center">
            <h5 class="card-title">{{ data.title }}</h5>
            <i class="bi bi-download"></i>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'componentCard',
  props: ['componentsData', 'SearchData'],
  methods: {
    toggleLikeComponentFunc(index) {
      this.$emit('toggleLikeComponentFunc', index)
    },
    toggleOpenComponent(data) {
      this.$emit('toggleOpenComponent', data)
    }
  }
}
</script>
<style lang="css" scoped>
.card-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  justify-content: center;
}

.card {
  width: 280px;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  border: none;
}

.card-img-top {
  height: 150px;
  background-color: #e9ecef;
  overflow: hidden;
}
.card-img-top img {
  position: relative;
  width: 100%;
  height: 100%;
  transition: 0.5s;
}
.card-img-top img:hover {
  transform: scale(1.1);
  /* transform: brightness(5); */
}
.tag {
  font-size: 12px;
  color: #6c757d;
  border-radius: 12px;
  padding: 2px 8px;
  background-color: #f0f1f2;
  display: inline-block;
}

.steps {
  font-size: 12px;
  color: #6c757d;
  display: inline-block;
  margin-left: 10px;
}

.card-title {
  font-size: 1rem;
  font-weight: 500;
  margin-top: 10px;
}

.card-text {
  font-size: 0.875rem;
  color: #6c757d;
}

.card-footer {
  background-color: white;
  border-top: none;
}
</style>
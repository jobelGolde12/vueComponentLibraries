<template>
  <div
    class="modal p-5"
    :class="{ show: isModalVisible }"
    id="exampleModal"
    tabindex="-1"
    :style="{ display: isModalVisible ? 'block' : 'none' }"
    aria-labelledby="exampleModalLabel"
    aria-hidden="true"
    @click.stop
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="exampleModalLabel">{{ title }}</h1>

          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
            @click="closeModal"
          ></button>
        </div>
        <div class="modal-body flex flex-column">
          <div class="image-container">
            <img :src="img" alt="loading component image" />
          </div>

          <div
            class="footer-content pt-2 d-flex flex-row justify-content-between align-items-center"
          >
            <div class="category">
              Category : <span class="text-success">{{ category }}</span>
            </div>

            <div class="d-flex flex-row gap-3">
              <i
                class="bi bi-eye d-block pointer hover"
                data-bs-toggle="tooltip"
                data-bs-placement="top"
                title="View Code"
              ></i>

              <i
                class="bi bi-copy d-block pointer hover"
                data-bs-toggle="tooltip"
                data-bs-placement="top"
                title="Copy Code"
              ></i>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div v-if="isModalVisible" class="modal-backdrop fade show" @click="closeModal"></div>
</template>
<script>
export default {
  name: 'componentModal',
  props: ['isModalVisible', 'title', 'category', 'img'],
  methods: {
    closeModal() {
      this.$emit('update:isModalVisible', false)
    }
  }
}
</script>
<style lang="css" scoped>
@import '../../assets/global.css';
.modal-dialog {
  min-width: 40%;
}
.modal-body .image-container {
  position: relative;
  width: 100%;
  height: 30%;
}
.image-container img {
  position: relative;
  width: 100%;
  min-height: 10%;
}
</style>
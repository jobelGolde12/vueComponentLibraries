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
          <h1 class="modal-title fs-5" id="exampleModalLabel">Modal</h1>

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
            <img src="../../assets/images/team-icon.svg" alt="loading component image" />
          </div>

          <div
            class="footer-content pt-2 d-flex flex-row justify-content-between align-items-center"
          >
            <div class="category">Category : <span class="text-success">Body</span></div>

            <div>
              <i
                class="bi bi-info-circle"
                data-bs-toggle="tooltip"
                data-bs-placement="top"
                title="Tooltip on top"
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
  props: ['isModalVisible'],
  methods: {
    closeModal() {
      this.$emit('update:isModalVisible', false)
    }
  }
}
</script>
<style lang="css" scoped>
.modal-body .image-container {
  position: relative;
  width: 100%;
  height: 60%;
}
.image-container img {
  position: relative;
  width: 100%;
  height: 80%;
}
</style>
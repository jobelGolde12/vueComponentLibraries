<template>
  <div class="container-fluid d-flex flex-row my-3 ms-5 align-items-center">
    <div class="text-dark me-3">Categories:</div>
    <div class="categories d-flex flex-row gap-3">
      <div
        class="category px-2 py-1 rounded text-dark pointer"
        v-for="data in categories"
        :key="data.index"
        @click="chooseCategoryFunc(data)"
      >
        {{ data }}
      </div>
    </div>
  </div>
</template>
<script>
export default {
  props: ['categories'],
  methods: {
    chooseCategoryFunc(data) {
      this.$emit('chooseCategoryFunc', data)
    }
  }
}
</script>
<style lang="css" scoped>
.category {
  background: rgba(0, 0, 0, 0.1);
  cursor: pointer;
}
.category:hover {
  background: rgba(0, 0, 0, 0.2);
}
</style>
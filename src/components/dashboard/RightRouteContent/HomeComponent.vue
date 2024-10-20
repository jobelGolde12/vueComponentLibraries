<template>
  <div class="main-container">
    <div class="container mt-5">
      <!-- Search Bar -->
      <div class="search-bar input-group mb-3">
        <input type="text" class="form-control" placeholder="Search..." aria-label="Search" />
        <button class="btn btn-outline-secondary" type="button">
          <i class="bi bi-search"></i>
        </button>
      </div>

      <CategoriesList :categories="allCategories" />
      <div class="card-grid">
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
              <i class="bi bi-download" @click.stop="downloadComponentFile(data)"></i>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <ComponentModal
    :isModalVisible="isModalVisible"
    @update:isModalVisible="isModalVisible = $event"
    :title="selectedItem.title"
    :category="selectedItem.category"
    :img="selectedItem.img"
    :path="selectedItem.path"
  />
</template>
    <script>
// import img from '../../../assets/images/vue.png'
import contentLeftImg from '../../../assets/images/everyComponentsImage/centerContent/content-left-img.png'
import contentRightImg from '../../../assets/images/everyComponentsImage/centerContent/content-right-img.png'
import hero1 from '../../../assets/images/everyComponentsImage/hero/hero1.png'
import hero2 from '../../../assets/images/everyComponentsImage/hero/hero2.png'
import ComponentModal from '../ComponentModal.vue'
import CategoriesList from './homeSubContent/categoriesList.vue'
export default {
  name: 'homeComponent',
  data() {
    return {
      componentsData: [
        {
          id: '1',
          title: 'left image',
          name: 'ContentLeftImage',
          category: 'content',
          isLiked: false,
          img: contentLeftImg,
          component: '@components/AllComponentFolder/ContentSection/ContentLeftImage.vue',
          path: '/contentLeftImage'
        },
        {
          id: '2',
          title: 'right image',
          name: 'ContentRightImage',
          category: 'content',
          isLiked: false,
          img: contentRightImg,
          component: '@components/AllComponentFolder/ContentSection/ContentRightImage.vue',
          path: '/contentRightImage'
        },
        {
          id: '3',
          title: 'Hero',
          name: 'Hero1Component',
          category: 'hero',
          isLiked: false,
          img: hero1,
          component: '@components/AllComponentFolder/hero/Hero1Component.vue',
          path: '/hero1Component'
        },
        {
          id: '4',
          title: 'Hero Gradient bg',
          name: 'Hero2Component',
          category: 'hero',
          isLiked: false,
          img: hero2,
          component: '@components/AllComponentFolder/hero/Hero2Component.vue',
          path: '/hero2Component'
        }
      ],
      isModalVisible: false,
      selectedItem: {},
      allCategories: []
    }
  },
  methods: {
    toggleLikeComponentFunc(index) {
      this.componentsData[index].isLiked = !this.componentsData[index].isLiked
      this.isModalVisible = true
    },
    toggleOpenComponent(data) {
      this.isModalVisible = !this.isModalVisible
      this.selectedItem = data
      console.log(this.selectedItem)
    },
    getAllCategoriesFunc() {
      for (let i = 0; i < this.componentsData.length; i++) {
        if (!this.allCategories.includes(this.componentsData[i].category)) {
          this.allCategories.push(this.componentsData[i].category)
        }
      }
    },
    async downloadComponentFile(data) {
      try {
        const response = await fetch(`/download/${data.name}.vue`)
        if (response.ok) {
          const blob = await response.blob()
          const url = window.URL.createObjectURL(blob)
          const a = document.createElement('a')
          a.href = url
          a.download = `${data.name}.vue` // Download with the correct filename
          document.body.appendChild(a)
          a.click()
          a.remove()
        } else {
          console.error('Failed to download file:', response.statusText)
        }
      } catch (error) {
        console.error('Error downloading file:', error)
      }
    }
  },
  components: {
    ComponentModal,
    CategoriesList
  },
  mounted() {
    this.getAllCategoriesFunc()
  }
}
</script>
    <style lang="css" scoped>
@import '../../../assets/global.css';
.main-container {
  width: 100%;
  height: 100%;
  overflow-x: hidden;
}

.search-bar {
  max-width: 500px;
  margin: 20px auto;
}

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
<template>
  <div class="main-container">
    <div class="container mt-5">
      <!-- Search Bar -->
      <form @input.prevent="SearchDataFunc">
        <div class="search-bar input-group mb-3">
          <input
            type="text"
            class="searchBar shadow-sm"
            placeholder="Search..."
            aria-label="Search"
            list="category"
            v-model="SearchData.search"
          />
          <datalist id="category">
            <option :value="data" v-for="data in allCategories" :key="data.index"></option>
          </datalist>
          <button class="btn btn-outline-secondary shadow-sm" type="button">
            <i class="bi bi-search"></i>
          </button>
        </div>
      </form>

      <CategoriesList :categories="allCategories" @chooseCategoryFunc="chooseCategoryFunc" />
      <ComponentCard
        :componentsData="componentsData"
        @toggleLikeComponentFunc="toggleLikeComponentFunc"
        @toggleOpenComponent="toggleOpenComponent"
        :SearchData="SearchData"
      />
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
import ComponentCard from './homeSubContent/ComponentCard.vue'
export default {
  name: 'homeComponent',
  data() {
    return {
      componentsData: [
        {
          id: '1',
          title: 'left image',
          category: 'content',
          isLiked: false,
          img: contentLeftImg,
          component: '@components/AllComponentFolder/ContentSection/ContentLeftImage.vue',
          path: '/contentLeftImage'
        },
        {
          id: '2',
          title: 'right image',
          category: 'content',
          isLiked: false,
          img: contentRightImg,
          component: '@components/AllComponentFolder/ContentSection/ContentRightImage.vue',
          path: '/contentRightImage'
        },
        {
          id: '3',
          title: 'Hero',
          category: 'hero',
          isLiked: false,
          img: hero1,
          component: '@components/AllComponentFolder/hero/Hero1Component.vue',
          path: '/hero1Component'
        },
        {
          id: '4',
          title: 'Hero Gradient bg',
          category: 'hero',
          isLiked: false,
          img: hero2,
          component: '@components/AllComponentFolder/hero/Hero2Component.vue',
          path: '/hero2Component'
        }
      ],
      isModalVisible: false,
      selectedItem: {},
      allCategories: ['All'],
      chooseCategory: [],
      SearchData: {
        search: '',
        data: []
      }
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
    chooseCategoryFunc(data) {
      console.log('Selected category => ' + data)
      for (let i = 0; i < this.componentsData.length; i++) {
        if (this.componentsData[i].category === data) {
          this.chooseCategory.push(this.componentsData[i])
        }
      }
    },
    SearchDataFunc() {
      if (this.SearchData.search !== '') {
        for (let i = 0; i < this.componentsData.length; i++) {
          this.SearchData.data.push(this.componentsData[i])
        }
      }
    }
  },
  components: {
    ComponentModal,
    CategoriesList,
    ComponentCard
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
.search-bar input {
  position: relative;
  width: 80%;
  padding: 0.2rem 0.5rem;
  border: 1px solid rgba(0, 0, 0, 0.1);
}
</style>
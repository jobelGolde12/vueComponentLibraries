import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/leftComponent',
      name: 'leftComponent',
      component: () => import('../components/dashboard/LeftComponent.vue')
    },
    {
      path: '/rightComponent',
      name: 'rightComponent',
      component: () => import('../components/dashboard/RightComponent.vue')
    },
    {
      path: '/dashboardView',
      name: 'dashboardView',
      component: () => import('../views/DashboardView.vue')
    }
  ]
})

export default router

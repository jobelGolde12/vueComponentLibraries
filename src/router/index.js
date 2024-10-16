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
      component: () => import('../views/DashboardView.vue'),
      children: [
        {
          path: '',
          name: 'homeComponent',
          component: () => import('../components/dashboard/RightRouteContent/HomeComponent.vue')
        },
        {
          path: '/profileComponent',
          name: 'rofileComponent',
          component: () => import('../components/dashboard/RightRouteContent/ProfileComponent.vue')
        },
        {
          path: '/trialComponent',
          name: 'trialComponent',
          component: () => import('../components/welcome/TrialComponent.vue')
        }
      ]
    },
    {
      path: '/pricingComponent',
      name: 'pricingComponent',
      component: () => import('../components/welcome/PricingComponent.vue')
    }
  ]
})

export default router

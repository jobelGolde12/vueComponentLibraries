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
        }
      ]
    },
    {
      path: '/pricingComponent',
      name: 'pricingComponent',
      component: () => import('../components/welcome/PricingComponent.vue')
    },
    {
      path: '/loginComponent',
      name: 'loginComponent',
      component: () => import('../components/welcome/LoginComponent.vue')
    },
    {
      path: '/signupComponent',
      name: 'signupComponent',
      component: () => import('../components/welcome/SignupComponent.vue')
    },

    //pag in click ni user an view icon
    {
      path: '/contentLeftImage',
      name: 'contentLeftImage',
      component: () =>
        import('../components/AllComponentFolder/contentSection/ContentLeftImage.vue')
    },
    {
      path: '/contentRightImage',
      name: 'contentRightImage',
      component: () =>
        import('../components/AllComponentFolder/contentSection/ContentRightImage.vue')
    },
    {
      path: '/hero1Component',
      name: 'hero1Component',
      component: () => import('../components/AllComponentFolder/hero/hero1Component.vue')
    },
    {
      path: '/hero2Component',
      name: 'hero2Component',
      component: () => import('../components/AllComponentFolder/hero/Hero2Component.vue')
    },
    {
      path: '/adminDashboard',
      name: 'adminDasboard',
      component: () => import('../views/AdminDashboard.vue')
    }
  ]
})

export default router

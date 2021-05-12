import Vue from 'vue'
import VueRouter from 'vue-router'
// import Home from '../views/Home.vue'
import SingIn from '../components/SingIn.vue'
import SingUp from '../components/SingUp.vue'
import Case from '../components/Case.vue'
import Jenkins from '../components/Jenkins.vue'
import Report from '../components/Report.vue'
import Task from '../components/Task.vue'
import User from '../components/User.vue'

// 解决router更新路由冗余问题
const originalPush = VueRouter.prototype.push

VueRouter.prototype.push = function push(location){
  return originalPush.call(this, location).catch(err => err)
}

Vue.use(VueRouter)

const routes = [
  // {
  //   path: '/',
  //   name: 'Home',
  //   component: Home
  // },
  // {
  //   path: '/about',
  //   name: 'About',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  // }
  {
    path:'/',
    name:'SingIn',
    component:SingIn
  },
  {
    path:'/sing-up',
    name:'SingUp',
    component:SingUp
  },
  {
    path:'/case',
    name:'Case',
    component:Case
  },
  {
    path:'/jenkins',
    name:'Jenkins',
    component:Jenkins
  },
  {
    path:'/report',
    name:'Report',
    component:Report
  },
  {
    path:'/task',
    name:'Task',
    component:Task
  },{
    path:'/user',
    name:'User',
    component:User
  }
]

const router = new VueRouter({
  routes
})

export default router

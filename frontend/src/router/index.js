import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Task from '../views/Task.vue'
import Monitor from '../views/Monitor.vue'
import Operation from '../views/Operation.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/home', component: Home },
  { path: '/task', component: Task },
  { path: '/monitor', component: Monitor },
  { path: '/operation', component: Operation }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router

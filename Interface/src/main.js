// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App'
import axios from 'axios'
import ProjectList from './components/ProjectList'
import Login from './components/Login'
import Register from './components/Register'
import AddProject from './components/CreateProject'
import UpdateProject from './components/UpdateProject'
import CaseList from './components/CaseList'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import CreateCase from "./components/CreateCase";
import UpdateCase from "./components/UpdateCase";

Vue.use(ElementUI);
Vue.use(VueRouter);

Vue.config.productionTip = false;
axios.defaults.withCredentials = true;
Vue.prototype.$bus = new Vue();
Vue.prototype.$axios = axios;
axios.defaults.baseURL = "http://127.0.0.1:8000/";
axios.defaults.headers.post['Content-Type'] = 'application/json; charset=UTF-8';
axios.defaults.headers.get['Content-Type'] = 'application/json; charset=UTF-8';
axios.defaults.headers.put['Content-Type'] = 'application/json; charset=UTF-8';
axios.defaults.headers.delete['Content-Type'] = 'application/json; charset=UTF-8';
if (localStorage.token !== '') {

  axios.defaults.headers.post['Authorization'] = "JWT " + localStorage.token;

  axios.defaults.headers.get['Authorization'] = "JWT " + localStorage.token;

  axios.defaults.headers.put['Authorization'] = "JWT " + localStorage.token;

  axios.defaults.headers.delete['Authorization'] = "JWT " + localStorage.token;
}


const router = new VueRouter({
  mode: 'history',
  base: __dirname,
  linkActiveClass: "mui-active",
  routes: [
    {path: "/project/", component: ProjectList, meta: {requireAuth: true}},
    {path: "/login/", component: Login, meta: {requireAuth: true}},
    {path: "/register_user/", component: Register, meta: {requireAuth: true}},
    {path: "/add_project/", component: AddProject, meta: {requireAuth: true}},
    {
      path: "/update_project/:id",
      component: UpdateProject,
      meta: {requireAuth: true}
    },
    {
      path: "/testcase/", component: CaseList, meta: {requireAuth: true}
    },
    {
      path: "/add_case/", component: CreateCase, meta: {requireAuth: true}
    },
    {
      path: "/update_testcase/:id", component: UpdateCase, meta: {requireAuth: true}
    },


  ]
});


/* eslint-disable no-new */
new Vue({
  router,
  template: `
    <div id="app">
    <router-view></router-view>
    </div>
  `

}).$mount("#app")


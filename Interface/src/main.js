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
import UserList from "./components/UserList";
import CreateUser from "./components/CreateUser";
import UpdateUser from "./components/UpdateUser";
import ResetPwd from "./components/ResetPwd";
import schart from "./components/schart";
import echarts from 'echarts'
import TimeingTask from "./components/TimeingTask";

Vue.use(ElementUI);
Vue.use(VueRouter);

Vue.config.productionTip = false;
axios.defaults.withCredentials = true;
Vue.prototype.$bus = new Vue();
Vue.prototype.$axios = axios;
axios.defaults.baseURL = "http://127.0.0.1:8000/";
// axios.defaults.baseURL = "http://121.196.217.69:8082/";
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
      path: "/update_testcase/:id",
      component: UpdateCase,
      meta: {requireAuth: true}
    },
    {
      path: "/user/",
      component: UserList,
      meta: {requireAuth: true}
    },
    {
      path: "/add_user/",
      component: CreateUser,
      meta: {requireAuth: true}
    },
    {
      path: "/user_update/:id",
      component: UpdateUser,
      meta: {requireAuth: true}
    },
    {
      path: "/pwd_reset/:id",
      component: ResetPwd,
      meta: {requireAuth: true}
    },
    {
      path: "/echarts",
      component: schart,
      meta: {requireAuth: true}
    },
       {
      path: "/timing_task",
      component: TimeingTask,
      meta: {requireAuth: true}
    },
  ]
});


axios.interceptors.response.use(
  response => {
    return response;
  },
  error => {
    if (error.response) {
      if (error.response.status == 401) {
          router.push('/login');
        Vue.prototype.$message({
            type: 'info',
            message: '未登陆'
          });
      }
    }

  }
);
/* eslint-disable no-new */
new Vue({
  router,
  template: `
    <div id="app">
    <router-view></router-view>
    </div>
  `

}).$mount("#app")


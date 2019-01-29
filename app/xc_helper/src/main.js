// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import {post, fetch, patch, put, del} from "./util/http";
import Element from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css';

Vue.use(Element)
Vue.config.productionTip = false

//定义全局变量
Vue.prototype.$post = post;
Vue.prototype.fetch = fetch;
Vue.prototype.patch = patch;
Vue.prototype.put = put;
Vue.prototype.del = del;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: {App},
  template: '<App/>',
  render: h => h(App)
})

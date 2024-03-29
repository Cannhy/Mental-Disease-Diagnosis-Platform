// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import axios from 'axios'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import App from './App'
import router from './router'
import cookie from './util/cookie'
import './assets/font/fontFestival.css'

Vue.use(ElementUI)
Vue.config.productionTip = false
Vue.prototype.$http = axios
Vue.prototype.$url = 'http://127.0.0.1:8000/'
Vue.prototype.cookie = cookie

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: {App},
  template: '<App/>',
  data: function () {
    return {
      isCollapsed: true
    }
  },
  methods: {
    handleOpen (key, keyPath) {
      console.log(key, keyPath)
    },
    handleClose (key, keyPath) {
      console.log(key, keyPath)
    }
  }
})

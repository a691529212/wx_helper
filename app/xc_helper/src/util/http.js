import axios from 'axios';
// import {Message} from 'element-ui';

axios.defaults.timeout = 5000;
axios.defaults.baseURL = 'http://127.0.0.1:7587';

//http request 拦截器
axios.interceptors.request.use(
  config => {
    // const token = getCookie('sign')
    config.headers = {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
    // if (token) {
    //   config.params = {'token': token}
    // }
    return config
  },
  error => {
    return Promise.reject(error)
  }
);

//http response 拦截器
axios.interceptors.response.use(
  response => {
    if (response.data.errorCode == 2) {
      router.push({
        path: "/login",
        query: {redirect: router.currentRoute.fullPath}//从哪个页面跳转
      })
    }
    return response
  },
  error => {
    return Promise.reject(error)
  }
);

/**
 * get
 * @param url
 * @param params
 * @returns {Promise<any>}
 */
export function fetch(url, params = {}) {
  return new Promise((resolve, reject) => {
    axios.get(url, {
      params: params
    }).then(response => {
      resolve(response.data);
    }).catch(err => {
      reject(err);
    })
  })
}

/**
 * 封装post请求
 * @param url
 * @param data
 * @returns {Promise<any>}
 */
export function post(url, data = {}) {
  console.log(url)
  return new Promise((resolve, reject) => {
    axios.post(url, data)
      .then(response => {
        resolve(response.data);
      }, err => {
        reject(err)
      })
  })
}

/**
 * 封装patch请求
 * @param url
 * @param data
 * @returns {Promise}
 */
export function patch(url, data = {}) {
  return new Promise((resolve, reject) => {
    axios.patch(url, data)
      .then(response => {
        resolve(response.data);
      }, err => {
        reject(err)
      })
  })
}

/**
 * 封装put请求
 * @param url
 * @param data
 * @returns {Promise}
 */
export function put(url, data = {}) {
  return new Promise((resolve, reject) => {
    axios.put(url, data)
      .then(response => {
        resolve(response.data);
      }, err => {
        reject(err)
      })
  })
}

/**
 * 封装delete请求
 * @param url
 * @param data
 * @returns {Promise<any>}
 */
export function del(url, data = {}) {
  return new Promise((resolve, reject) => {
    axios.delete(url, data)
      .then(response => {
        resolve(response.data);
      }, err => {
        reject(err)
      })
  })
}


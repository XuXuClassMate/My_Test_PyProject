import axios from 'axios'
var instance = axios.create({
    headers:{
        'Content-Type':'application/json'
    },
    baseURL:'http://stug.ceshiren.com:8089/'
})

instance.interceptors.request.use(config=>{
    // 把本地存储的token放在http请求中发送出去
  if(localStorage.getItem('token')){
    config.headers.common['token']=localStorage.getItem('token')
  }
  return config
})

export default instance
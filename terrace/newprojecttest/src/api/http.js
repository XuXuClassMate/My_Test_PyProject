import axios from 'axios'
var instance = axios.create({
    headers:{
        'Content-Type':'application/json'
    },
    baseURL:'http://stug.ceshiren.com:8089/'
})
export default instance
import axios from 'axios'
var instance = axios.create({
    headers:{
        'Content-Type':'application/json'
    },
    baseURL:''
})
export default instance
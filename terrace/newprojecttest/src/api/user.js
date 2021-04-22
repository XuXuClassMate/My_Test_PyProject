import axios from './http'

const user = {
    SingIn(){
        // 登录接口
        return axios.post('/user/login', params)
    }, 
    SingUp(){
        // 注册接口
        return axios.post('/user/register', params)
    }
}
export default user
import axios from './http'

const user = {
    SingIn(params){
        // 登录接口
        return axios.post('/user/login', params)
    }, 
    SingUp(params){
        // 注册接口
        return axios.post('/user/register', params)
    }
}
// 接口返回
export default user
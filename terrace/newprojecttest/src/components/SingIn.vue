<template>
    <div  class="login-form">
        <h1>登录</h1>
        <v-text-field label="用户名" v-model="username" type="username"></v-text-field>
        <v-text-field label="密码"  v-model="password" type="password"></v-text-field>
        <v-btn depressed @click="login()" color="primary" style="padding: 8px; border-radius: 6px; margin: 0 10px;">登录</v-btn> 
        <v-btn depressed @click="singup()" style="padding: 8px; border-radius: 6px; margin: 0 10px;">注册</v-btn>
        <!-- <div style="margin-top: 10px"><v-btn  color="error">找回密码</v-btn></div>   -->
    </div>
</template>
<script>
export default {
    data(){
        return{
            username : '',
            password : ''
        }
    },  
    methods:{
        singup(){
            // console.log('123')
            this.$router.push({name:'SingUp'})
        },
        login(){
            let post_data = {
                username: this.username,
                password: this.password,
            }
            console.log(post_data)
            this.$api.user.SingIn(post_data).then(res=>{
                console.log(res)
                // 把登录获取到的token存储下来，以便后续调用
                localStorage.setItem('token',res,data.data.token)
                localStorage.setItem('username'.this.username)
                this.$router.push({name:'Jenkins'})
                //case页面作为登陆成功的默认展页面
                this.$router.push({name:'Case'})
            })
        }
    }
    
}
</script>
<style scoped>
.login-form{
    width: 300px;
    margin: 0 auto;
    text-align: center;
    margin: auto;
    /* width: 20%; 
    border: 1px solid;
    padding: 5px; */
} 

</style>

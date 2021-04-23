<template>
    <div  class="login-form">
        <h1>登录</h1>
        <v-text-field label="用户名" v-model="username" type="username"></v-text-field>
        <v-text-field label="密码"  v-model="password" type="password"></v-text-field>
        <v-btn depressed @click="login()" color="primary">登录</v-btn> 
        <v-btn depressed @click="singup()">注册</v-btn>
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
            console.log('123')
            this.$router.push({name:'SingUp'})
        },
        login(){
            let post_data = {
                username: this.username,
                password: this.password,
            }
            this.$api.user.SingIn(post_data).then(res=>{
                console.log(res)
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

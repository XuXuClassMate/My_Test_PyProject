<template>
    <div  class="login-form">
        <h1>登录</h1>
        <v-text-field label="用户名" type="username"></v-text-field>
        <v-text-field label="密码" type="password"></v-text-field>
        <v-btn depressed color="primary">登录</v-btn> 
        <v-btn depressed @click="singup()">注册</v-btn>
        <!-- <div style="margin-top: 10px"><v-btn  color="error">找回密码</v-btn></div>   -->
    </div>
</template>
<script>
export default {
    methods:{
        singup(){
            console.log('123')
        }
    }
    
}
</script>
<style scoped>
.login-form{
    width: 300px;
    margin: 0 auto;
    text-align: center;
    /* margin: auto;
    width: 20%; 
    border: 1px solid;
    padding: 5px; */
} 

</style>

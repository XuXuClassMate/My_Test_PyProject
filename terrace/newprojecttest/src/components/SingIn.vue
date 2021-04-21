<template>
    <div  class="login-form">
        <h1>登录</h1>
        <v-text-field label="用户名" type="username"></v-text-field>
        <v-text-field label="密码" type="password"></v-text-field>
        <v-btn depressed color="primary">登录</v-btn> 
        <!-- <v-btn depressed color="error">找回密码</v-btn> -->
        <v-btn depressed disabled>注册</v-btn>
          
  
        
    </div>
</template>
<script>
export default {
    
}
</script>
<style scoped>
.login-form{
    width: 300px;
    margin: 0 auto;
    text-align: center;
}

</style>

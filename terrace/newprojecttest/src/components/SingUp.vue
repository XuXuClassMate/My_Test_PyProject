<template>
    <div class='singup'>
        <h1>注册</h1>
        <v-text-field v-model="username" label='用户名' type='user name'></v-text-field>
        <v-text-field v-model="password" label='密码' type='password'></v-text-field>
        <v-text-field v-model="email" label='邮箱' type_id='email'></v-text-field>
        <v-btn depressed color="primary" @click="register()" style="padding: 8px; border-radius: 6px; margin: 0 10px;">注册</v-btn>
        <v-btn depressed @click="singIn()" style="padding: 8px; border-radius: 6px; margin: 0 10px;" text id="singIn">去登陆</v-btn>     
    </div> 
</template>
<script>
export default {
    data(){
        return{
            username:'',
            password:'',
            email:''
        }
    },
    methods:{
        singIn(){ 
            // 这里为什么和注册接口不是一个模式->this.$api.user.SingIn调用格式
            this.$router.push({name:'SingIn'})
        },
        register(){
            let post_data = {
                username : this.username,
                password : this.password,
                email : this.email,
            }
            this.$api.user.SingUp(post_data).then(res=>{
                console.log(res)
            })
        }
    }

}
</script>

<style scoped>
.singup{
    width: 300px;
    margin: 0 auto;
    text-align: center;
    margin: auto;
    /* width: 20%; 
    border: 1px solid;
    padding: 5px; */
} 


</style>
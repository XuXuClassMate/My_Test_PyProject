<template>
    <div>
        <template>
            <v-tabs fixed-tabs background-color="indigo" dark :value="4">
                <v-tab @click="$router.push({name:'Case'})">用例管理</v-tab>
                <v-tab @click="$router.push({name:'Task'})">任务管理</v-tab>
                <v-tab @click="$router.push({name:'Jenkins'})">Jenkins管理</v-tab>
                <v-tab @click="$router.push({name:'Report'})">测试报告管理</v-tab>
                <v-tab @click="$router.push({name:'User'})">用户管理</v-tab>
            </v-tabs>
        </template>
        User
    </div>
</template>

<script>
export default {
    data(){
        return{

        }
    },
    methods:{

    }
}
</script>

<style scoped>

</style>


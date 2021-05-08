<template>
    <div>
        <template>
            <v-tabs fixed-tabs background-color="indigo" dark>
                <v-tab @click="$router.push({name:'Case'})">用例管理</v-tab>
                <v-tab @click="$router.push({name:'Task'})">任务管理</v-tab>
                <v-tab @click="$router.push({name:'Jenkins'})">Jenkins管理</v-tab>
                <v-tab @click="$router.push({name:'Report'})">测试报告管理</v-tab>
            </v-tabs>
        </template>
        Report
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


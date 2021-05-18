<template>
    <div>
        <template>
            <v-tabs fixed-tabs background-color="indigo" dark :value="0">
                <v-tab @click="$router.push({name:'Case'})">用例管理</v-tab>
                <v-tab @click="$router.push({name:'Task'})">任务管理</v-tab>
                <v-tab @click="$router.push({name:'Jenkins'})">Jenkins管理</v-tab>
                <v-tab @click="$router.push({name:'Report'})">测试报告管理</v-tab>
                <v-tab @click="$router.push({name:'User'})">用户管理</v-tab>
            </v-tabs>
        </template>
        <v-btn color='success' class='btn'>新增计划</v-btn>
        <v-btn color='primary' class='btn'>新建用例</v-btn>
        <p>
            <br>  <!--顶部空行 -->
            <br/>
        </p>
        <template>
            <v-data-table
                v-model="selected"
                :headers="headers"
                :items="desserts"
                :single-select="singleSelect"
                item-key="name"
                show-select
                class="elevation-1">
            </v-data-table>
        </template>
    </div>
</template>

<script>
export default {
    data(){
        return{
            selected: [],
            headers: [{
                text:'id',
                value:''
            },{
                text:'用例名称',
                value:''
            },{
                text:'数据',
                value:''
            },{
                text:'操作',
                value:''
            }], 
            desserts: []
        }
    },
    methods:{

    }
}
</script>

<style scoped>
.btn{
    margin: 10px;
    float: right   
}
</style>


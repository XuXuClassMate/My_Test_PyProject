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
        <v-dialog v-model="editDialog" max-width="500px">
            <v-card>
                <v-card-title>修改测试用例</v-card-title>
                <v-card-text>
                    <v-container>
                        <v-text-field label="用例名称" v-model="editItem.caseName"></v-text-field>
                        <v-textarea label="用例详情" v-model="editItem.caseDate"></v-textarea>
                        
                    </v-container>
                </v-card-text>
                    <v-spacer></v-spacer>
                    <v-but color="parimary" @click="confirmEdit()">确定</v-but>
                    <v-but color="parimary" text @click="editDialog = false ">取消</v-but>
            </v-card>
        </v-dialog>
        <v-dialog v-model="createdTask" max-width="500px">
            <v-card>
                <v-card-title>新增测试计划</v-card-title>
                <v-card-text>
                    <v-container>
                        <v-text-field label="任务名称" v-model="addTask.name"></v-text-field>
                        <v-textarea label="备注" v-model="addTask.remark"></v-textarea>
                        
                    </v-container>
                </v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="primary" @click="newTask()">确定</v-btn>
                    <v-btn color="primary" text @click="createdTask = false ">取消</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>


        <v-dialog v-model="addDialog" max-width="500px">
        <v-card>
            <v-card-title>
                添加测试用例
            </v-card-title>
            <v-card-text>
                <v-container>
                    <v-text-field label="用例名称" v-model="addItem.name"></v-text-field>
                    <v-select label="用例类型" :items='selectItem' v-model="addItem.type"></v-select>
                    <v-file-input label="请上传用例" outlined v-model="addItem.file" v-if="addItem.type == '文件'"></v-file-input>
                    <v-textarea label="用例详情" v-model="addItem.data" v-if="addItem.type == '文本'"></v-textarea>
                    <v-text-field label="备注" v-model="addItem.remark"></v-text-field>
                </v-container> 
            </v-card-text>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="primary" @click="addCase()">确定</v-btn>
                <v-btn color="primary" text @click="addDialog = false">取消</v-btn>
            </v-card-actions>
        </v-card>
        </v-dialog>

        <v-btn color='success' class='btn' @click="createdTask=true">新增计划</v-btn>
        <v-btn color='primary' class='btn' @click="addDialog = true">新建用例</v-btn>
        <p>
            <br>  <!--顶部空行 -->
            <br/>
        </p>
        <template>
            <v-data-table
                v-model="selected"
                :headers="headers"
                :items="desserts"
                item-key="name"
                show-select
                class="elevation-1">
                <template v-slot:[`item.operate`] = {item}>     <!-- 当前点击行的信息 -->
                    <v-btn color='primary' text small @click="editCase(item)">编辑</v-btn>
                    <v-btn color='error' text small @click="deleteCase(item)">删除</v-btn>

                </template>
            </v-data-table>
        </template>
    </div>
</template>

<script>
export default {
    data(){
        return{
            addDialog:false,
            editDialog:false,
            createdTask:false,
            selectItem:['文本', '文件'],
            editItem:{},
            addTask:{
                name:'',
                remark:''
            },
            addItem:{
                name:'',
                type:'',
                file:'',
                data:'',
                remark:''
            },
            // 选中的数据
            selected: [],
            // 表头数据
            headers: [{
                text:'id',
                value:'id'
            },{
                text:'用例名称',
                value:'caseName'
            },{
                text:'用例详情',
                value:'caseDate'
            },{
                text:'操作',
                value:'operate'
            }], 
            // 表中数据
            desserts: []
        }
    },
    created(){
        let post_data={
            pageNum:1,
            pageSize:10,

        };
        this.$api.cases.getList(post_data).then(res=>{
            console.log(res)
            this.desserts =res.data.data.data
        })
    },
    methods:{
        addCase(){
            if(this.addItem=="文本"){
                let post_data={
                caseDate:this.addItem.data,
                caseName:this.addItem.name,
                remark:this.addItem.remark
                }
                this.$api.cases.createcaseByTest(post_data).then(res=>{
                    console.log(res)
                    this.addDialog = false  //关闭新建测试用例弹窗
                })
            }else if(this.addItem=="文件"){
                let post_data=new FormData()
                post_data.append('casefile',this.addItem.file)
                post_data.append('caseDate',this.addItem.remark)
                post_data.append('caseName',this.addItem.name)
                this.$api.cases.createcaseByFile(post_data).then(res=>{
                    console.log(res)
                })
            }
            console.log(this.addItem)
            // 关闭弹窗
            this.addDialog=false
            // 刷新页面
            post_data={
            pageNum:1,
            pageSize:10,

            },
            this.$api.cases.getList(post_data).then(res=>{
                console.log(res)
                this.desserts =res.data.data.data
            })           
        },
        editCase(item){
            this.editDialog=true
            this.editItem=item
        },
        confirmEdit(item){
            let post_data={
                caseData:this.editItem.casedata,
                caseName:this.editItem.casename,
                caseType:this.editItem.casetype,
                id:this.editItem.id,
                remark:this.editItem.remark
                }
            this.$api.cases.editCase(post_data).them(res=>{
                console.log(res)
                this.editDialog = false
                post_data={
                    pageNum:1,
                    pageSize:10,

                },
                this.$api.cases.getList(post_data).then(res=>{
                    console.log(res)
                    this.desserts =res.data.data.data
                })
            })

        },
        newTask(){
            console.log(this.selected)
            let caseIdList=[];
            for (let i = 0; i < this.selected.length; i++) {
                caseIdList.push(this.selected[i].id);              
            }   
            let post_data={
                caseIdList:caseIdList,
                testTask:{
                    name:this.addTask.name,
                    remark:this.addTask.remark,
                    testJenkinsId:1
                }
            }
            this.$api.cases.createTask(post_data).then(res=>{
                console.log(res)
            })
        },
        deleteCase(item){
            let post_data = {
                caseId:item.id
            }
            this.$api.cases.deleteCase(post_data).then(res=>{
                console.log(res)  
            })
        }   
    },
}
</script>

<style scoped>
.btn{
    margin: 10px;
    float: right   
}
</style>


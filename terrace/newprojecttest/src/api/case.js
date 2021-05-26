import axios from './http'

const cases = {
    getList(params){
        // 获取测试用例的接口
        return axios.get('testCase/list', {params})
    },
    createcaseByTest(params){
        // 文本形式添加测试用例的接口
        return axios.post('testCase/text', params)
    },
    createcaseByFile(params){
        // 文件形式添加测试用例的接口
        return axios.post('testCase/file',{
            methods:'post',
            data:params,
            header:{'Content-type':'multipart/form-data'}
        })
    },
    deleteCase(params){
        // delete case api
        return axios.delete('/testcase/'+params.caseID,params)
    },
    editCase(params){
        // put case api
        return axios.put('/testcase/'+params)
    },
    createTask(params){
        // add testtask 测试任务
        return axios.post('/task', params)
    }
}
export default cases
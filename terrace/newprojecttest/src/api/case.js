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
        return axios.post('testCase/text', params)
    }

}
export default cases
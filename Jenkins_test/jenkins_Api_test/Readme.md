**接口功能自动化测试程序**
运行环境：
- python3
- pytest
- allure report
- git

依赖准备：
pip install allure-pytest

运行命令：
pytest -sv test/weather_test.py --alluredir ./allure-results

 #### jenkins自动化测试结果
  - [执行日志](./Jenkins_test/jenkins_Api_test/email_log/build.log)
  - [执行结束已发送邮件](./Jenkins_test/jenkins_Api_test/email_log/Jenkins构建提示：0412newjob%20-%20Build%20%23%201%20-%20Successful!.eml)

![images](allure-report/data/Lark20210414-093223.png)
![iamges](allure-report/data/Lark20210414-093230.png)

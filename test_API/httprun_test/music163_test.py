# NOTE: Generated By HttpRunner v3.1.4
# FROM: music163.json


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseMusic163(HttpRunner):

    config = Config("testcase name")

    teststeps = [
        Step(
            RunRequest("/")
            .get("https://music.163.com/")
            .with_headers(
                **{
                    "header": "header"
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "text/html;charset=utf8")
        ),
    ]


if __name__ == "__main__":
    TestCaseMusic163().test_start()

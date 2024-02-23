# DolphinPTTest Readme
（Dolphin Performance Test）

### This is based on the DolphinScheduler API for API performance testing
（Non-restful APIs do not write test cases now）

## Test case for resources

- [X] Login
- [ ] Tenant
- [X] User
- [ ] Env
- [ ] Timing
- [ ] Calendar
- [ ] Card
- [ ] AlertPlgin
- [ ] AlertGroup
- [ ] DataSource
- [X] Project




```shell
../DolphinTest/DolphinPTTest/test
locust -f page/ -R
```
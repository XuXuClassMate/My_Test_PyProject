from mitmproxy import ctx


# 实现请求计算器，每来一个请求，计算器 + 1 ，并且打印
class Counter:
    def __init__(self):
        self.num = 0

    def request(self, flow):
        self.num = self.num + 1
        ctx.log.info("######==============================================#####")
        # ctx.log.info("We've seen %d flows" % self.num)
        ctx.log.info(f'这是第{self.num}条请求')


addons = [
    Counter()
]
# 运行指令
# mitmdump -s .py路径

""" 测试小游戏 """
import random

# Computer:电脑
# User : 用户

print('游戏说明：\n  猜拳游戏 ：石头 ==> 1;剪刀 ==> 2;布 ==> 3; 停止游戏 ==> 0\n 请输入对用阿拉伯数字')


class game:
    while True:
        Computer = random.randint(1, 3)
        User = int(input('请输入你的选择：'))
        if len(User) == 1:
            if 0 <= User <= 3:
                if User == 0:
                    print('游戏结束')
                    break
                elif User > Computer:
                    print('玩家获胜')
                elif User < Computer:
                    print('电脑获胜')
                elif User == Computer:
                    print('平局')
            else:
                print("输入不合规，请重新开始")
        else:
            print("输入不合规，请重新开始")

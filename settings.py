from random import randint
class Settings():
    "存储所有设置的类"

    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width = 400
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        #蛇头设置
        self.sh_speed_factor = 0.1
        self.sh_width = 10
        self.sh_height = 10
        self.sh_color = 69, 185, 46

        #食物设置
        self.food_radius  = 10
        self.food_color = 0, 0, 0

        #身体设置
        self.body_color = (0, 0, 0)

    @staticmethod
    def random_xy():
        """"获得随机的X，值Y"""
        x = randint(0, 400)
        y = randint(0, 600)
        return (x, y)
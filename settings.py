class Settings():
    "存储所有设置的类"

    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width = 600
        self.screen_height = 400
        self.bg_color = (230, 230, 230)

        #蛇头设置
        self.sh_speed_factor = 1
        self.sh_width = 10
        self.sh_height = 10
        self.sh_color = 69, 185, 46
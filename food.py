import pygame
from pygame.sprite import Sprite

from settings import Settings

class Food(Sprite):
    """一个对食物管理的类"""
    def __init__(self, screen, gs_settings):
        self.screen = screen
        self.flag_draw = False
        # self.rect = pygame.Rect(0, 0, gs_settings.sh_width,
        #                         gs_settings.sh_height)

        self.center = Settings.random_xy()
        self.color = gs_settings.food_color
        self.radius = gs_settings.food_radius
        #防止首次调用 check_collision（）出错
        self.rect = pygame.draw.circle(self.screen, self.color, self.center, self.radius)

    def draw_food(self):
        """绘制圆形食物"""
        self.rect =  pygame.draw.circle(self.screen, self.color, self.center, self.radius)

    def update_center(self):
        self.center = Settings.random_xy()
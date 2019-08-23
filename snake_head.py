import pygame
from pygame.sprite import Sprite

from settings import Settings


class SnakeHead(Sprite):
    """蛇的头部进行管理的类"""

    def __init__(self, gs_settings, screen):
        """初始化蛇头并设置其初始位置"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.gs_settings = gs_settings

        #创建一个表示蛇头的矩形，在设置正确的位置
        self.rect = pygame.Rect(0, 0, gs_settings.sh_width,
                                gs_settings.sh_height)

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        self.inner_color = Settings.random_rgb()
        self.color = gs_settings.sh_color

        #移动标志
        self.moving_direction="right"

    def draw_sh(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        # pygame.draw.rect(self.screen, self.color, self.rect)
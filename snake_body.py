import pygame
from pygame.sprite import Sprite

from random import randint

class SnakeBody(Sprite):
    """蛇的头部进行管理的类"""

    def __init__(self, gs_settings, screen, snake_head):
        """初始化蛇头并设置其初始位置"""
        super(SnakeBody, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.gs_settings = gs_settings
        self.sh = snake_head

        self.body_rect = pygame.Rect(0, 0, self.gs_settings.sh_width,
                                     self.gs_settings.sh_height)

    def draw_body(self):
        self.color = (randint(0,255), randint(0,255), randint(0,255),)
        pygame.draw.rect(self.screen, self.color, self.rect)
    def update(self):
        if self.moving_direction == "right" :
            self.centerx += self.gs_settings.sh_speed_factor
        elif self.moving_direction == "left" :
            self.centerx -= self.gs_settings.sh_speed_factor
        elif self.moving_direction == "up" :
            self.centery -= self.gs_settings.sh_speed_factor
        elif self.moving_direction == "down":
            self.centery += self.gs_settings.sh_speed_factor
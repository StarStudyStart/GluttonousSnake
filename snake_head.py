import pygame
from pygame.sprite import Sprite

class SnakeHead(Sprite):
    """蛇的头部进行管理的类"""

    def __init__(self, gs_settings, screen):
        """初始化蛇头并设置其初始位置"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #创建一个表示蛇头的矩形，在设置正确的位置
        self.rect = pygame.Rect(0, 0, gs_settings.sh_width,
                                gs_settings.sh_height)

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        self.color = gs_settings.sh_color
        self.speed_factor = gs_settings.sh_speed_factor
        
        #移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        """根据移动标志调整飞船位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 1
        if self.moving_up and self.rect.top > 0:
            self.rect.centery -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 1

    def draw_sh(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

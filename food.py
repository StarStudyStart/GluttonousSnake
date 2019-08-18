import pygame


class Food():
    """一个对食物管理的类"""
    def __init__(self, screen, gs_settings):
        self.screen = screen

        # self.rect = pygame.Rect(0, 0, gs_settings.sh_width,
        #                         gs_settings.sh_height)

        self.center = gs_settings.food_center
        self.color = gs_settings.food_color
        self.radius = gs_settings.food_radius

    def draw_food(self):
        """绘制圆形食物"""
        pygame.draw.circle(self.screen, self.color, self.center, self.radius)

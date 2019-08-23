# /usr/env/python3
# -*- coding:utf-8-*-

import sys
import pygame

from food import Food
from settings import Settings
from snake_head import SnakeHead
import game_functions as gf

def run_game():
    # 初始化游戏并创建一个项目
    pygame.init()
    gs_settings = Settings()
    screen = pygame.display.set_mode((gs_settings.screen_width, gs_settings.screen_height))
    pygame.display.set_caption("Snake")

    snake_speed_clock = pygame.time.Clock()
    # 创建一个蛇头
    snake_head = SnakeHead(gs_settings, screen)
    food = Food(screen, gs_settings)

    #创建蛇的身体
    snakes = [snake_head]

    while True:
        #监视键盘和鼠标事件
        gf.check_events(snakes[0])
        gf.move_snake(snakes,gs_settings, screen)
        gf.check_collision(food, snakes)
        # 每次循环时都重绘制屏幕
        gf.update_screen(gs_settings, screen, snakes, food, snake_speed_clock)

run_game()

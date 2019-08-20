# /usr/env/python3
# -*- coding:utf-8-*-

import sys
import pygame
from pygame.sprite import Group

from food import Food
from settings import Settings
from snake_head import SnakeHead
import game_functions as gf

def run_game():
    #初始化游戏并创建一个项目
    pygame.init()
    gs_settings = Settings()
    screen = pygame.display.set_mode((gs_settings.screen_width, gs_settings.screen_height))
    pygame.display.set_caption("Snake")

    #创建一个蛇头
    snake_head = SnakeHead(gs_settings, screen)
    food = Food(screen, gs_settings)

    #创建蛇的身体
    snake_bodys = Group()

    while True:
        #监视键盘和鼠标事件
        gf.check_events(snake_head)
        snake_head.update()
        gf.check_collision(gs_settings, screen, snake_head, food, snake_bodys)
        #每次循环时都重绘制屏幕
        gf.update_screen(gs_settings, screen, snake_head, food)

run_game()

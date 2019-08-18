# /usr/env/python3
# -*- coding:utf-8-*-

import sys
import pygame

from settings import Settings
from snake_head import SnakeHead
import game_functions as gs

def run_game():
    #初始化游戏并创建一个项目
    pygame.init()
    gs_settings = Settings()
    screen = pygame.display.set_mode((gs_settings.screen_height, gs_settings.screen_width))
    pygame.display.set_caption("Snake")

    #创建一个蛇头
    snake_head = SnakeHead(gs_settings, screen)

    while True:
        #监视键盘和鼠标事件
        gs.check_events(snake_head)
        
        snake_head.update()

        #每次循环时都重绘制屏幕
        gs.update_screen(gs_settings, screen, snake_head)

run_game()

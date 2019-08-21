import sys
import pygame

from snake_body import SnakeBody
from snake_head import SnakeHead


def check_keydown_events(event, sh):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        sh.moving_direction="right"
    elif event.key == pygame.K_LEFT:
        sh.moving_direction="left"
    elif event.key == pygame.K_UP:
        sh.moving_direction="up"
    elif event.key == pygame.K_DOWN:
        sh.moving_direction="down"

def check_events(sh):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, sh)

def snake_grow():
    pass

def check_collision(gs_settings, screen, snake_head, food, snake_bodys):
    """更新蛇的身体"""
    if  pygame.sprite.collide_rect(snake_head, food):
        food.update_center()
        new_head = SnakeHead(gs_settings, screen)
        if snake_head.moving_direction == "right" :
            new_head.centerx = snake_head.centerx + 10
            new_head.centery = snake_head.centery
            new_head.moving_direction = "right"
            print(new_head.rect)
        elif snake_head.moving_direction == "left" :
            new_head.centerx = snake_head.centerx - 10
            new_head.centery = snake_head.centery
            new_head.moving_direction = "left"
        elif snake_head.moving_direction == "up" :
            new_head.centerx = snake_head.centerx
            new_head.centery = snake_head.centery - 10
            new_head.moving_direction = "up"
        elif snake_head.moving_direction == "down":
            new_head.centerx = snake_head.centerx
            new_head.centery = snake_head.centery + 10
            new_head.moving_direction = "down"
        snake_bodys.insert(0, new_head)
def update_screen(gs_settings, screen, snake_bodys, food):
    """更新屏幕上的图像，并切换到新的屏幕"""
    screen.fill(gs_settings.bg_color)
    for snake in snake_bodys:
        snake.draw_sh()
    food.draw_food()
    # 让最近绘制的屏幕可见
    pygame.display.flip()

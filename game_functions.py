import sys
import pygame

from snake_body import SnakeBody

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
        new_body = SnakeBody(gs_settings, screen,snake_head)
        if snake_head.moving_direction == "right" :
            snake_head.centerx += self.gs_settings.sh_speed_factor
        elif snake_head.moving_direction == "left" :
            snake_head.centerx -= self.gs_settings.sh_speed_factor
        elif snake_head.moving_direction == "up" :
            snake_head.centery -= self.gs_settings.sh_speed_factor
        elif snake_head.moving_direction == "down":
            snake_head.centery += self.gs_settings.sh_speed_factor
        new_body.rect
        snake_bodys.add(new_body)
        print("hit")

def update_screen(gs_settings, screen, snake_head, food):
    """更新屏幕上的图像，并切换到新的屏幕"""
    screen.fill(gs_settings.bg_color)
    snake_head.draw_sh()
    food.draw_food()
    # 让最近绘制的屏幕可见
    pygame.display.flip()

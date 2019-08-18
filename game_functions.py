import sys

import pygame

def check_keydown_events(event, sh):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        sh.moving_right = True
    elif event.key == pygame.K_LEFT:
        sh.moving_left = True
    elif event.key == pygame.K_UP:
        sh.moving_up = True
    elif event.key == pygame.K_DOWN:
        sh.moving_down = True
    
def check_keyup_events(event ,sh):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        sh.moving_right = False
    elif event.key == pygame.K_LEFT:
        sh.moving_left = False
    elif event.key == pygame.K_UP:
        sh.moving_up = False
    elif event.key == pygame.K_DOWN:
        sh.moving_down = False

def check_events(sh):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, sh)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, sh)
            
def update_screen(gs_settings, screen, snake_head):
    """更新屏幕上的图像，并切换到新的屏幕"""
    screen.fill(gs_settings.bg_color)
    snake_head.draw_sh()
    # 让最近绘制的屏幕可见
    pygame.display.flip()

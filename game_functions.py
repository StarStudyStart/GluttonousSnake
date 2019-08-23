import sys
import pygame

from snake_head import SnakeHead

HEAD = 0


def check_keydown_events(event, snake_head):
    """响应按键"""
    if event.key == pygame.K_RIGHT and snake_head.moving_direction != "left":
        snake_head.moving_direction = "right"
    elif event.key == pygame.K_LEFT and snake_head.moving_direction != "right":
        snake_head.moving_direction = "left"
    elif event.key == pygame.K_UP and snake_head.moving_direction != "down":
        snake_head.moving_direction = "up"
    elif event.key == pygame.K_DOWN and snake_head.moving_direction != "up":
        snake_head.moving_direction = "down"


def check_events(sh):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, sh)


def attr_set(new_head, x, y, diretcion):
    """设置舌头的相关属性"""
    new_head.rect.centerx = x
    new_head.rect.centery = y
    new_head.moving_direction = diretcion


def move_snake(snakes, gs_settings, screen):
    snake_head = snakes[HEAD]
    new_head = SnakeHead(gs_settings, screen)
    if snake_head.moving_direction == "right":
        attr_set(new_head, snake_head.rect.centerx + 10, snake_head.rect.centery, "right")
    elif snake_head.moving_direction == "left":
        attr_set(new_head, snake_head.rect.centerx - 10, snake_head.rect.centery, "left")
    elif snake_head.moving_direction == "up":
        attr_set(new_head, snake_head.rect.centerx, snake_head.rect.centery - 10, "up")
    elif snake_head.moving_direction == "down":
        attr_set(new_head, snake_head.rect.centerx, snake_head.rect.centery + 10, "down")
    snakes.insert(0, new_head)


def check_collision(food, snakes):
    """更新蛇的身体"""
    if pygame.sprite.collide_rect(snakes[HEAD], food):
        food.update_center()
    else:
        del snakes[-1]


def update_screen(gs_settings, screen, snakes, food, snake_speed_clock):
    """更新屏幕上的图像，并切换到新的屏幕"""
    screen.fill(gs_settings.bg_color)
    for snake in snakes:
        snake.draw_sh()
    food.draw_food()
    # 让最近绘制的屏幕可见
    pygame.display.update()
    snake_speed_clock.tick(gs_settings.snake_speed)
    # pygame.display.flip()

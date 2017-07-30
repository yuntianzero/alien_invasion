import sys
import pygame



def check_event(ship):
    """响应按键和鼠标事件"""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # 向右移动飞船
                ship.moving_right = True
            if event.key == pygame.K_LEFT:
                # 向左移动飞船
                ship.moving_left = True
            if event.key == pygame.K_UP:
                # 向上移动飞船
                ship.moving_up = True
            if event.key == pygame.K_DOWN:
                # 向上移动飞船
                ship.moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            if event.key == pygame.K_LEFT:
                ship.moving_left = False
            if event.key == pygame.K_UP:
                ship.moving_up = False
            if event.key == pygame.K_DOWN:
                ship.moving_down = False




def update_screen(ai_settings,screen, ship, doraemon):
    # 每次循环都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    doraemon.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()
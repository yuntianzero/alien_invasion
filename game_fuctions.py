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
                ship.rect.centerx += 1
            if event.key == pygame.K_LEFT:
                # 向左移动飞船
                ship.rect.centerx -= 1



def update_screen(ai_settings,screen, ship, doraemon):
    # 每次循环都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    doraemon.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()
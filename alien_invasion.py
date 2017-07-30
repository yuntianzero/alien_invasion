# -*- coding: utf-8 -*-
import pygame

from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_fuctions as gf
from doraemon import Doraemon

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings =Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #  创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建Doraemon
    doraemon = Doraemon(ai_settings,screen)
    # 创建一个存储子弹的编组
    bullets = Group()
    #  背景色
    bg_color = (ai_settings.bg_color)
	
    # 游戏主循环
    while True:
        gf.check_event(ai_settings, screen, ship, bullets)
        #doraemon.update()
        ship.update()
        bullets.update()

        # 删除已消失的子弹
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        print(len(bullets))

        gf.update_screen(ai_settings,screen, ship, doraemon, bullets)

       # screen.fill(ai_settings.bg_color)
       # ship.blitme()

        # 增加Doraemon


run_game()
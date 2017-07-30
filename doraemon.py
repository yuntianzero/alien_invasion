__author__ = 'zero'
import pygame

"""
    def __init__(self, sceen):
        # 初始化Doraemon位置
        self.screen = sceen

        # 加载Doraemon图像并获取其外接矩形
        self.image=pygame.image.load('images/doraemon.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = sceen.get_rect()

        # 将doraemon放在屏幕正中央
        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)
"""

class Doraemon():
    def __init__(self, ai_settings, screen):
        """"初始化Doraemon并设置其初始位置"""
        self.screen = screen
        # 传递setting里面参数
        self.ai_settings = ai_settings
       # 加载Doraemon图像并获取其外接矩形
        self.image = pygame.image.load('images/doraemon.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将Doraemon放在屏幕中央
        self.rect.center = self.screen_rect.center


        # 在Doraemon的属性center中存储小数值
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)
        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def update(self):
        """根据移动标志调整Doraemon的位置"""
        # if self.moving_right:
        # self.rect.centerx += 1
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center_x += self.ai_settings.ship_speed_factor
            # if self.moving_left:
            # self.rect.centerx -= 1
        if self.moving_left and self.rect.left > 0:
            self.center_x -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.center_y -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center_y += self.ai_settings.ship_speed_factor

        # 根据self.center更新rect对象
        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y


    def blitme(self):
        """在指定位置绘制Doraemon"""
        self.screen.blit(self.image, self.rect)



__author__ = 'zero'
import pygame

class Doraemon():

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




#from msilib.schema import SelfReg
from email.mime import image
import pygame


class Ship:

    def __init__(self, game, height, width):

        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()  # 返回屏幕的位置对象
        
        self.image = pygame.image.load('src/plane.jpg')
        self.image = pygame.transform.scale(self.image, (height, width))
        
        self.rect = self.image.get_rect()  # 返回飞船的位置对象
        self.rect.midbottom = self.screen_rect.midbottom  # 飞船图片位置为屏幕底部中央

    def draw_plane(self):
        self.screen.blit(self.image, self.rect)

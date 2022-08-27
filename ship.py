import pygame


class Ship:

    def __init__(self, game, height, width):

        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()  # 返回屏幕的位置对象

        self.image = pygame.image.load('src/plane.jpg')
        self.image = pygame.transform.scale(self.image, (height, width))

        self.rect = self.image.get_rect()  # 返回飞船的位置对象
        self.rect.midbottom = self.screen_rect.midbottom  # 飞船图片位置为屏幕底部中央

        self.moving_right = False
        self.moving_left = False

    def draw_plane(self):
        self.screen.blit(self.image, self.rect)

    def updata(self, setting):
        if self.moving_right:
            tmp = setting.ship_speed + self.rect.x
            if (tmp <= 0 or tmp >= setting.screen_width - setting.ship_width):
                return
            self.rect.x = tmp
        if self.moving_left:
            tmp = self.rect.x - setting.ship_speed
            if (tmp <= 0 or tmp >= setting.screen_width - setting.ship_width):
                return
            self.rect.x = tmp

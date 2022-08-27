import pygame
import sys
from ship import Ship
from setting import settings


class game:

    def __init__(self):
        pygame.init()  # 使用pygame之前必须初始化
        self.setting = settings()
        if (self.setting.full_screen):
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)# 全屏设置主屏窗口
            self.setting.screen_height = self.screen.get_rect().height
            self.setting.screen_width = self.screen.get_rect().width
        else:        
            self.screen = pygame.display.set_mode(
                (self.setting.screen_width, self.setting.screen_height))  
        self.the_plane = Ship(self, self.setting.ship_height,
                              self.setting.ship_width)
        pygame.display.set_caption("简单弹幕游戏")

    def run_game(self):
        while True:
            self._check_events()
            self._updata_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # 按下按键
                self.check_keydown(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup(event)

    def _updata_screen(self):
        self.screen.fill(self.setting.bgcolor)
        self.the_plane.updata(self.setting)
        self.the_plane.draw_plane()
        pygame.display.flip()  # 更新显示内容

    def check_keydown(self, event):
        if event.key == pygame.K_RIGHT:  # 向右移动
            self.the_plane.moving_right = True
            print(self.the_plane.rect.x)
        elif event.key == pygame.K_LEFT:
            self.the_plane.moving_left = True
        
        if(event.key == pygame.K_ESCAPE):
            sys.exit()

    def check_keyup(self, event):
        if event.key == pygame.K_RIGHT:
            self.the_plane.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.the_plane.moving_left = False


if __name__ == '__main__':
    ai = game()
    ai.run_game()
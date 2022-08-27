import sys
import pygame
from ship import Ship 
from setting import settings


class game:

    def __init__(self):
        pygame.init()  # 使用pygame之前必须初始化
        self.setting = settings()
        self.screen = pygame.display.set_mode((
            self.setting.screen_width, self.setting.screen_height))  # 设置主屏窗口
        self.the_plane = Ship(self, self.setting.ship_height, self.setting.ship_width)
        pygame.display.set_caption("简单弹幕游戏")
        

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.setting.bgcolor)
            self.the_plane.draw_plane()
            pygame.display.flip()  # 更新显示内容


if __name__ == '__main__':
    ai = game()
    ai.run_game()
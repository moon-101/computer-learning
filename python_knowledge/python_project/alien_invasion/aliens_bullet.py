import pygame
from pygame.sprite import Sprite



class AliensBullet(Sprite):
    """管理外星人发射的子弹"""

    def __init__(self,ai_game,center_pos):
        """创建在随机一个外星人当前位置创建一个子弹对象"""
        super().__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.color=self.settings.alien_bullet_color

        #(0,0)上创建一个表示子弹的矩形，再设置正确的位置。
        self.rect=pygame.Rect(0,0,self.settings.alien_bullet_width,self.settings.alien_bullet_height)

        self.rect.center=center_pos

        #存储用小数表示的子弹位置。
        self.y=float(self.rect.y)


    def update(self):
        """向下移动子弹。"""
        #更新表示子弹位置的小数值
        self.y+= self.settings.alien_bullet_speed

        # 更新表示子弹的rect的位置
        self.rect.y=self.y

    def draw_bullet(self):
        """在屏幕绘制子弹"""
        pygame.draw.rect(self.screen,self.color,self.rect)
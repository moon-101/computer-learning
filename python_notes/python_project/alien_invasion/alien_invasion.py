"""
1.首先要创建一个空的Pygame窗口，之后用来绘制游戏元素，并响应玩家输入，设置背景色。

5.在大型项目中，经常需要在添加新代码前重构既有代码。重构旨在简化既有代码的结构，使其更容易扩散。本节将把越来越长的方法run_game()拆分成两个辅助方法。辅助方法在类中执行任务，但并非是通过实例调用的。在python中，辅助方法的名称以单个下划线打头。
"""
import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion():
    """管理游戏资源和行为的类"""
    def __init__(self):
        """初始游戏化并创建游戏资源"""
        pygame.init()#pygame初始化
        self.settings=Settings()
        #全屏设置
        self.screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)#self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))#创建幕布,(创建一个显示窗口)，（1200，800）单位是一像素，该数据是个surface
        self.settings.screen_width=self.screen.get_rect().width
        self.settings.screen_height=self.screen.get_rect().height

        
        pygame.display.set_caption("Alien Invasion")#创建标题

        self.ship=Ship(self)
        #子弹
        self.bullets=pygame.sprite.Group()

    
    def run_game(self):
        """开始游戏主循环"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()            

    def _check_events(self):
        """监视鼠标和键盘事件"""
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type ==pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type==pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        """键盘按下所发生的事件"""
        if event.key==pygame.K_RIGHT:
            #向右移动飞船
            self.ship.moving_right=True
        elif event.key==pygame.K_LEFT:
            #向左移动飞船
            self.ship.moving_left=True
        elif event.key==pygame.K_UP:
            #向上移动飞船
            self.ship.moving_up=True
        elif event.key==pygame.K_DOWN:
            #向下移动飞船
            self.ship.moving_down=True

        elif event.key==pygame.K_q:
        
            # 退出游戏
            sys.exit()
        
        elif event.key==pygame.K_SPACE:
            self._fire_bullet()


    def _check_keyup_events(self,event):
        """响应松开"""
        if event.key==pygame.K_RIGHT:
            #向右移动飞船
            self.ship.moving_right=False
        elif event.key==pygame.K_LEFT:
            #向左移动飞船
            self.ship.moving_left=False
        elif event.key==pygame.K_UP:
            #向上移动飞船
            self.ship.moving_up=False
        elif event.key==pygame.K_DOWN:
            #向下移动飞船
            self.ship.moving_down=False

    def _fire_bullet(self):
        """创建一颗子弹，并将其加入编组bullets中"""
        if len(self.bullets)<self.settings.bullets_allowed:
            new_bullet=Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """更新子弹位置，删除消失的子弹"""
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom<=0:
                self.bullets.remove(bullet)
            if bullet.rect.left<=0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """每次循环时都重绘屏幕"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # 让最新的绘制屏幕可见。
        pygame.display.flip()#模块，类，方法
if __name__=='__main__':
    ai=AlienInvasion()
    ai.run_game()



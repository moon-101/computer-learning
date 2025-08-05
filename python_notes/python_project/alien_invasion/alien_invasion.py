"""
1.首先要创建一个空的Pygame窗口，之后用来绘制游戏元素，并响应玩家输入，设置背景色。

5.在大型项目中，经常需要在添加新代码前重构既有代码。重构旨在简化既有代码的结构，使其更容易扩散。本节将把越来越长的方法run_game()拆分成两个辅助方法。辅助方法在类中执行任务，但并非是通过实例调用的。在python中，辅助方法的名称以单个下划线打头。
"""
import sys
from time import sleep
import random

import pygame

from settings import Settings
from game_stats import GameStates
from button import Button
from scoreboard import Scoreboard
from ship import Ship
from bullet import Bullet
from alien import Alien
from aliens_bullet import AliensBullet

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
        self.screen_rect = self.screen.get_rect()  # 增加这个属性
        
        pygame.display.set_caption("Alien Invasion")#创建标题


        #创建一个用于存储游戏统计信息的实例
        #,并创建得分板
        self.stats=GameStates(self)
        self.sb=Scoreboard(self)

        #飞船
        self.ship=Ship(self)

        #子弹
        self.bullets=pygame.sprite.Group()

        # 外星人
        self.aliens=pygame.sprite.Group()        
        self._create_fleet()

        #外星人子弹容器
        self.alien_bullets=pygame.sprite.Group()#新增外星人子弹容器
        self.last_alien_shot=0#记录上次射击时间

        #创建play按钮
        self.play_button=Button(self,"play")

        

    def run_game(self):
        """开始游戏主循环"""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                self._update_alien_bullets()
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
            
            elif event.type==pygame.MOUSEBUTTONDOWN:
                mouse_pos=pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

        
    def _check_play_button(self,mouse_pos):
        """玩家点击play按钮时开始新游戏"""
        button_clicked=self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            #重置游戏设置
            self.settings.initialize_dynamic_settings()
            #重置游戏统计信息
            self.stats.reset_stats()
            self.stats.game_active=True

            self.sb.prep_score()

            #清空余下的外星人和子弹
            self.aliens.empty()
            self.bullets.empty()

            #创建一群新的外星人并让飞船居中
            self._create_fleet()
            self.ship.center_ship()
            
            #隐藏鼠标光标
            pygame.mouse.set_visible(False)

            self.sb.prep_images()




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
            with open('high_score.txt','w') as file:
                file.write(str(self.sb.stats.high_score))
            sys.exit()
        
        elif event.key==pygame.K_SPACE:
            #发射子弹
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
        
        self._check_bullet_allien_collisions()
        self.start_new_level()
    def _check_bullet_allien_collisions(self):
        """检查子弹和外星人是否发生碰撞"""
        # 检查是否有子弹击中外星人
        # 如果是，就删除相应的子弹和外星人
        collisions=pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score+=self.settings.alien_points*len(aliens)
                self.sb.prep_score()
                self.sb.check_high_score()


    def start_new_level(self):
        """开始一个新的等级"""
        if not self.aliens:
            #删除现有的子弹并新建一群外星人
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            #等级+1
            self.stats.level+=1
            self.sb.prep_level()

    def _create_fleet(self):
        """创建外星人群"""
        #创建一个外星人
        alien=Alien(self)
        alien_width=alien.rect.width
        alien_height=alien.rect.height
        available_space_x=self.settings.screen_width-(2*alien_width)
        number_alien_x=available_space_x//(2*alien_width)

        #计算屏幕可容纳多少行外星人
        ship_height=self.ship.rect.height
        available_space_y=(self.settings.screen_height-(3*alien_height)-ship_height)
        number_rows=available_space_y//(2*alien_height)
        #创建一群外星人
        for row_number in range(number_rows):
            for alien_number in range(number_alien_x):
                self._create_alien(alien_number,row_number)

    def _create_alien(self,alien_number,row_number):
        """创建一行外星人"""
        alien=Alien(self)
        alien_width,alien_height=alien.rect.size
        alien.x=alien_width+2*alien_width*alien_number
        alien.rect.x=alien.x
        alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
        self.aliens.add(alien)
    


    def _shoot_alien_bullet(self):
        """实现随机外星人射击"""
        #每600毫秒有概念射击
        now=pygame.time.get_ticks()
        if now-self.last_alien_shot>600 and len(self.aliens)>0:
            if random.random()<0.3:
                shooter=random.choice(self.aliens.sprites())
                new_bullet=AliensBullet(self,shooter.rect.center)
                self.alien_bullets.add(new_bullet)
            self.last_alien_shot=now
    
    def _update_alien_bullets(self):
        """更新外星人子弹位置"""
        self.alien_bullets.update()
        #删除超出屏幕的子弹
        for bullet in self.alien_bullets.copy():
            if bullet.rect.top>self.settings.screen_height:
                self.alien_bullets.remove(bullet)#如何确定删除的子弹是那个超出屏幕的子弹?
        #检测飞船的碰撞
        if pygame.sprite.spritecollideany(self.ship,self.alien_bullets):
            self._ship_hit()

    def _check_fleet_edges(self):
        """有外星人到达边缘时采取响应的措施"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """将整群外星人下移，并改变它们的方向"""
        for alien in self.aliens.sprites():
            alien.rect.y+=self.settings.fleet_drop_speed
        self.settings.fleet_direction*=-1
    
    def _check_aliens_bottom(self):
        """检查是否有外星人达到了屏幕底端。"""
        screen_rect=self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >=screen_rect.bottom:
                #飞船被撞到一样处理
                self._ship_hit()
                break
    
    def _update_aliens(self):
        """外星人移动更新"""
        self._check_fleet_edges()
        self.aliens.update()

        # 检测外星人和飞船之间的碰撞
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()

        #检查是否有外星人到达了屏幕底部
        self._check_aliens_bottom()

        self._shoot_alien_bullet()#新增射击检测

    
    def _ship_hit(self):
        """响应外星人撞到飞船"""
        if self.stats.ships_left>0:
            #将ships_left减1,更新计分板
            self.stats.ships_left-=1
            self.sb.prep_ships()

            # 重置游戏元素
            self.aliens.empty()     # 清空外星人
            self.bullets.empty()   # 清空子弹
            
            self._create_fleet()   # 重新生成外星人群
            self.ship.center_ship()# 重置飞船位置
                #暂停
            sleep(0.5)
        else:
            self.stats.game_active=False
            pygame.mouse.set_visible(True)



    def _update_screen(self):
        """每次循环时都重绘屏幕"""
        self.screen.fill(self.settings.bg_color)
        #显示得分
        self.sb.show_score()

        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        for bullet in self.alien_bullets.sprites():
            bullet.draw_bullet()  # 绘制外星人子弹


        #如果游戏处于非活动状态，就绘制play按钮
        if not self.stats.game_active:
            self.play_button.draw_button()

        # 让最新的绘制屏幕可见。
        pygame.display.flip()#模块，类，方法
    

if __name__=='__main__':
    ai=AlienInvasion()
    ai.run_game()



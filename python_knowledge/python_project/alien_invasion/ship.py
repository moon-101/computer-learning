import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """管理飞船的类"""
    def __init__(self,ai_game):
        """初始化飞船以及设置其初始位置"""
        super().__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.screen_rect=ai_game.screen.get_rect()

        #加载飞船图像并外接矩形。
        self.image=pygame.image.load(r'images\ship.bmp')
        self.rect=self.image.get_rect()

        #对于每艘新飞船，都将其放在屏幕底部中间
        self.rect.midbottom=self.screen_rect.midbottom

        #在飞船的属性x\y,中存储小数值
        self.x=float(self.rect.x)
        self.y=float(self.rect.y)

        # 设立一个移动信号灯,移动标志
        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False

    def update(self):
        if self.moving_right==True and self.rect.right<=self.settings.screen_width:
            self.x+=self.settings.ship_speed
        if self.moving_left and self.rect.left>=0:
            self.x-=self.settings.ship_speed

        if self.moving_up and self.rect.top>=0:
            self.y-=self.settings.ship_speed
        
        if self.moving_down and self.rect.bottom<=self.settings.screen_height:
            self.y+=self.settings.ship_speed

        # 根据self.x更新rect对象
        self.rect.x=self.x
        self.rect.y=self.y
    
    def center_ship(self):
        """让飞船在屏幕底端居中"""
        self.rect.midbottom=self.screen_rect.midbottom
        self.x=float(self.rect.x)    
        self.y = float(self.rect.y)  # 如果启用垂直移动，需要重置y坐标


    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)

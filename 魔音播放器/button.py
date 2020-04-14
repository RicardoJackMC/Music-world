import random

import pygame

import Load_Music

class Button():

    def __init__(self, screen, add, name, place):
        
        self.screen = screen
        self.add = add#路径
        self.name = name#按钮功能(没卵用....)
        self.place = place#按钮绘制位置
        self.mybt = pygame.image.load(r''+self.add)#图片地址
        self.rect = self.mybt.get_rect()#获取图案矩形 
        self.angle = 1#图像旋转角度

    def click_button(self,mouse_x,mouse_y):
        """判定点击按钮"""
        if (mouse_x > self.place[0] and mouse_x < self.rect.width+(self.place[0])  
            and mouse_y > self.place[1] and mouse_y < self.rect.height+(self.place[1])):
            return True
    
    def show_button(self):
        """显示按钮"""
        self.screen.blit(self.mybt, self.place)

    def ro_img(self):#旋转图像
        newimg = pygame.transform.rotozoom(self.mybt, self.angle, 1.0)
        newrect = newimg.get_rect(center=(300,248))#固定图像中心
        self.screen.blit(newimg, newrect)
        self.angle += 1


class Music_Mode(Button):

    def change_img(self, add):
        self.add = add
        self.mybt = pygame.image.load(r''+self.add)#图片地址
        super().show_button()

    def order_play(self, music_num, music_list):#顺序播放
        if not pygame.mixer.music.get_busy():
            Load_Music.next_music(music_num, music_list)

    def Single_cycle(self):#单曲循环
        if not pygame.mixer.music.get_busy():
            Load_Music.play_music()

    def random_play(self, music_num, music_list):#随机播放
        if not pygame.mixer.music.get_busy():
            music_num[0] = random.randint(0, len(music_list)-1)
            Load_Music.load_music(music_list[music_num[0]])
            Load_Music.play_music()
    

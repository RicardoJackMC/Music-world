import sys
import os
import pygame
from draw import draw
from button import Button
import Load_Music
def check_events(music_num, volume, Music_List):
    """响应按键"""  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                Load_Music.next_music(music_num, Music_List)

            if event.key == pygame.K_LEFT:
                Load_Music.previous_music(music_num, Music_List)

            if event.key == pygame.K_p:
                Load_Music.pause_music()
            
            if event.key == pygame.K_SPACE:
                Load_Music.unpause_music()
            
            if event.key == pygame.K_KP_ENTER:
                Load_Music.load_music(Music_List[music_num[0]])
                Load_Music.play_music()
            
            if event.key == pygame.K_UP:
                volume[0] += 0.1
                Load_Music.volume_music(volume)
            
            if event.key == pygame.K_DOWN:
                volume[0] -= 0.1
                Load_Music.volume_music(volume)

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()           
            mouse = [mouse_x, mouse_y]
            return mouse

def get_click(get_mouse, shortcut_keys_bt, play_bt, pause_bt, next_bt, previous_bt, show_bt,draw_bt, music_num, Music_list, music_run, play_mode, mode):
    """检测鼠标点击"""
    if get_mouse != None :#是否有点击事件
        mouse = get_mouse
        if shortcut_keys_bt.click_button(mouse[0], mouse[1]):
            os.startfile(r".\shortcut_keys_bt.txt")
        if play_bt.click_button(mouse[0], mouse[1]):
            music_run[0] = Load_Music.play_music()
        elif pause_bt.click_button(mouse[0], mouse[1]):
            if music_run[0] and pygame.mixer.music.get_busy():
                music_run[0] = Load_Music.pause_music() 
                
            else:
                music_run[0] = Load_Music.unpause_music()

        elif next_bt.click_button(mouse[0], mouse[1]):
            Load_Music.next_music(music_num, Music_list)

        elif previous_bt.click_button(mouse[0], mouse[1]):
            Load_Music.previous_music(music_num, Music_list)

        elif show_bt.click_button(mouse[0], mouse[1]):
            music_run[0] = Load_Music.unpause_music()
        elif draw_bt.click_button(mouse[0], mouse[1]):
            draw()         
        elif play_mode.click_button(mouse[0], mouse[1]):
            mode[0] += 1
            if mode[0] > 3:
                mode[0] = 1
        



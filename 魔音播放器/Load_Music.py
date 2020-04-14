import os

import pygame

class Music_List():
    def __init__(self):
        # 播放列表
        self.play_list = []
        # 默认文件夹
        self.file_dir = 'music'

    def get_play_list(self):
        # 开始遍历目录
        for root, dirs, files in os.walk(self.file_dir):
            for file in files:
                if '.mp3' in file:
                    self.play_list.append(self.file_dir + "/" + file)
        return self.play_list


def load_music(titlt):#加载音乐
    try:
        pygame.mixer.music.load(titlt)
    except :
        pass

def play_music():
    pygame.mixer.music.play()
    return True

def stop_music():
    pygame.mixer.music.stop()

def pause_music():
    """暂停音乐"""
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
        return False

def unpause_music():
    """解除暂停"""
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.unpause()
        return True 

def next_music(music_num, Music_list):
    #下一曲.
    music_num[0] += 1
    check_music(music_num, Music_list)
    try:
        load_music(Music_list[music_num[0]])
        play_music() 
    except:
        pass

def previous_music(music_num, Music_list):
    #上一曲
    music_num[0] -= 1
    check_music(music_num, Music_list)
    try:
        load_music(Music_list[music_num[0]])
        play_music()
    except:
        pass

def volume_music(volume):
    #调节音量
    pygame.mixer.music.set_volume(volume[0])
    print("音量："+str(100*volume[0]))

def check_music(music_num, Music_List):
    if abs(music_num[0]) < len(Music_List):
        pass
    else:
        music_num[0] = 0
    return music_num
    

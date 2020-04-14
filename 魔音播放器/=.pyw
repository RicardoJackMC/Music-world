import pygame
from draw import draw
import Load_Music
import function
from button import Button
from button import Music_Mode
import sys
import time
import button
def player_run():
    pygame.init()
    screen = pygame.display.set_mode((630, 892))
    pygame.display.set_caption("魔音播放器")

    background=pygame.image.load(r"./img/ccc.jpg")
    screen.blit(background,(0,0))

    music_num = [0]
    volume = [1]

    Music_list = Load_Music.Music_List().get_play_list()
    Load_Music.load_music(Music_list[music_num[0]])

    music_run = [True]

    pygame.time.Clock().tick(30)

    mode = [1]

    play_bt = Button(screen=screen, add="./img/play.png", name="play_music", place=[250, 600])
    next_bt = Button(screen=screen, add="./img/next.png", name="next_music", place=[400, 600])
    previous_bt = Button(screen=screen, add="./img/previous.png", name="previous_music", place=[100, 600])
    pause_bt = Button(screen=screen, add="./img/pause.png", name="pause_music", place=[250, 450])
    show_bt = Button(screen=screen, add="./img/show.png", name="show_music", place=[150, 100])
    draw_bt=Button(screen=screen, add="./img/565.png", name="565", place=[180, 750])
    play_mode = Music_Mode(screen=screen, add="./img/order.png", name="play_mode", place=[0, 0])
    shortcut_keys_bt = Button(screen=screen, add="./img/shortcut_keys_bt.png", name="shortcut_keys_bt", place=[390, 0])

    while True:

        get_mouse = function.check_events(music_num, volume, Music_list)
        function.get_click(get_mouse, shortcut_keys_bt, play_bt, pause_bt, next_bt, previous_bt,
            show_bt,draw_bt, music_num, Music_list, music_run, play_mode, mode)

        show_bt.show_button()
        play_bt.show_button()
        next_bt.show_button()
        previous_bt.show_button()
        pause_bt.show_button()
        draw_bt.show_button()
        shortcut_keys_bt.show_button()
        if mode[0] == 1:
            play_mode.change_img(add="./img/order.png")
            play_mode.order_play(music_num, Music_list)
        elif mode[0] == 2:
            play_mode.change_img(add="./img/single.png")
            play_mode.Single_cycle()
        elif mode[0] == 3:
            play_mode.change_img(add="./img/random.png")
            play_mode.random_play(music_num, Music_list)
        else:
            play_mode.change_img(add="./img/order.png")
            play_mode.order_play(music_num, Music_list)
            mode[0] = 1
            
        if pygame.mixer.music.get_busy() and music_run[0]:
            show_bt.ro_img()

        pygame.display.flip()


player_run()


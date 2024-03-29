import pygame
import sqlite3
import tkinter as tk
from gamestate import *
from sys import exit

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

pygame.init()

select_game_text_animation = 0
select_game_text_state = 'inc'

# set display size
if screen_height == 1440:
    screen = pygame.display.set_mode((2560, 1440), pygame.FULLSCREEN)
elif screen_height == 2160:
    screen = pygame.display.set_mode((3840, 2160), pygame.FULLSCREEN)
elif screen_height == 1080:
    screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
elif screen_height == 720:
    screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
elif screen_height == 480:
    screen = pygame.display.set_mode((854, 480), pygame.FULLSCREEN)
elif screen_height == 360:
    screen = pygame.display.set_mode((640, 360), pygame.FULLSCREEN)
elif screen_height == 240:
    screen = pygame.display.set_mode((426, 240), pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

cariboo_btn = pygame.image.load('graphics/main_menu/cariboo.png').convert()
cariboo_btn = pygame.transform.scale(cariboo_btn, (screen.get_width() * 0.65, screen.get_height() * 0.65))
cariboo_btn_rect = cariboo_btn.get_rect(center = (screen.get_width() * 0.5, screen.get_height() * 0.5))

cariboo_background_1 = pygame.image.load('graphics/backgrounds/platformer_background_4/background_cariboo.png').convert()
cariboo_background_1 = pygame.transform.scale(cariboo_background_1, (screen.get_width(), screen.get_height()))
cariboo_background_rect = cariboo_background_1.get_rect(topleft = (0, 0))

close_button = pygame.image.load('graphics/buttons/close_btn.png')
close_button = pygame.transform.scale(close_button, (screen.get_width() * 0.03, screen.get_height() * 0.06))
close_button_rect = close_button.get_rect(topright = (screen.get_width() - (screen.get_width() * 0.01) , screen.get_height() * 0.01))

pixel_font_large = pygame.font.Font('fonts/pixel/Pixeltype.ttf', int(screen.get_width() * 0.05))
select_game = pixel_font_large.render('SELECT A GAME', False, (255,255,255))
select_game_rect = select_game.get_rect(center = (screen.get_width() * 0.5, screen.get_height() * 0.05))
select_game_black = pixel_font_large.render('SELECT A GAME', False, (0,0,0))

pixel_font_med = pixel_font_large = pygame.font.Font('fonts/pixel/Pixeltype.ttf', int(screen.get_width() * 0.03))
cariboo_text = pixel_font_med.render('CARIBOO', False, (255,255,255))
cariboo_text_rect = cariboo_text.get_rect(center = (screen.get_width() * 0.5, screen.get_height() * 0.12))
cariboo_text_black = pixel_font_med.render('CARIBOO', False, (0,0,0))

flash_text = pixel_font_med.render('FLASH CARDS', False, (255,255,255))
flash_text_rect = flash_text.get_rect(center = (screen.get_width() * 0.5 + screen.get_width(), screen.get_height() * 0.12))
flash_text_black = pixel_font_med.render('FLASH CARDS', False, (0,0,0))

btn_border_black = pygame.Surface((cariboo_btn.get_width() * 1.01, cariboo_btn.get_height() * 1.01))
btn_border_white = pygame.Surface((cariboo_btn.get_width() * 1.01, cariboo_btn.get_height() * 1.01))
btn_border_white.fill((255,255,255))
btn_border_black.fill((0,0,0))

flash_background = pygame.Surface((screen.get_width(), screen.get_height()))
flash_background.fill((140,183,230))
flash_background_rect = flash_background.get_rect(topleft = (screen.get_width(), 0))

flash_btn = pygame.image.load('graphics/main_menu/flash_cards.png').convert()
flash_btn = pygame.transform.scale(flash_btn, (screen.get_width() * 0.65, screen.get_height() * 0.65))
flash_btn_rect = flash_btn.get_rect(center = (screen.get_width() * 0.5 + screen.get_width(), screen.get_height() * 0.5))

left_arrow_w = pygame.image.load('graphics/main_menu/left_arrow_white.png').convert_alpha()
left_arrow_g = pygame.image.load('graphics/main_menu/left_arrow_gray.png')
right_arrow_w = pygame.image.load('graphics/main_menu/right_arrow_white.png').convert_alpha()
right_arrow_g = pygame.image.load('graphics/main_menu/right_arrow_gray.png').convert_alpha()

left_arrow_g = pygame.transform.scale(left_arrow_g, (screen.get_width() * 0.04, screen.get_height() * 0.05))
left_arrow_w = pygame.transform.scale(left_arrow_w, (screen.get_width() * 0.04, screen.get_height() * 0.05))
right_arrow_g = pygame.transform.scale(right_arrow_g, (screen.get_width() * 0.04, screen.get_height() * 0.05))
right_arrow_w = pygame.transform.scale(right_arrow_w, (screen.get_width() * 0.04, screen.get_height() * 0.05))

right_arrow_rect = right_arrow_w.get_rect(center = (screen.get_width() * 0.9, screen.get_height() * 0.5))
left_arrow_rect = left_arrow_g.get_rect(center = (screen.get_width() * 0.1, screen.get_height() * 0.5))

game_btn_left = cariboo_btn_rect.left
game_btn_top = cariboo_btn_rect.top

def move_menu(direction):
    global cariboo_background_rect
    global flash_background_rect
    global cariboo_btn_rect
    global cariboo_text_rect
    global flash_text_rect
    global flash_btn_rect

    iteration_add = screen.get_width() / 120
    loop_end = 0

    cariboo_bg_pos = cariboo_background_rect.left
    cariboo_btn_pos = cariboo_btn_rect.left
    cariboo_text_pos = cariboo_text_rect.left

    flash_bg_pos = flash_background_rect.left
    flash_text_pos = flash_text_rect.left
    flash_btn_pos = flash_btn_rect.left


    if direction == 'right' and cariboo_background_rect.left == 0:
        while loop_end <= screen.get_width():
            if loop_end + iteration_add > screen.get_width() or loop_end + iteration_add == screen.get_width():
                cariboo_background_rect.left = cariboo_bg_pos - screen.get_width()
                cariboo_btn_rect.left = cariboo_btn_pos - screen.get_width()
                cariboo_text_rect.left = cariboo_text_pos - screen.get_width()

                flash_background_rect.left = flash_bg_pos - screen.get_width()
                flash_text_rect.left = flash_text_pos - screen.get_width()
                flash_btn_rect.left = flash_btn_pos - screen.get_width()

            else:
                cariboo_background_rect.left -= iteration_add
                cariboo_btn_rect.left -= iteration_add
                cariboo_text_rect.left -= iteration_add

                flash_background_rect.left -= iteration_add
                flash_text_rect.left -= iteration_add
                flash_btn_rect.left -= iteration_add
            
            screen.blit(cariboo_background_1, cariboo_background_rect)
            screen.blit(cariboo_btn, cariboo_btn_rect)
            screen.blit(cariboo_text, cariboo_text_rect)
            screen.blit(cariboo_text_black, cariboo_text_rect) 
            cariboo_text_black.set_alpha(200)

            screen.blit(flash_background, flash_background_rect)
            screen.blit(flash_text, flash_text_rect)
            screen.blit(flash_text_black, flash_text_rect)
            flash_text_black.set_alpha(200)
            screen.blit(flash_btn, flash_btn_rect)
            

            screen.blit(select_game, select_game_rect)
            screen.blit(select_game_black, select_game_rect)

            loop_end += iteration_add

            pygame.display.update()
        # cariboo_background_rect.left -= screen.get_width()
        # cariboo_btn_rect.left -= screen.get_width()
        # cariboo_text_rect.left -= screen.get_width()

        # flash_background_rect.left -= screen.get_width()
        # flash_text_rect.left -= screen.get_width()
        # flash_btn_rect.left -= screen.get_width()
    
    if direction == 'left' and cariboo_background_rect.left != 0:
        while loop_end <= screen.get_width():
            if loop_end + iteration_add > screen.get_width() or loop_end + iteration_add == screen.get_width():
                cariboo_background_rect.left = cariboo_bg_pos + screen.get_width()
                cariboo_btn_rect.left = cariboo_btn_pos + screen.get_width()
                cariboo_text_rect.left = cariboo_text_pos + screen.get_width()

                flash_background_rect.left = flash_bg_pos + screen.get_width()
                flash_text_rect.left = flash_text_pos + screen.get_width()
                flash_btn_rect.left = flash_btn_pos + screen.get_width()

            else:
                cariboo_background_rect.left += iteration_add
                cariboo_btn_rect.left += iteration_add
                cariboo_text_rect.left += iteration_add

                flash_background_rect.left += iteration_add
                flash_text_rect.left += iteration_add
                flash_btn_rect.left += iteration_add
            
            screen.blit(cariboo_background_1, cariboo_background_rect)
            screen.blit(cariboo_btn, cariboo_btn_rect)
            screen.blit(cariboo_text, cariboo_text_rect)
            screen.blit(cariboo_text_black, cariboo_text_rect) 
            cariboo_text_black.set_alpha(200)

            screen.blit(flash_background, flash_background_rect)
            screen.blit(flash_text, flash_text_rect)
            screen.blit(flash_text_black, flash_text_rect)
            flash_text_black.set_alpha(200)
            screen.blit(flash_btn, flash_btn_rect)
            

            screen.blit(select_game, select_game_rect)
            screen.blit(select_game_black, select_game_rect)

            loop_end += iteration_add

            pygame.display.update()

        # cariboo_background_rect.left += screen.get_width()
        # cariboo_btn_rect.left += screen.get_width()
        # cariboo_text_rect.left += screen.get_width()

        # flash_background_rect.left += screen.get_width()
        # flash_text_rect.left += screen.get_width()
        # flash_btn_rect.left += screen.get_width()

def menu():
    global game_state
    global select_game_text_animation
    global select_game_text_state
    global flash_background_rect
    global cariboo_background_rect

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if close_button_rect.collidepoint(event.pos):
                pygame.quit()
                exit()

            if cariboo_btn_rect.collidepoint(event.pos):
                set_game_state('cariboo_init')
            
            if flash_btn_rect.collidepoint(event.pos):
                set_game_state('flash_init')
            
            if right_arrow_rect.collidepoint(event.pos):
                move_menu('right')

            if left_arrow_rect.collidepoint(event.pos):
                move_menu('left')
    
    screen.blit(cariboo_background_1, cariboo_background_rect)
    screen.blit(flash_background, flash_background_rect)
    
    screen.blit(btn_border_white, (game_btn_left - (screen.get_width() * 0.003), game_btn_top - (screen.get_height() * 0.003)))
    screen.blit(btn_border_black, (game_btn_left - (screen.get_width() * 0.003), game_btn_top - (screen.get_height() * 0.003)))
    screen.blit(cariboo_btn, cariboo_btn_rect)
    screen.blit(cariboo_text, cariboo_text_rect)
    screen.blit(cariboo_text_black, cariboo_text_rect)
    cariboo_text_black.set_alpha(select_game_text_animation)

    screen.blit(flash_text, flash_text_rect)
    screen.blit(flash_text_black, flash_text_rect)
    flash_text_black.set_alpha(select_game_text_animation)
    screen.blit(flash_btn, flash_btn_rect)

    screen.blit(select_game, select_game_rect)
    screen.blit(select_game_black, select_game_rect)
    screen.blit(right_arrow_w, right_arrow_rect)
    screen.blit(left_arrow_w, left_arrow_rect)
    screen.blit(right_arrow_g, right_arrow_rect)
    screen.blit(left_arrow_g, left_arrow_rect)  

    btn_border_black.set_alpha(select_game_text_animation)
    right_arrow_g.set_alpha(select_game_text_animation)
    left_arrow_g.set_alpha(select_game_text_animation)

    screen.blit(close_button, close_button_rect)

    if select_game_text_state == 'inc':
        select_game_text_animation += 2
    if select_game_text_state == 'dec':
        select_game_text_animation -= 2
    if select_game_text_animation == 200:
        select_game_text_state = 'dec'
    if select_game_text_animation == 10:
        select_game_text_state = 'inc'


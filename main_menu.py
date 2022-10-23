import pygame
import sqlite3
import tkinter as tk
from gamestate import *

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

pygame.init()

select_game_text_animation = 0
select_game_text_state = 'inc'

# set display size
if screen_height == 1440:
    screen = pygame.display.set_mode((2560, 1440))
if screen_height == 2160:
    screen = pygame.display.set_mode((3840, 2160), pygame.FULLSCREEN)
if screen_height == 1080:
    screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
if screen_height == 720:
    screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
if screen_height == 480:
    screen = pygame.display.set_mode((854, 480), pygame.FULLSCREEN)
if screen_height == 360:
    screen = pygame.display.set_mode((640, 360), pygame.FULLSCREEN)
if screen_height == 240:
    screen = pygame.display.set_mode((426, 240), pygame.FULLSCREEN)

cariboo_btn = pygame.image.load('graphics/main_menu/cariboo.png').convert()
cariboo_btn = pygame.transform.scale(cariboo_btn, (screen.get_width() * 0.65, screen.get_height() * 0.65))
cariboo_btn_rect = cariboo_btn.get_rect(center = (screen.get_width() * 0.5, screen.get_height() * 0.5))

cariboo_background_1 = pygame.image.load('graphics/backgrounds/platformer_background_4/background_cariboo.png').convert()
cariboo_background_1 = pygame.transform.scale(cariboo_background_1, (screen.get_width(), screen.get_height()))

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

btn_border_black = pygame.Surface((cariboo_btn.get_width() * 1.01, cariboo_btn.get_height() * 1.01))
btn_border_white = pygame.Surface((cariboo_btn.get_width() * 1.01, cariboo_btn.get_height() * 1.01))
btn_border_white.fill((255,255,255))
btn_border_black.fill((0,0,0))

def menu():
    global game_state
    global select_game_text_animation
    global select_game_text_state

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
    
    screen.blit(cariboo_background_1, (0,0))
    screen.blit(close_button, close_button_rect)
    screen.blit(btn_border_white, (cariboo_btn_rect.left - (screen.get_width() * 0.003), cariboo_btn_rect.top - (screen.get_height() * 0.003)))
    screen.blit(btn_border_black, (cariboo_btn_rect.left - (screen.get_width() * 0.003), cariboo_btn_rect.top - (screen.get_height() * 0.003)))
    screen.blit(cariboo_btn, cariboo_btn_rect)
    screen.blit(select_game, select_game_rect)
    screen.blit(select_game_black, select_game_rect)
    screen.blit(cariboo_text, cariboo_text_rect)
    screen.blit(cariboo_text_black, cariboo_text_rect)
    cariboo_text_black.set_alpha(select_game_text_animation)
    btn_border_black.set_alpha(select_game_text_animation)

    if select_game_text_state == 'inc':
        select_game_text_animation += 2
    if select_game_text_state == 'dec':
        select_game_text_animation -= 2
    if select_game_text_animation == 200:
        select_game_text_state = 'dec'
    if select_game_text_animation == 10:
        select_game_text_state = 'inc'


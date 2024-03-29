from fileinput import close
from turtle import circle
import pygame
from pygame import MOUSEBUTTONDOWN, K_b, gfxdraw
from sys import exit
import tkinter as tk
import sqlite3
from random import randint
from cariboo_game import *
import main_menu
from gamestate import set_game_state
import flash_cards
import intro

# init the game
pygame.init()

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

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
    
pygame.display.set_caption('Speech Games')

# start clock
clock = pygame.time.Clock()

# states for game initializing
cariboo_initialize_state = True
flash_cards_init_state = True

# initiate everything for the game cariboo
initiate_cariboo_circles_text_board()
button_images()
initiate_menu_buttons()
initiate_cariboo_state()

while True: 
    # import the game state with every iteration in order to check for changes in the game_state
    from gamestate import game_state

    if game_state == 'intro':
        intro.intro_screen()

    if game_state == 'main_menu':
        main_menu.menu()
    
    if game_state == 'flash_init':
        if flash_cards_init_state:
            flash_cards.button_images()
            flash_cards_init_state = False
            
        flash_cards.flash_cards_game()

    if game_state == 'cariboo_init':
        cariboo_game()

    # update the game
    pygame.display.update()
    # set fps to 60
    clock.tick(60)
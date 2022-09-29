import pygame
from pygame import gfxdraw
from sys import exit
import tkinter as tk
import sqlite3
from random import randint
import math

# functions/methods

def restart_cariboo():
    global ball_list
    global balls_found_list
    global game_state

    global ball_1_rect_list
    global ball_2_rect_list
    global ball_3_rect_list
    global ball_4_rect_list

    ball_list = []
    balls_found_list = []
    ball_1_rect_list = []
    ball_2_rect_list = []
    ball_3_rect_list = []
    ball_4_rect_list = []

    set_flash_state()
    set_flash_animation_state()
    ball_animation_init()
    game_state = 'cariboo'
    print(ball_list)


def position_ball(x, y):
    global ball_1_rect_list
    global ball_2_rect_list
    global ball_3_rect_list
    global ball_4_rect_list

    if len(ball_list) < 1:
        ball_board_position(ball_1_list[0])
        ball_1_rect_list = [ball_1_trans.get_rect(topleft = (x, y)), ball_1_trans.get_rect(topleft = (x + screen.get_width() * 0.005, y + screen.get_width() * 0.004)), ball_1_trans.get_rect(topleft = (x + screen.get_width() * 0.012, y + screen.get_width() * 0.01))]
        return
    if len(ball_list) == 1:
        ball_board_position(ball_2_list[0])
        ball_2_rect_list = [ball_2_trans.get_rect(topleft = (x, y)), ball_2_trans.get_rect(topleft = (x + screen.get_width() * 0.005, y + screen.get_width() * 0.004)), ball_2_trans.get_rect(topleft = (x + screen.get_width() * 0.012, y + screen.get_width() * 0.01))]
        return
    if len(ball_list) == 2:
        ball_board_position(ball_3_list[0])
        ball_3_rect_list = [ball_3_trans.get_rect(topleft = (x, y)), ball_3_trans.get_rect(topleft = (x + screen.get_width() * 0.005, y + screen.get_width() * 0.004)), ball_3_trans.get_rect(topleft = (x + screen.get_width() * 0.012, y + screen.get_width() * 0.01))]
        return
    if len(ball_list) == 3:
        ball_board_position(ball_4_list[0])
        ball_4_rect_list = [ball_4_trans.get_rect(topleft = (x, y)), ball_4_trans.get_rect(topleft = (x + screen.get_width() * 0.005, y + screen.get_width() * 0.004)), ball_4_trans.get_rect(topleft = (x + screen.get_width() * 0.012, y + screen.get_width() * 0.01))]
        print(ball_list)
        return
    if len(ball_list) == 4:
        return

def ball_board_position(ball_img):
    # get the length of the list in order to know how many or statements to put in below to see if a new randint is needed
    list_length = len(ball_list)
    # generate a random number that represents the different tiles in the game
    num = randint(1, 15)

    if list_length == 1:
        if num == ball_list[0][0]:
            print('I am in list length 1')
            return ball_board_position(ball_img)
    
    if list_length == 2:
        if num == ball_list[0][0] or num == ball_list[1][0]:
            print('i am in list length 2')
            return ball_board_position(ball_img)
    
    if list_length == 3:
        if num == ball_list[0][0] or num == ball_list[1][0] or num == ball_list[2][0]:
            print('i am in list length 3')
            return ball_board_position(ball_img)

    if list_length == 4:
        if num == ball_list[0][0] or num == ball_list[1][0] or num == ball_list[2][0] or num == ball_list[3][0]:
            print('i am in list length 4')
            return ball_board_position(ball_img)

    screen_width_percentage = screen.get_width() * 0.015
    screen_height_percentage = screen.get_height() * 0.035

    if num == 1:
        ball_list.append((num, ball_img, ball_img.get_rect(topleft = (one_1_rect.left + screen_width_percentage, one_1_rect.top + screen_height_percentage))))
    elif num == 2:
        ball_list.append((num, ball_img, ball_img.get_rect(topleft = (one_2_rect.left + screen_width_percentage, one_2_rect.top + screen_height_percentage))))
    elif num == 3:
        ball_list.append((num, ball_img, ball_img.get_rect(topleft = (one_3_rect.left + screen_width_percentage, one_3_rect.top + screen_height_percentage))))
    elif num == 4:
        ball_list.append((num, ball_img, ball_img.get_rect(topleft = (one_4_rect.left + screen_width_percentage, one_4_rect.top + screen_height_percentage))))
    elif num == 5:
        ball_list.append((num, ball_img, ball_img.get_rect(topleft = (one_5_rect.left + screen_width_percentage, one_5_rect.top + screen_height_percentage))))
    elif num == 6:
        ball_list.append((num, ball_img, ball_img.get_rect(topleft = (two_1_rect.left + screen_width_percentage, two_1_rect.top + screen_height_percentage))))
    elif num == 7:
        ball_list.append((num, ball_img, ball_img.get_rect(topleft = (two_2_rect.left + screen_width_percentage, two_2_rect.top + screen_height_percentage))))
    elif num == 8:
        ball_list.append((num, ball_img, ball_img.get_rect(topleft = (two_3_rect.left + screen_width_percentage, two_3_rect.top + screen_height_percentage))))
    elif num == 9:
        ball_list.append((num, ball_img, ball_img.get_rect(topleft = (two_4_rect.left + screen_width_percentage, two_4_rect.top + screen_height_percentage))))
    elif num == 10:
        ball_list.append((num, ball_img, ball_img.get_rect(topleft = (two_5_rect.left + screen_width_percentage, two_5_rect.top + screen_height_percentage))))
    elif num == 11:
        ball_list.append((num, ball_img, ball_img.get_rect(topleft = (three_1_rect.left + screen_width_percentage, three_1_rect.top + screen_height_percentage))))
    elif num == 12:
        ball_list.append((num, ball_img, ball_img.get_rect(topleft = (three_2_rect.left + screen_width_percentage, three_2_rect.top + screen_height_percentage))))
    elif num == 13:
        ball_list.append((num, ball_img, ball_img.get_rect(topleft = (three_3_rect.left + screen_width_percentage, three_3_rect.top + screen_height_percentage))))
    elif num == 14:
        ball_list.append((num, ball_img, ball_img.get_rect(topleft = (three_4_rect.left + screen_width_percentage, three_4_rect.top + screen_height_percentage))))
    elif num == 15:
        ball_list.append((num, ball_img, ball_img.get_rect(topleft = (three_5_rect.left + screen_width_percentage, three_5_rect.top + screen_height_percentage))))

def set_flash_state():
    global rect_1_1_state
    global rect_1_2_state
    global rect_1_3_state
    global rect_1_4_state
    global rect_1_5_state
    global rect_2_1_state
    global rect_2_2_state
    global rect_2_3_state
    global rect_2_4_state
    global rect_2_5_state
    global rect_3_1_state
    global rect_3_2_state
    global rect_3_3_state
    global rect_3_4_state
    global rect_3_5_state

    rect_1_1_state = False
    rect_1_2_state = False
    rect_1_3_state = False
    rect_1_4_state = False
    rect_1_5_state = False
    rect_2_1_state = False
    rect_2_2_state = False
    rect_2_3_state = False
    rect_2_4_state = False
    rect_2_5_state = False
    rect_3_1_state = False
    rect_3_2_state = False
    rect_3_3_state = False
    rect_3_4_state = False
    rect_3_5_state = False

def set_flash_animation_state():
    global rect_1_1_animation
    global rect_1_2_animation
    global rect_1_3_animation
    global rect_1_4_animation
    global rect_1_5_animation
    global rect_2_1_animation
    global rect_2_2_animation
    global rect_2_3_animation
    global rect_2_4_animation
    global rect_2_5_animation
    global rect_3_1_animation
    global rect_3_2_animation
    global rect_3_3_animation
    global rect_3_4_animation
    global rect_3_5_animation

    rect_1_1_animation = 0
    rect_1_2_animation = 0
    rect_1_3_animation = 0
    rect_1_4_animation = 0
    rect_1_5_animation = 0
    rect_2_1_animation = 0
    rect_2_2_animation = 0
    rect_2_3_animation = 0
    rect_2_4_animation = 0
    rect_2_5_animation = 0
    rect_3_1_animation = 0
    rect_3_2_animation = 0
    rect_3_3_animation = 0
    rect_3_4_animation = 0
    rect_3_5_animation = 0

def flash_cards_animation(name):
    global rect_1_1_animation
    global rect_1_2_animation
    global rect_1_3_animation
    global rect_1_4_animation
    global rect_1_5_animation
    global rect_2_1_animation
    global rect_2_2_animation
    global rect_2_3_animation
    global rect_2_4_animation
    global rect_2_5_animation
    global rect_3_1_animation
    global rect_3_2_animation
    global rect_3_3_animation
    global rect_3_4_animation
    global rect_3_5_animation

    if name == 'rect_1_1':
        if rect_1_1_animation >= 4:
            screen.blit(one_1_image_trans[4], one_1_rect)
        elif rect_1_1_animation >= 3:
            screen.blit(one_1_image_trans[3], one_1_rect)
            rect_1_1_animation += 0.03
        elif rect_1_1_animation >= 2:
            screen.blit(one_1_image_trans[2], one_1_rect)
            rect_1_1_animation += 0.03
        elif rect_1_1_animation >= 1:
            screen.blit(one_1_image_trans[1], one_1_rect)
            rect_1_1_animation += 0.03
        elif rect_1_1_animation < 1:
            screen.blit(one_1_image_trans[0], one_1_rect)
            rect_1_1_animation += 0.03
    
    if name == 'rect_1_2':
        if rect_1_2_animation >= 4:
            screen.blit(one_2_image_trans[4], one_2_rect)
        elif rect_1_2_animation >= 3:
            screen.blit(one_2_image_trans[3], one_2_rect)
            rect_1_2_animation += 0.03
        elif rect_1_2_animation >= 2:
            screen.blit(one_2_image_trans[2], one_2_rect)
            rect_1_2_animation += 0.03
        elif rect_1_2_animation >= 1:
            screen.blit(one_2_image_trans[1], one_2_rect)
            rect_1_2_animation += 0.03
        elif rect_1_2_animation < 1:
            screen.blit(one_2_image_trans[0], one_2_rect)
            rect_1_2_animation += 0.03

    if name == 'rect_1_3':
        if rect_1_3_animation >= 4:
            screen.blit(one_3_image_trans[4], one_3_rect)
        elif rect_1_3_animation >= 3:
            screen.blit(one_3_image_trans[3], one_3_rect)
            rect_1_3_animation += 0.03
        elif rect_1_3_animation >= 2:
            screen.blit(one_3_image_trans[2], one_3_rect)
            rect_1_3_animation += 0.03
        elif rect_1_3_animation >= 1:
            screen.blit(one_3_image_trans[1], one_3_rect)
            rect_1_3_animation += 0.03
        elif rect_1_3_animation < 1:
            screen.blit(one_3_image_trans[0], one_3_rect)
            rect_1_3_animation += 0.03
        
    if name == 'rect_1_4':
        if rect_1_4_animation >= 4:
            screen.blit(one_4_image_trans[4], one_4_rect)
        elif rect_1_4_animation >= 3:
            screen.blit(one_4_image_trans[3], one_4_rect)
            rect_1_4_animation += 0.03
        elif rect_1_4_animation >= 2:
            screen.blit(one_4_image_trans[2], one_4_rect)
            rect_1_4_animation += 0.03
        elif rect_1_4_animation >= 1:
            screen.blit(one_4_image_trans[1], one_4_rect)
            rect_1_4_animation += 0.03
        elif rect_1_4_animation < 1:
            screen.blit(one_4_image_trans[0], one_4_rect)
            rect_1_4_animation += 0.03

    if name == 'rect_1_5':
        if rect_1_5_animation >= 4:
            screen.blit(one_5_image_trans[4], one_5_rect)
        elif rect_1_5_animation >= 3:
            screen.blit(one_5_image_trans[3], one_5_rect)
            rect_1_5_animation += 0.03
        elif rect_1_5_animation >= 2:
            screen.blit(one_5_image_trans[2], one_5_rect)
            rect_1_5_animation += 0.03
        elif rect_1_5_animation >= 1:
            screen.blit(one_5_image_trans[1], one_5_rect)
            rect_1_5_animation += 0.03
        elif rect_1_5_animation < 1:
            screen.blit(one_5_image_trans[0], one_5_rect)
            rect_1_5_animation += 0.03

    if name == 'rect_2_1':
        if rect_2_1_animation >= 4:
            screen.blit(two_1_image_trans[4], two_1_rect)
        elif rect_2_1_animation >= 3:
            screen.blit(two_1_image_trans[3], two_1_rect)
            rect_2_1_animation += 0.03
        elif rect_2_1_animation >= 2:
            screen.blit(two_1_image_trans[2], two_1_rect)
            rect_2_1_animation += 0.03
        elif rect_2_1_animation >= 1:
            screen.blit(two_1_image_trans[1], two_1_rect)
            rect_2_1_animation += 0.03
        elif rect_2_1_animation < 1:
            screen.blit(two_1_image_trans[0], two_1_rect)
            rect_2_1_animation += 0.03

    if name == 'rect_2_2':
        if rect_2_2_animation >= 4:
            screen.blit(two_2_image_trans[4], two_2_rect)
        elif rect_2_2_animation >= 3:
            screen.blit(two_2_image_trans[3], two_2_rect)
            rect_2_2_animation += 0.03
        elif rect_2_2_animation >= 2:
            screen.blit(two_2_image_trans[2], two_2_rect)
            rect_2_2_animation += 0.03
        elif rect_2_2_animation >= 1:
            screen.blit(two_2_image_trans[1], two_2_rect)
            rect_2_2_animation += 0.03
        elif rect_2_2_animation < 1:
            screen.blit(two_2_image_trans[0], two_2_rect)
            rect_2_2_animation += 0.03

    if name == 'rect_2_3':
        if rect_2_3_animation >= 4:
            screen.blit(two_3_image_trans[4], two_3_rect)
        elif rect_2_3_animation >= 3:
            screen.blit(two_3_image_trans[3], two_3_rect)
            rect_2_3_animation += 0.03
        elif rect_2_3_animation >= 2:
            screen.blit(two_3_image_trans[2], two_3_rect)
            rect_2_3_animation += 0.03
        elif rect_2_3_animation >= 1:
            screen.blit(two_3_image_trans[1], two_3_rect)
            rect_2_3_animation += 0.03
        elif rect_2_3_animation < 1:
            screen.blit(two_3_image_trans[0], two_3_rect)
            rect_2_3_animation += 0.03

    if name == 'rect_2_4':
        if rect_2_4_animation >= 4:
            screen.blit(two_4_image_trans[4], two_4_rect)
        elif rect_2_4_animation >= 3:
            screen.blit(two_4_image_trans[3], two_4_rect)
            rect_2_4_animation += 0.03
        elif rect_2_4_animation >= 2:
            screen.blit(two_4_image_trans[2], two_4_rect)
            rect_2_4_animation += 0.03
        elif rect_2_4_animation >= 1:
            screen.blit(two_4_image_trans[1], two_4_rect)
            rect_2_4_animation += 0.03
        elif rect_2_4_animation < 1:
            screen.blit(two_4_image_trans[0], two_4_rect)
            rect_2_4_animation += 0.03

    if name == 'rect_2_5':
        if rect_2_5_animation >= 4:
            screen.blit(two_5_image_trans[4], two_5_rect)
        elif rect_2_5_animation >= 3:
            screen.blit(two_5_image_trans[3], two_5_rect)
            rect_2_5_animation += 0.03
        elif rect_2_5_animation >= 2:
            screen.blit(two_5_image_trans[2], two_5_rect)
            rect_2_5_animation += 0.03
        elif rect_2_5_animation >= 1:
            screen.blit(two_5_image_trans[1], two_5_rect)
            rect_2_5_animation += 0.03
        elif rect_2_5_animation < 1:
            screen.blit(two_5_image_trans[0], two_5_rect)
            rect_2_5_animation += 0.03

    if name == 'rect_3_1':
        if rect_3_1_animation >= 4:
            screen.blit(three_1_image_trans[4], three_1_rect)
        elif rect_3_1_animation >= 3:
            screen.blit(three_1_image_trans[3], three_1_rect)
            rect_3_1_animation += 0.03
        elif rect_3_1_animation >= 2:
            screen.blit(three_1_image_trans[2], three_1_rect)
            rect_3_1_animation += 0.03
        elif rect_3_1_animation >= 1:
            screen.blit(three_1_image_trans[1], three_1_rect)
            rect_3_1_animation += 0.03
        elif rect_3_1_animation < 1:
            screen.blit(three_1_image_trans[0], three_1_rect)
            rect_3_1_animation += 0.03

    if name == 'rect_3_2':
        if rect_3_2_animation >= 4:
            screen.blit(three_2_image_trans[4], three_2_rect)
        elif rect_3_2_animation >= 3:
            screen.blit(three_2_image_trans[3], three_2_rect)
            rect_3_2_animation += 0.03
        elif rect_3_2_animation >= 2:
            screen.blit(three_2_image_trans[2], three_2_rect)
            rect_3_2_animation += 0.03
        elif rect_3_2_animation >= 1:
            screen.blit(three_2_image_trans[1], three_2_rect)
            rect_3_2_animation += 0.03
        elif rect_3_2_animation < 1:
            screen.blit(three_2_image_trans[0], three_2_rect)
            rect_3_2_animation += 0.03

    if name == 'rect_3_3':
        if rect_3_3_animation >= 4:
            screen.blit(three_3_image_trans[4], three_3_rect)
        elif rect_3_3_animation >= 3:
            screen.blit(three_3_image_trans[3], three_3_rect)
            rect_3_3_animation += 0.03
        elif rect_3_3_animation >= 2:
            screen.blit(three_3_image_trans[2], three_3_rect)
            rect_3_3_animation += 0.03
        elif rect_3_3_animation >= 1:
            screen.blit(three_3_image_trans[1], three_3_rect)
            rect_3_3_animation += 0.03
        elif rect_3_3_animation < 1:
            screen.blit(three_3_image_trans[0], three_3_rect)
            rect_3_3_animation += 0.03

    if name == 'rect_3_4':
        if rect_3_4_animation >= 4:
            screen.blit(three_4_image_trans[4], three_4_rect)
        elif rect_3_4_animation >= 3:
            screen.blit(three_4_image_trans[3], three_4_rect)
            rect_3_4_animation += 0.03
        elif rect_3_4_animation >= 2:
            screen.blit(three_4_image_trans[2], three_4_rect)
            rect_3_4_animation += 0.03
        elif rect_3_4_animation >= 1:
            screen.blit(three_4_image_trans[1], three_4_rect)
            rect_3_4_animation += 0.03
        elif rect_3_4_animation < 1:
            screen.blit(three_4_image_trans[0], three_4_rect)
            rect_3_4_animation += 0.03

    if name == 'rect_3_5':
        if rect_3_5_animation >= 4:
            screen.blit(three_5_image_trans[4], three_5_rect)
        elif rect_3_5_animation >= 3:
            screen.blit(three_5_image_trans[3], three_5_rect)
            rect_3_5_animation += 0.03
        elif rect_3_5_animation >= 2:
            screen.blit(three_5_image_trans[2], three_5_rect)
            rect_3_5_animation += 0.03
        elif rect_3_5_animation >= 1:
            screen.blit(three_5_image_trans[1], three_5_rect)
            rect_3_5_animation += 0.03
        elif rect_3_5_animation < 1:
            screen.blit(three_5_image_trans[0], three_5_rect)
            rect_3_5_animation += 0.03

def move_found_balls(name, pos):
    # first check if the event.pos collided with any of the flash cards rectangles and if the animation is not finished. If the animation is not finished, then do not execute the function
    if one_1_rect.collidepoint(pos):
        if rect_1_1_animation < 4:
            print('collided with one 1')
            return
    elif one_2_rect.collidepoint(pos):
        if rect_1_2_animation < 4:
            print('collided with one 2')
            return
    elif one_3_rect.collidepoint(pos):
        if rect_1_3_animation < 4:
         print('collided with one 3')
         return
    elif one_4_rect.collidepoint(pos):
        if rect_1_4_animation < 4:
            print('collided with one 4')
            return
    elif one_5_rect.collidepoint(pos):
        if rect_1_5_animation < 4:
            print('collided with one 5')
            return
    elif two_1_rect.collidepoint(pos):
        if rect_2_1_animation < 4:
            print('collided with two 1')
            return
    elif two_2_rect.collidepoint(pos):
        if rect_2_2_animation < 4:
            print('collided with two 2')
            return
    elif two_3_rect.collidepoint(pos):
        if rect_2_3_animation < 4:
            print('collided with two 3')
            return
    elif two_4_rect.collidepoint(pos):
        if rect_2_4_animation < 4:
            print('collided with two 4')
            return
    elif two_5_rect.collidepoint(pos):
        if rect_2_5_animation < 4:
            print('collided with two 5')
            return
    elif three_1_rect.collidepoint(pos):
        if rect_3_1_animation < 4:
            print('collided with three 1')
            return
    elif three_2_rect.collidepoint(pos):
        if rect_3_2_animation < 4:
            print('collided with three 2')
            return
    elif three_3_rect.collidepoint(pos):
        if rect_3_3_animation < 4:
            print('collided with three 3')
            return
    elif three_4_rect.collidepoint(pos):
        if rect_3_4_animation < 4:
            print('collided with three 4')
            return
    elif three_5_rect.collidepoint(pos):
        if rect_3_5_animation < 4:
            print('collided with three 5')
            return

    if name in balls_found_list:
        print('ball already found')
        return

    if len(balls_found_list) == 0:
        if name == 'ball_1':
            print('ball_1')
            balls_found_list.append('ball_1')
            ball_list[0][2].left = screen.get_width() * 0.86
            ball_list[0][2].top = screen.get_height() * 0.20
        if name == 'ball_2':
            print('ball_2')
            balls_found_list.append('ball_2')
            ball_list[1][2].left = screen.get_width() * 0.86
            ball_list[1][2].top = screen.get_height() * 0.20
        if name == 'ball_3':
            print('ball_3')
            balls_found_list.append('ball_3')
            ball_list[2][2].left = screen.get_width() * 0.86
            ball_list[2][2].top = screen.get_height() * 0.20
        if name == 'ball_4':
            print('ball_4')
            balls_found_list.append('ball_4')
            ball_list[3][2].left = screen.get_width() * 0.86
            ball_list[3][2].top = screen.get_height() * 0.20
    
    elif len(balls_found_list) == 1:
        if name == 'ball_1':
            print('ball_1')
            balls_found_list.append('ball_1')
            ball_list[0][2].left = screen.get_width() * 0.86
            ball_list[0][2].top = screen.get_height() * 0.30 
        if name == 'ball_2':
            print('ball_2')
            balls_found_list.append('ball_2')
            ball_list[1][2].left = screen.get_width() * 0.86
            ball_list[1][2].top = screen.get_height() * 0.30
        if name == 'ball_3':
            print('ball_3')
            balls_found_list.append('ball_3')
            ball_list[2][2].left = screen.get_width() * 0.86
            ball_list[2][2].top = screen.get_height() * 0.30
        if name == 'ball_4':
            print('ball_4')
            balls_found_list.append('ball_4')
            ball_list[3][2].left = screen.get_width() * 0.86
            ball_list[3][2].top = screen.get_height() * 0.30

    elif len(balls_found_list) == 2:
        if name == 'ball_1':
            print('ball_1')
            balls_found_list.append('ball_1')
            ball_list[0][2].left = screen.get_width() * 0.86
            ball_list[0][2].top = screen.get_height() * 0.40 
        if name == 'ball_2':
            print('ball_2')
            balls_found_list.append('ball_2')
            ball_list[1][2].left = screen.get_width() * 0.86
            ball_list[1][2].top = screen.get_height() * 0.40 
        if name == 'ball_3':
            print('ball_3')
            balls_found_list.append('ball_3')
            ball_list[2][2].left = screen.get_width() * 0.86
            ball_list[2][2].top = screen.get_height() * 0.40 
        if name == 'ball_4':
            print('ball_4')
            balls_found_list.append('ball_4')
            ball_list[3][2].left = screen.get_width() * 0.86
            ball_list[3][2].top = screen.get_height() * 0.40

    elif len(balls_found_list) == 3:
        if name == 'ball_1':
            print('ball_1')
            balls_found_list.append('ball_1')
            ball_list[0][2].left = screen.get_width() * 0.86
            ball_list[0][2].top = screen.get_height() * 0.50 
        if name == 'ball_2':
            print('ball_2')
            balls_found_list.append('ball_2')
            ball_list[1][2].left = screen.get_width() * 0.86
            ball_list[1][2].top = screen.get_height() * 0.50 
        if name == 'ball_3':
            print('ball_3')
            balls_found_list.append('ball_3')
            ball_list[2][2].left = screen.get_width() * 0.86
            ball_list[2][2].top = screen.get_height() * 0.50 
        if name == 'ball_4':
            print('ball_4')
            balls_found_list.append('ball_4')
            ball_list[3][2].left = screen.get_width() * 0.86
            ball_list[3][2].top = screen.get_height() * 0.50

    elif len(balls_found_list) == 4:
        print('all balls found')

# connect to database
conn = sqlite3.connect('words_database/words-database.db')
c = conn.cursor()
c.execute('SELECT * FROM a_initial')
words_and_paths = c.fetchall()
conn.close()

# init the game
pygame.init()

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


# set display size
screen = pygame.display.set_mode((screen_width * 0.90, screen_height * 0.90), pygame.RESIZABLE)
pygame.display.set_caption('Speech Game')

# start clock
clock = pygame.time.Clock()

# set the game_state to decide a game
game_state = 'cariboo_init'
game_phase = 'ball'
ball_list = []
balls_found_list = []

# main board rect
main_board = pygame.Rect((screen.get_width() * 0.05, screen.get_height() * 0.05), (screen.get_width() * 0.90, screen.get_height() * 0.90))
blue_ball_area = pygame.Rect((screen.get_width() * 0.80, screen.get_height() * 0.05), (screen.get_width() * 0.15, screen.get_height() * 0.90))

# import circles and transform
circle_1_image = pygame.image.load('graphics/ui/circle3.png').convert_alpha()
circle_1_image_transform = pygame.transform.scale(circle_1_image, (screen.get_width() * 0.04, screen.get_height() * 0.08))
circle_2_image_transform = pygame.transform.scale(circle_1_image, (screen.get_width() * 0.04, screen.get_height() * 0.08))
circle_3_image_transform = pygame.transform.scale(circle_1_image, (screen.get_width() * 0.04, screen.get_height() * 0.08))

# rects for circles
circle_1_rect = circle_1_image_transform.get_rect(center = (screen.get_width() * 0.15, screen.get_height() * 0.12))
circle_2_rect = circle_2_image_transform.get_rect(center = (screen.get_width() * 0.43, screen.get_height() * 0.12))
circle_3_rect = circle_3_image_transform.get_rect(center = (screen.get_width() * 0.71, screen.get_height() * 0.12))

# import font
# cariboo_font = pygame.font.Font('fonts/cariboo/LuckiestGuy-Regular.ttf', int(screen.get_width() * 0.03))
cariboo_font = pygame.font.Font('fonts/pixel/Pixeltype.ttf', int(screen.get_width() * 0.03))
game_title = cariboo_font.render('Cariboo', True, (233,169,21))
game_title_rect = game_title.get_rect(center = (screen.get_width() * 0.57, screen.get_height() * 0.13))
up_text = cariboo_font.render('Up', True, (185,136,235))
up_text_rect = up_text.get_rect(center = (screen.get_width() * 0.32, screen.get_height() * 0.13))

pixel_font = pygame.font.Font('fonts/pixel/Pixeltype.ttf', int(screen.get_width() * 0.05))
restart_text = pixel_font.render('Restart', False, (255,255,255))
game_text = pixel_font.render('Game', False, (255,255,255))
restart_text_rect = restart_text.get_rect(center = (screen.get_width() * 0.50, screen.get_height() * 0.47))
game_text_rect = game_text.get_rect(center = (screen.get_width() * 0.50, screen.get_height() * 0.54))

step_text = cariboo_font.render('Step', True, (117,198,184))
step_text_rect = step_text.get_rect(center = (screen.get_width() * 0.27, screen.get_height() * 0.13))

# import card images for cariboo
one_1_image = pygame.image.load(words_and_paths[0][1]).convert_alpha()
one_2_image = pygame.image.load(words_and_paths[1][1]).convert_alpha()
one_3_image = pygame.image.load(words_and_paths[2][1]).convert_alpha()
one_4_image = pygame.image.load(words_and_paths[3][1]).convert_alpha()
one_5_image = pygame.image.load(words_and_paths[4][1]).convert_alpha()
two_1_image = pygame.image.load(words_and_paths[5][1]).convert_alpha()
two_2_image = pygame.image.load(words_and_paths[6][1]).convert_alpha()
two_3_image = pygame.image.load(words_and_paths[7][1]).convert_alpha()
two_4_image = pygame.image.load(words_and_paths[8][1]).convert_alpha()
two_5_image = pygame.image.load(words_and_paths[9][1]).convert_alpha()
three_1_image = pygame.image.load(words_and_paths[10][1]).convert_alpha()
three_2_image = pygame.image.load(words_and_paths[11][1]).convert_alpha()
three_3_image = pygame.image.load(words_and_paths[12][1]).convert_alpha()
three_4_image = pygame.image.load(words_and_paths[13][1]).convert_alpha()
three_5_image = pygame.image.load(words_and_paths[14][1]).convert_alpha()

# background image for cariboo
cariboo_background_1 = pygame.image.load('graphics/backgrounds/platformer_background_4/background_cariboo.png').convert()
cariboo_background_2 = pygame.image.load('graphics/backgrounds/platformer_background_4/background_cariboo_2.png').convert()
cariboo_background_3 = pygame.image.load('graphics/backgrounds/platformer_background_4/background_cariboo_3.png').convert()
cariboo_background_1 = pygame.transform.scale(cariboo_background_1, (screen.get_width(), screen.get_height()))
cariboo_background_2 = pygame.transform.scale(cariboo_background_2, (screen.get_width(), screen.get_height()))
cariboo_background_3 = pygame.transform.scale(cariboo_background_3, (screen.get_width(), screen.get_height()))

# transforms for all card images
def images_and_rect_trans():

    global one_1_image_trans
    global one_2_image_trans
    global one_3_image_trans
    global one_4_image_trans
    global one_5_image_trans
    global two_1_image_trans
    global two_2_image_trans
    global two_3_image_trans
    global two_4_image_trans
    global two_5_image_trans
    global three_1_image_trans
    global three_2_image_trans
    global three_3_image_trans
    global three_4_image_trans
    global three_5_image_trans

    global restart_button_image
    global restart_button_rect

    one_1_image_trans = [pygame.transform.scale(one_1_image, (screen.get_width() * 0.07, screen.get_height() * 0.21)), pygame.transform.scale(one_1_image, (screen.get_width() * 0.07, screen.get_height() * 0.14)), pygame.transform.scale(one_1_image, (screen.get_width() * 0.07, screen.get_height() * 0.07)), pygame.transform.scale(one_1_image, (screen.get_width() * 0.07, screen.get_height() * 0.03)), pygame.transform.scale(one_1_image, (screen.get_width() * 0.07, screen.get_height() * 0.002))]
    one_2_image_trans = [pygame.transform.scale(one_2_image, (screen.get_width() * 0.07, screen.get_height() * 0.21)), pygame.transform.scale(one_2_image, (screen.get_width() * 0.07, screen.get_height() * 0.14)), pygame.transform.scale(one_2_image, (screen.get_width() * 0.07, screen.get_height() * 0.07)), pygame.transform.scale(one_2_image, (screen.get_width() * 0.07, screen.get_height() * 0.03)), pygame.transform.scale(one_2_image, (screen.get_width() * 0.07, screen.get_height() * 0.002))]
    one_3_image_trans = [pygame.transform.scale(one_3_image, (screen.get_width() * 0.07, screen.get_height() * 0.21)), pygame.transform.scale(one_3_image, (screen.get_width() * 0.07, screen.get_height() * 0.14)), pygame.transform.scale(one_3_image, (screen.get_width() * 0.07, screen.get_height() * 0.07)), pygame.transform.scale(one_3_image, (screen.get_width() * 0.07, screen.get_height() * 0.03)), pygame.transform.scale(one_3_image, (screen.get_width() * 0.07, screen.get_height() * 0.002))]
    one_4_image_trans = [pygame.transform.scale(one_4_image, (screen.get_width() * 0.07, screen.get_height() * 0.21)), pygame.transform.scale(one_4_image, (screen.get_width() * 0.07, screen.get_height() * 0.14)), pygame.transform.scale(one_4_image, (screen.get_width() * 0.07, screen.get_height() * 0.07)), pygame.transform.scale(one_4_image, (screen.get_width() * 0.07, screen.get_height() * 0.03)), pygame.transform.scale(one_4_image, (screen.get_width() * 0.07, screen.get_height() * 0.002))]
    one_5_image_trans = [pygame.transform.scale(one_5_image, (screen.get_width() * 0.07, screen.get_height() * 0.21)), pygame.transform.scale(one_5_image, (screen.get_width() * 0.07, screen.get_height() * 0.14)), pygame.transform.scale(one_5_image, (screen.get_width() * 0.07, screen.get_height() * 0.07)), pygame.transform.scale(one_5_image, (screen.get_width() * 0.07, screen.get_height() * 0.03)), pygame.transform.scale(one_5_image, (screen.get_width() * 0.07, screen.get_height() * 0.002))]
    two_1_image_trans = [pygame.transform.scale(two_1_image, (screen.get_width() * 0.07, screen.get_height() * 0.21)), pygame.transform.scale(two_1_image, (screen.get_width() * 0.07, screen.get_height() * 0.14)), pygame.transform.scale(two_1_image, (screen.get_width() * 0.07, screen.get_height() * 0.07)), pygame.transform.scale(two_1_image, (screen.get_width() * 0.07, screen.get_height() * 0.03)), pygame.transform.scale(two_1_image, (screen.get_width() * 0.07, screen.get_height() * 0.002))]
    two_2_image_trans = [pygame.transform.scale(two_2_image, (screen.get_width() * 0.07, screen.get_height() * 0.21)), pygame.transform.scale(two_2_image, (screen.get_width() * 0.07, screen.get_height() * 0.14)), pygame.transform.scale(two_2_image, (screen.get_width() * 0.07, screen.get_height() * 0.07)), pygame.transform.scale(two_2_image, (screen.get_width() * 0.07, screen.get_height() * 0.03)), pygame.transform.scale(two_2_image, (screen.get_width() * 0.07, screen.get_height() * 0.002))]
    two_3_image_trans = [pygame.transform.scale(two_3_image, (screen.get_width() * 0.07, screen.get_height() * 0.21)), pygame.transform.scale(two_3_image, (screen.get_width() * 0.07, screen.get_height() * 0.14)), pygame.transform.scale(two_3_image, (screen.get_width() * 0.07, screen.get_height() * 0.07)), pygame.transform.scale(two_3_image, (screen.get_width() * 0.07, screen.get_height() * 0.03)), pygame.transform.scale(two_3_image, (screen.get_width() * 0.07, screen.get_height() * 0.002))]
    two_4_image_trans = [pygame.transform.scale(two_4_image, (screen.get_width() * 0.07, screen.get_height() * 0.21)), pygame.transform.scale(two_4_image, (screen.get_width() * 0.07, screen.get_height() * 0.14)), pygame.transform.scale(two_4_image, (screen.get_width() * 0.07, screen.get_height() * 0.07)), pygame.transform.scale(two_4_image, (screen.get_width() * 0.07, screen.get_height() * 0.03)), pygame.transform.scale(two_4_image, (screen.get_width() * 0.07, screen.get_height() * 0.002))]
    two_5_image_trans = [pygame.transform.scale(two_5_image, (screen.get_width() * 0.07, screen.get_height() * 0.21)), pygame.transform.scale(two_5_image, (screen.get_width() * 0.07, screen.get_height() * 0.14)), pygame.transform.scale(two_5_image, (screen.get_width() * 0.07, screen.get_height() * 0.07)), pygame.transform.scale(two_5_image, (screen.get_width() * 0.07, screen.get_height() * 0.03)), pygame.transform.scale(two_5_image, (screen.get_width() * 0.07, screen.get_height() * 0.002))]
    three_1_image_trans = [pygame.transform.scale(three_1_image, (screen.get_width() * 0.07, screen.get_height() * 0.21)), pygame.transform.scale(three_1_image, (screen.get_width() * 0.07, screen.get_height() * 0.14)), pygame.transform.scale(three_1_image, (screen.get_width() * 0.07, screen.get_height() * 0.07)), pygame.transform.scale(three_1_image, (screen.get_width() * 0.07, screen.get_height() * 0.03)), pygame.transform.scale(three_1_image, (screen.get_width() * 0.07, screen.get_height() * 0.002))]
    three_2_image_trans = [pygame.transform.scale(three_2_image, (screen.get_width() * 0.07, screen.get_height() * 0.21)), pygame.transform.scale(three_2_image, (screen.get_width() * 0.07, screen.get_height() * 0.14)), pygame.transform.scale(three_2_image, (screen.get_width() * 0.07, screen.get_height() * 0.07)), pygame.transform.scale(three_2_image, (screen.get_width() * 0.07, screen.get_height() * 0.03)), pygame.transform.scale(three_2_image, (screen.get_width() * 0.07, screen.get_height() * 0.002))]
    three_3_image_trans = [pygame.transform.scale(three_3_image, (screen.get_width() * 0.07, screen.get_height() * 0.21)), pygame.transform.scale(three_3_image, (screen.get_width() * 0.07, screen.get_height() * 0.14)), pygame.transform.scale(three_3_image, (screen.get_width() * 0.07, screen.get_height() * 0.07)), pygame.transform.scale(three_3_image, (screen.get_width() * 0.07, screen.get_height() * 0.03)), pygame.transform.scale(three_3_image, (screen.get_width() * 0.07, screen.get_height() * 0.002))]
    three_4_image_trans = [pygame.transform.scale(three_4_image, (screen.get_width() * 0.07, screen.get_height() * 0.21)), pygame.transform.scale(three_4_image, (screen.get_width() * 0.07, screen.get_height() * 0.14)), pygame.transform.scale(three_4_image, (screen.get_width() * 0.07, screen.get_height() * 0.07)), pygame.transform.scale(three_4_image, (screen.get_width() * 0.07, screen.get_height() * 0.03)), pygame.transform.scale(three_4_image, (screen.get_width() * 0.07, screen.get_height() * 0.002))]
    three_5_image_trans = [pygame.transform.scale(three_5_image, (screen.get_width() * 0.07, screen.get_height() * 0.21)), pygame.transform.scale(three_5_image, (screen.get_width() * 0.07, screen.get_height() * 0.14)), pygame.transform.scale(three_5_image, (screen.get_width() * 0.07, screen.get_height() * 0.07)), pygame.transform.scale(three_5_image, (screen.get_width() * 0.07, screen.get_height() * 0.03)), pygame.transform.scale(three_5_image, (screen.get_width() * 0.07, screen.get_height() * 0.002))]

    global one_1_rect
    global one_2_rect
    global one_3_rect
    global one_4_rect
    global one_5_rect
    global two_1_rect
    global two_2_rect
    global two_3_rect
    global two_4_rect
    global two_5_rect
    global three_1_rect
    global three_2_rect
    global three_3_rect
    global three_4_rect
    global three_5_rect

    # first row of flash cards
    one_1_rect = one_1_image_trans[0].get_rect(center = (screen.get_width() * 0.15, screen.get_height() * 0.30))
    one_2_rect = one_2_image_trans[0].get_rect(center = (screen.get_width() * 0.29, screen.get_height() * 0.30))
    one_3_rect = one_3_image_trans[0].get_rect(center = (screen.get_width() * 0.43, screen.get_height() * 0.30))
    one_4_rect = one_4_image_trans[0].get_rect(center = (screen.get_width() * 0.57, screen.get_height() * 0.30))
    one_5_rect = one_5_image_trans[0].get_rect(center = (screen.get_width() * 0.71, screen.get_height() * 0.30))

    # second row of flash cards
    two_1_rect = two_1_image_trans[0].get_rect(center = (screen.get_width() * 0.15, screen.get_height() * 0.55))
    two_2_rect = two_2_image_trans[0].get_rect(center = (screen.get_width() * 0.29, screen.get_height() * 0.55))
    two_3_rect = two_3_image_trans[0].get_rect(center = (screen.get_width() * 0.43, screen.get_height() * 0.55))
    two_4_rect = two_4_image_trans[0].get_rect(center = (screen.get_width() * 0.57, screen.get_height() * 0.55))
    two_5_rect = two_5_image_trans[0].get_rect(center = (screen.get_width() * 0.71, screen.get_height() * 0.55))

    # third row of flash cards
    three_1_rect = three_1_image_trans[0].get_rect(center = (screen.get_width() * 0.15, screen.get_height() * 0.80))
    three_2_rect = three_2_image_trans[0].get_rect(center = (screen.get_width() * 0.29, screen.get_height() * 0.80))
    three_3_rect = three_3_image_trans[0].get_rect(center = (screen.get_width() * 0.43, screen.get_height() * 0.80))
    three_4_rect = three_4_image_trans[0].get_rect(center = (screen.get_width() * 0.57, screen.get_height() * 0.80))
    three_5_rect = three_5_image_trans[0].get_rect(center = (screen.get_width() * 0.71, screen.get_height() * 0.80))

    ## button to restart the game
    restart_button_image = pygame.image.load('graphics/buttons/20.png')
    restart_button_image = pygame.transform.scale(restart_button_image, (screen.get_width() * 0.20, screen.get_height() * 0.60))
    restart_button_rect = restart_button_image.get_rect(center = (screen.get_width() * 0.50, screen.get_height() * 0.50))

def chest_update():
    global chest_image_trans
    global chest_image_rect
    global chest_ajar_trans
    global chest_ajar_rect
    global chest_open_trans
    global chest_open_rect

    chest_image = pygame.image.load('graphics/neutral/chest_closed.png').convert_alpha()
    chest_image_trans = pygame.transform.scale(chest_image, (screen.get_width() * 0.07, screen.get_height() * 0.11))
    chest_image_rect = chest_image_trans.get_rect(center = (screen.get_width() * 0.88, screen.get_height() * 0.13))

    chest_ajar_image = pygame.image.load('graphics/neutral/chest_ajar.png').convert_alpha()
    chest_ajar_trans = pygame.transform.scale(chest_ajar_image, (screen.get_width() * 0.07, screen.get_height() * 0.11))
    chest_ajar_rect = chest_ajar_trans.get_rect(center = (screen.get_width() * 0.88, screen.get_height() * 0.13))

    chest_open_image = pygame.image.load('graphics/neutral/chest_open.png').convert_alpha()
    chest_open_trans = pygame.transform.scale(chest_open_image, (screen.get_width() * 0.07, screen.get_height() * 0.11))
    chest_open_rect = chest_open_trans.get_rect(center = (screen.get_width() * 0.88, screen.get_height() * 0.13))

def ball_update():
    global ball_1_trans
    global ball_2_trans
    global ball_3_trans
    global ball_4_trans
    global ball_1_image

    global ball_1_list
    global ball_2_list
    global ball_3_list
    global ball_4_list

    global ball_1_animation
    global ball_2_animation
    global ball_3_animation
    global ball_4_animation

    ball_1_image = pygame.image.load('graphics/neutral/bubble_1.png').convert_alpha()
    ball_2_image = pygame.image.load('graphics/neutral/bubble_2.png').convert_alpha()
    ball_3_image = pygame.image.load('graphics/neutral/bubble_3.png').convert_alpha()
    ball_4_image = pygame.image.load('graphics/neutral/bubble_4.png').convert_alpha()

    ball_1_list = [pygame.transform.scale(ball_1_image, (screen.get_width() * 0.04, screen.get_height() * 0.08)), pygame.transform.scale(ball_1_image, (screen.get_width() * 0.03, screen.get_height() * 0.06)), pygame.transform.scale(ball_1_image, (screen.get_width() * 0.015, screen.get_height() * 0.03))]
    ball_2_list = [pygame.transform.scale(ball_2_image, (screen.get_width() * 0.04, screen.get_height() * 0.08)), pygame.transform.scale(ball_2_image, (screen.get_width() * 0.03, screen.get_height() * 0.06)), pygame.transform.scale(ball_2_image, (screen.get_width() * 0.015, screen.get_height() * 0.03))]
    ball_3_list = [pygame.transform.scale(ball_3_image, (screen.get_width() * 0.04, screen.get_height() * 0.08)), pygame.transform.scale(ball_3_image, (screen.get_width() * 0.03, screen.get_height() * 0.06)), pygame.transform.scale(ball_3_image, (screen.get_width() * 0.015, screen.get_height() * 0.03))]
    ball_4_list = [pygame.transform.scale(ball_4_image, (screen.get_width() * 0.04, screen.get_height() * 0.08)), pygame.transform.scale(ball_4_image, (screen.get_width() * 0.03, screen.get_height() * 0.06)), pygame.transform.scale(ball_4_image, (screen.get_width() * 0.015, screen.get_height() * 0.03))]

    ball_1_trans = pygame.transform.scale(ball_1_image, (screen.get_width() * 0.05, screen.get_height() * 0.08))
    ball_2_trans = pygame.transform.scale(ball_2_image, (screen.get_width() * 0.05, screen.get_height() * 0.08))
    ball_3_trans = pygame.transform.scale(ball_3_image, (screen.get_width() * 0.05, screen.get_height() * 0.08))
    ball_4_trans = pygame.transform.scale(ball_4_image, (screen.get_width() * 0.05, screen.get_height() * 0.08))

def ball_animation_init():
    global ball_1_animation
    global ball_2_animation
    global ball_3_animation
    global ball_4_animation
    global chest_animation
    global background_animation

    ball_1_animation = 0
    ball_2_animation = 0
    ball_3_animation = 0
    ball_4_animation = 0
    chest_animation = 0
    background_animation = 0

# rects for card images
images_and_rect_trans()
chest_update()
ball_update()
set_flash_state()
set_flash_animation_state()
ball_animation_init()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            main_board = pygame.Rect((screen.get_width() * 0.05, screen.get_height() * 0.05), (screen.get_width() * 0.90, screen.get_height() * 0.90))
            blue_ball_area = pygame.Rect((screen.get_width() * 0.80, screen.get_height() * 0.05), (screen.get_width() * 0.15, screen.get_height() * 0.90))
            # resize circles
            circle_1_image_transform = pygame.transform.scale(circle_1_image, (screen.get_width() * 0.04, screen.get_height() * 0.08))
            circle_2_image_transform = pygame.transform.scale(circle_1_image, (screen.get_width() * 0.04, screen.get_height() * 0.08))
            circle_3_image_transform = pygame.transform.scale(circle_1_image, (screen.get_width() * 0.04, screen.get_height() * 0.08))

            # re-position rects
            circle_1_rect = circle_1_image_transform.get_rect(center = (screen.get_width() * 0.15, screen.get_height() * 0.12))
            circle_2_rect = circle_2_image_transform.get_rect(center = (screen.get_width() * 0.43, screen.get_height() * 0.12))
            circle_3_rect = circle_3_image_transform.get_rect(center = (screen.get_width() * 0.71, screen.get_height() * 0.12))

            # resize title text
            cariboo_font = pygame.font.Font('fonts/cariboo/LuckiestGuy-Regular.ttf', int(screen.get_width() * 0.03))
            game_title = cariboo_font.render('Cariboo', True, (233,169,21))
            game_title_rect = game_title.get_rect(center = (screen.get_width() * 0.57, screen.get_height() * 0.13))

            up_text = cariboo_font.render('Up', True, (185,136,235))
            up_text_rect = up_text.get_rect(center = (screen.get_width() * 0.32, screen.get_height() * 0.13))

            step_text = cariboo_font.render('Step', True, (117,198,184))
            step_text_rect = step_text.get_rect(center = (screen.get_width() * 0.27, screen.get_height() * 0.13))

            # resize all flash cards
            images_and_rect_trans()
            chest_update()
            ball_update()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Collider for inserting balls to the top circles
            if circle_1_rect.collidepoint(event.pos) :
                position_ball(circle_1_rect.left, circle_1_rect.top)
            elif circle_2_rect.collidepoint(event.pos):
                position_ball(circle_2_rect.left, circle_2_rect.top)
            elif circle_3_rect.collidepoint(event.pos):
                position_ball(circle_3_rect.left, circle_3_rect.top)

            # Colliders for flash cards/main rectangles
            if len(ball_list) == 4:
                # first row of flash cards/rectangles
                if one_1_rect.collidepoint(event.pos):
                    rect_1_1_state = True
                if one_2_rect.collidepoint(event.pos):
                    rect_1_2_state = True
                if one_3_rect.collidepoint(event.pos):
                    rect_1_3_state = True
                if one_4_rect.collidepoint(event.pos):
                    rect_1_4_state = True
                if one_5_rect.collidepoint(event.pos):
                    rect_1_5_state = True

                ## second row of flash cards/rectangles
                if two_1_rect.collidepoint(event.pos):
                    rect_2_1_state = True
                if two_2_rect.collidepoint(event.pos):
                    rect_2_2_state = True
                if two_3_rect.collidepoint(event.pos):
                    rect_2_3_state = True
                if two_4_rect.collidepoint(event.pos):
                    rect_2_4_state = True
                if two_5_rect.collidepoint(event.pos):
                    rect_2_5_state = True
                
                ### third row of flash cards/rectangles
                if three_1_rect.collidepoint(event.pos):
                    rect_3_1_state = True
                if three_2_rect.collidepoint(event.pos):
                    rect_3_2_state = True
                if three_3_rect.collidepoint(event.pos):
                    rect_3_3_state = True
                if three_4_rect.collidepoint(event.pos):
                    rect_3_4_state = True
                if three_5_rect.collidepoint(event.pos):
                    rect_3_5_state = True
                
                ### Colliders for balls in order to move them
                if ball_list[0][2].collidepoint(event.pos):
                    print('collided with ball 1')
                    move_found_balls('ball_1', event.pos)

                if ball_list[1][2].collidepoint(event.pos):
                    print('collided with ball 2')
                    move_found_balls('ball_2', event.pos)

                if ball_list[2][2].collidepoint(event.pos):
                    print('collided with ball 3')
                    move_found_balls('ball_3', event.pos)
                
                if ball_list[3][2].collidepoint(event.pos):
                    print('collided with ball_4')
                    move_found_balls('ball_4', event.pos)
                
                # collider to restart game
            if restart_button_rect.collidepoint(event.pos) and game_state == 'cariboo_finished':
                print('game restarting')
                restart_cariboo()

    if game_state == 'cariboo_init':
        game_state = 'cariboo'


    if game_state == 'cariboo':
        # screen.fill((94,129,162))
        screen.blit(cariboo_background_1, (0, 0))
        # if background_animation < 1:
        #     screen.blit(cariboo_background_1, (0, 0))
        #     background_animation += 0.03
        # elif background_animation > 3:
        #     screen.blit(cariboo_background_3, (0,0))
        #     background_animation = 0
        # elif background_animation > 2:
        #     screen.blit(cariboo_background_3, (0,0))
        #     background_animation += 0.03
        # elif background_animation > 1:
        #     screen.blit(cariboo_background_2, (0, 0))
        #     background_animation += 0.03
        pygame.draw.rect(screen, 'Yellow', main_board, 0, 20)
        pygame.draw.rect(screen, 'Blue', blue_ball_area, 0, 20)
        
        # pygame.draw.circle(screen, 'Black', (screen.get_width() * 0.15, screen.get_height() * 0.12), 50)
        screen.blit(circle_1_image_transform, circle_1_rect)
        screen.blit(circle_2_image_transform, circle_2_rect)
        screen.blit(circle_3_image_transform, circle_3_rect)

        # cariboo title
        screen.blit(game_title, game_title_rect)

        # logo text
        screen.blit(up_text, up_text_rect)
        screen.blit(step_text, step_text_rect)

        ## position the balls behind flash cards after balls are inserted into the game
        try:
            screen.blit(ball_list[0][1], ball_list[0][2])
        except:
            pass

        try:
            screen.blit(ball_list[1][1], ball_list[1][2])
        except:
            pass

        try:
            screen.blit(ball_list[2][1], ball_list[2][2])
        except:
            pass
        try:
            screen.blit(ball_list[3][1], ball_list[3][2])
        except:
            pass
        
        # first row of flash card
        if rect_1_1_state is False: screen.blit(one_1_image_trans[0], one_1_rect)
        elif rect_1_1_animation >= 4: screen.blit(one_1_image_trans[4], one_1_rect)
        elif rect_1_1_state: flash_cards_animation('rect_1_1')

        if rect_1_2_state is False:  screen.blit(one_2_image_trans[0], one_2_rect)
        elif rect_1_2_animation >= 4: screen.blit(one_2_image_trans[4], one_2_rect)
        elif rect_1_2_state: flash_cards_animation('rect_1_2')

        if rect_1_3_state is False: screen.blit(one_3_image_trans[0], one_3_rect)
        elif rect_1_3_animation >= 4: screen.blit(one_3_image_trans[4], one_3_rect)
        elif rect_1_3_state: flash_cards_animation('rect_1_3')

        if rect_1_4_state is False: screen.blit(one_4_image_trans[0], one_4_rect)
        elif rect_1_4_animation >= 4: screen.blit(one_4_image_trans[4], one_4_rect)
        elif rect_1_4_state: flash_cards_animation('rect_1_4')

        if rect_1_5_state is False: screen.blit(one_5_image_trans[0], one_5_rect)
        elif rect_1_5_animation >= 4: screen.blit(one_5_image_trans[4], one_5_rect)
        elif rect_1_5_state: flash_cards_animation('rect_1_5')

        # second row of flash cards
        if rect_2_1_state is False: screen.blit(two_1_image_trans[0], two_1_rect)
        if rect_2_1_state: flash_cards_animation('rect_2_1')

        if rect_2_2_state is False: screen.blit(two_2_image_trans[0], two_2_rect)
        if rect_2_2_state: flash_cards_animation('rect_2_2')

        if rect_2_3_state is False: screen.blit(two_3_image_trans[0], two_3_rect)
        if rect_2_3_state: flash_cards_animation('rect_2_3')

        if rect_2_4_state is False: screen.blit(two_4_image_trans[0], two_4_rect)
        if rect_2_4_state: flash_cards_animation('rect_2_4')

        if rect_2_5_state is False: screen.blit(two_5_image_trans[0], two_5_rect)
        if rect_2_5_state: flash_cards_animation('rect_2_5')

        # third row of flash cards
        if rect_3_1_state is False: screen.blit(three_1_image_trans[0], three_1_rect)
        if rect_3_1_state: flash_cards_animation('rect_3_1')

        if rect_3_2_state is False: screen.blit(three_2_image_trans[0], three_2_rect)
        if rect_3_2_state: flash_cards_animation('rect_3_2')

        if rect_3_3_state is False: screen.blit(three_3_image_trans[0], three_3_rect)
        if rect_3_3_state: flash_cards_animation('rect_3_3')

        if rect_3_4_state is False: screen.blit(three_4_image_trans[0], three_4_rect)
        if rect_3_4_state: flash_cards_animation('rect_3_4')

        if rect_3_5_state is False: screen.blit(three_5_image_trans[0], three_5_rect)
        if rect_3_5_state: flash_cards_animation('rect_3_5')

        # chest
        if len(balls_found_list) < 4: screen.blit(chest_image_trans, chest_image_rect)
        if len(balls_found_list) == 4:
            if chest_animation <= 1:
                chest_animation += 0.03
                screen.blit(chest_ajar_trans, chest_ajar_rect)
            if chest_animation > 1:
                screen.blit(chest_open_trans, chest_open_rect)
                game_state = 'cariboo_finished'

        # animate the balls going into the holes
        try:   
            if ball_1_animation < 1:
                screen.blit(ball_1_list[0], ball_1_rect_list[0])
                ball_1_animation += 0.03
            elif ball_1_animation < 2:
                screen.blit(ball_1_list[1], ball_1_rect_list[1])
                ball_1_animation += 0.03
            elif ball_1_animation < 3:
                screen.blit(ball_1_list[2], ball_1_rect_list[2])
                ball_1_animation += 0.03
            elif ball_1_animation < 4:
                pass
        except: pass
        try:
            if ball_2_animation < 1:
                screen.blit(ball_2_list[0], ball_2_rect_list[0])
                ball_2_animation += 0.03
            elif ball_2_animation < 2:
                screen.blit(ball_2_list[1], ball_2_rect_list[1])
                ball_2_animation += 0.03
            elif ball_2_animation < 3:
                screen.blit(ball_2_list[2], ball_2_rect_list[2])
                ball_2_animation += 0.03
            elif ball_2_animation < 4:
                pass            
        except: pass
        try:
            if ball_3_animation < 1:
                screen.blit(ball_3_list[0], ball_3_rect_list[0])
                ball_3_animation += 0.03
            elif ball_3_animation < 2:
                screen.blit(ball_3_list[1], ball_3_rect_list[1])
                ball_3_animation += 0.03
            elif ball_3_animation < 3:
                screen.blit(ball_3_list[2], ball_3_rect_list[2])
                ball_3_animation += 0.03
            elif ball_3_animation < 4:
                pass     
        except: pass

        try:
            if ball_4_animation < 1:
                screen.blit(ball_4_list[0], ball_4_rect_list[0])
                ball_4_animation += 0.03
            elif ball_4_animation < 2:
                screen.blit(ball_4_list[1], ball_4_rect_list[1])
                ball_4_animation += 0.03
            elif ball_4_animation < 3:
                screen.blit(ball_4_list[2], ball_4_rect_list[2])
                ball_4_animation += 0.03
            elif ball_4_animation < 4:
                pass     
        except: pass

    if game_state == 'cariboo_finished':
        screen.blit(restart_button_image, restart_button_rect)
        screen.blit(restart_text, restart_text_rect)
        screen.blit(game_text, game_text_rect)

    # update the game
    pygame.display.update()
    # set fps to 60
    clock.tick(60)
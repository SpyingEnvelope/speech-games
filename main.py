from fileinput import close
from turtle import circle
import pygame
from pygame import gfxdraw
from sys import exit
import tkinter as tk
import sqlite3
from random import randint
import math

# functions/methods

def restart_cariboo(restart = False):
    global ball_list
    global balls_found_list
    global chest_animation_state
    global fade_in_animation
    global reward_animation

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
    chest_animation_state = 'not_finished'
    fade_in_animation = 'not_finished'
    reward_animation = 'not_finished'
    if restart:
        global game_state
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
            ball_list[0][2].left = screen.get_width() * 0.87
            ball_list[0][2].top = screen.get_height() * 0.20
        if name == 'ball_2':
            print('ball_2')
            balls_found_list.append('ball_2')
            ball_list[1][2].left = screen.get_width() * 0.87
            ball_list[1][2].top = screen.get_height() * 0.20
        if name == 'ball_3':
            print('ball_3')
            balls_found_list.append('ball_3')
            ball_list[2][2].left = screen.get_width() * 0.87
            ball_list[2][2].top = screen.get_height() * 0.20
        if name == 'ball_4':
            print('ball_4')
            balls_found_list.append('ball_4')
            ball_list[3][2].left = screen.get_width() * 0.87
            ball_list[3][2].top = screen.get_height() * 0.20
    
    elif len(balls_found_list) == 1:
        if name == 'ball_1':
            print('ball_1')
            balls_found_list.append('ball_1')
            ball_list[0][2].left = screen.get_width() * 0.87
            ball_list[0][2].top = screen.get_height() * 0.30 
        if name == 'ball_2':
            print('ball_2')
            balls_found_list.append('ball_2')
            ball_list[1][2].left = screen.get_width() * 0.87
            ball_list[1][2].top = screen.get_height() * 0.30
        if name == 'ball_3':
            print('ball_3')
            balls_found_list.append('ball_3')
            ball_list[2][2].left = screen.get_width() * 0.87
            ball_list[2][2].top = screen.get_height() * 0.30
        if name == 'ball_4':
            print('ball_4')
            balls_found_list.append('ball_4')
            ball_list[3][2].left = screen.get_width() * 0.87
            ball_list[3][2].top = screen.get_height() * 0.30

    elif len(balls_found_list) == 2:
        if name == 'ball_1':
            print('ball_1')
            balls_found_list.append('ball_1')
            ball_list[0][2].left = screen.get_width() * 0.87
            ball_list[0][2].top = screen.get_height() * 0.40 
        if name == 'ball_2':
            print('ball_2')
            balls_found_list.append('ball_2')
            ball_list[1][2].left = screen.get_width() * 0.87
            ball_list[1][2].top = screen.get_height() * 0.40 
        if name == 'ball_3':
            print('ball_3')
            balls_found_list.append('ball_3')
            ball_list[2][2].left = screen.get_width() * 0.87
            ball_list[2][2].top = screen.get_height() * 0.40 
        if name == 'ball_4':
            print('ball_4')
            balls_found_list.append('ball_4')
            ball_list[3][2].left = screen.get_width() * 0.87
            ball_list[3][2].top = screen.get_height() * 0.40

    elif len(balls_found_list) == 3:
        if name == 'ball_1':
            print('ball_1')
            balls_found_list.append('ball_1')
            ball_list[0][2].left = screen.get_width() * 0.87
            ball_list[0][2].top = screen.get_height() * 0.50 
        if name == 'ball_2':
            print('ball_2')
            balls_found_list.append('ball_2')
            ball_list[1][2].left = screen.get_width() * 0.87
            ball_list[1][2].top = screen.get_height() * 0.50 
        if name == 'ball_3':
            print('ball_3')
            balls_found_list.append('ball_3')
            ball_list[2][2].left = screen.get_width() * 0.87
            ball_list[2][2].top = screen.get_height() * 0.50 
        if name == 'ball_4':
            print('ball_4')
            balls_found_list.append('ball_4')
            ball_list[3][2].left = screen.get_width() * 0.87
            ball_list[3][2].top = screen.get_height() * 0.50

    elif len(balls_found_list) == 4:
        print('all balls found')

def initiate_menu_buttons():
    global back_button
    global back_button_rect
    global close_button
    global close_button_rect

    back_button = pygame.image.load('graphics/buttons/backward_btn.png')
    close_button = pygame.image.load('graphics/buttons/close_btn.png')

    back_button = pygame.transform.scale(back_button, (screen.get_width() * 0.03, screen.get_height() * 0.06))
    close_button = pygame.transform.scale(close_button, (screen.get_width() * 0.03, screen.get_height() * 0.06))

    back_button_rect = back_button.get_rect(topleft = (screen.get_width() * 0.01, screen.get_height() * 0.01))
    close_button_rect = close_button.get_rect(topright = (screen.get_width() - (screen.get_width() * 0.01) , screen.get_height() * 0.01))

def image_zoom(img, rect):
    global chest_animation_state
    global chest_closed_zoom
    global chest_closed_zoom_rect

    global chest_ajar_zoom
    global chest_ajar_zoom_rect

    global chest_open_zoom
    global chest_open_zoom_rect

    chest_closed_zoom = 0
    chest_closed_zoom_rect = 0

    for each in range(300):
        chest_closed_zoom = pygame.transform.scale(img, (screen.get_width() * (each / 500), screen.get_height() * (each / 500)))
        chest_closed_zoom_rect = chest_closed_zoom.get_rect(center = (screen.get_width() * 0.5, screen.get_height() * 0.5))
        
        screen.blit(chest_closed_zoom, chest_closed_zoom_rect)
        pygame.display.update()
        pygame.time.delay(1)
    
    chest_ajar_zoom = pygame.transform.scale(chest_ajar_image, (chest_closed_zoom.get_width(), chest_closed_zoom.get_height()))
    chest_open_zoom = pygame.transform.scale(chest_open_image, (chest_closed_zoom.get_width(), chest_closed_zoom.get_height()))
    chest_ajar_zoom_rect = chest_ajar_zoom.get_rect(center = (screen.get_width() * 0.5, screen.get_height() * 0.5))
    chest_open_zoom_rect = chest_open_zoom.get_rect(center = (screen.get_width() * 0.5, screen.get_height() * 0.5))

    chest_animation_state = 'finished'

def chest_open():
    global chest_animation

    chest_animation += 0.02

def fade_in():
    global fade_in_animation

    fade = pygame.Surface((screen.get_width(), screen.get_height()))
    fade.fill((94,129,162))

    for alpha in range(0, 200):
        if alpha <= 100:
            fade.set_alpha(alpha)
            screen.blit(fade, (0,0))
            pygame.display.update()
            pygame.time.delay(10)
        else:
            fade.set_alpha(alpha)
            screen.blit(fade, (0,0))
            pygame.display.update()
            pygame.time.delay(1)
    
    fade_in_animation = 'finished'

def reward_jump(reward):
    global reward_img_rect
    global reward_animation
    reward_img_rect = 0

    for each in range(60, 0, -1):
        if each > 30:
            reward_img_rect = reward.get_rect(center = (screen.get_width() * 0.5, screen.get_height() * (each / 120)))

            screen.fill((94,129,162))
            screen.blit(chest_open_zoom, chest_open_zoom_rect)
            screen.blit(reward, reward_img_rect)
            pygame.display.update()
            pygame.time.delay(30)
        if each < 30:
            pass
    
    reward_animation = 'finished'

def words_selector(table):
    global words_and_paths

    conn = sqlite3.connect('words_database/words-database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM ' + table)
    words_and_paths = c.fetchall()
    conn.close()

def initialize_cariboo():
    flash_cards_init()
    images_and_rect_trans()
    chest_update()
    ball_update()
    set_flash_state()
    set_flash_animation_state()
    ball_animation_init()
    restart_cariboo()
    initiate_cariboo_state()
    initiate_cariboo_circles_text_board()
    cariboo_audio_init()

def cariboo_audio_init():
    global ball_drop_audio

    ball_drop_audio = pygame.mixer.Sound('audio/cariboo/ball_drop.wav')

# init the game
pygame.init()

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


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
# screen = pygame.display.set_mode((screen_width * 0.90, screen_height * 0.90), pygame.RESIZABLE)
pygame.display.set_caption('Speech Game')

# start clock
clock = pygame.time.Clock()

# set the game_state to decide a game
def initiate_cariboo_state():
    global game_phase
    global game_state
    global ball_list
    global balls_found_list
    global chest_animation_state
    global fade_in_animation


    game_state = 'cariboo_init'
    game_phase = 'ball'
    ball_list = []
    balls_found_list = []
    chest_animation_state = 'not_finished'
    fade_in_animation = 'not_finished'

# main board rect
def initiate_cariboo_circles_text_board():
    global main_board
    global blue_ball_area
    global circle_1_image
    global circle_1_image_transform
    global circle_2_image_transform
    global circle_3_image_transform
    global circle_1_rect
    global circle_2_rect
    global circle_3_rect

    global pixel_font_med
    global pixel_font_large

    global game_title
    global game_title_rect
    global up_text
    global up_text_rect
    global restart_text
    global win_text
    global restart_text_rect
    global win_text_rect
    global push_text
    global push_text_rect
    global step_text
    global step_text_rect

    main_board = pygame.Rect((screen.get_width() * 0.05, screen.get_height() * 0.05), (screen.get_width() * 0.78, screen.get_height() * 0.90))
    blue_ball_area = pygame.Rect((screen.get_width() * 0.80, screen.get_height() * 0.05), (screen.get_width() * 0.15, screen.get_height() * 0.90))

    # import circles and transform
    circle_1_image = pygame.image.load('graphics/ui/circle3.png').convert_alpha()
    circle_1_image_transform = pygame.transform.scale(circle_1_image, (screen.get_width() * 0.04, screen.get_height() * 0.07))
    circle_2_image_transform = pygame.transform.scale(circle_1_image, (screen.get_width() * 0.04, screen.get_height() * 0.07))
    circle_3_image_transform = pygame.transform.scale(circle_1_image, (screen.get_width() * 0.04, screen.get_height() * 0.07))

    # rects for circles
    circle_1_rect = circle_1_image_transform.get_rect(center = (screen.get_width() * 0.15, screen.get_height() * 0.12))
    circle_2_rect = circle_2_image_transform.get_rect(center = (screen.get_width() * 0.43, screen.get_height() * 0.12))
    circle_3_rect = circle_3_image_transform.get_rect(center = (screen.get_width() * 0.71, screen.get_height() * 0.12))

    # import font
    # cariboo_font = pygame.font.Font('fonts/cariboo/LuckiestGuy-Regular.ttf', int(screen.get_width() * 0.03))
    pixel_font_med = pygame.font.Font('fonts/pixel/Pixeltype.ttf', int(screen.get_width() * 0.03))
    game_title = pixel_font_med.render('Cariboo', True, (233,169,21))
    game_title_rect = game_title.get_rect(center = (screen.get_width() * 0.57, screen.get_height() * 0.13))
    up_text = pixel_font_med.render('Up', True, (185,136,235))
    up_text_rect = up_text.get_rect(center = (screen.get_width() * 0.32, screen.get_height() * 0.13))

    pixel_font_large = pygame.font.Font('fonts/pixel/Pixeltype.ttf', int(screen.get_width() * 0.05))
    restart_text = pixel_font_large.render('Push to Restart', False, (255,255,255))
    win_text = pixel_font_large.render('Congratulations! You Found All the Balls!', False, (255,255,255))
    restart_text_rect = restart_text.get_rect(center = (screen.get_width() * 0.50, screen.get_height() * 0.80))
    win_text_rect = win_text.get_rect(center = (screen.get_width() * 0.50, screen.get_height() * 0.20))
    push_text = pixel_font_large.render('Claim Your Reward!', False, (255,255,255))
    push_text_rect = push_text.get_rect(center = (screen.get_width() * 0.5, screen.get_height() * 0.30))

    step_text = pixel_font_med.render('Step', True, (117,198,184))
    step_text_rect = step_text.get_rect(center = (screen.get_width() * 0.27, screen.get_height() * 0.13))

# import card images for cariboo
def flash_cards_init():
    global one_1_image
    global one_2_image
    global one_3_image
    global one_4_image
    global one_5_image
    global two_1_image
    global two_2_image
    global two_3_image
    global two_4_image
    global two_5_image
    global three_1_image
    global three_2_image
    global three_3_image
    global three_4_image
    global three_5_image

    global cariboo_background_1
    global cariboo_background_2
    global cariboo_background_3


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

    second_size = 0.10
    third_size = 0.07
    fourth_size = 0.03

    # rectangles measurements for the first is screen.get_width() * 0.07, screen.get_height() * 0.21
    one_1_image_trans = [pygame.transform.scale(one_1_image, (screen.get_width() * 0.07, screen.get_width() * 0.07)), pygame.transform.scale(one_1_image, (screen.get_width() * 0.07, screen.get_height() * second_size)), pygame.transform.scale(one_1_image, (screen.get_width() * 0.07, screen.get_height() * third_size)), pygame.transform.scale(one_1_image, (screen.get_width() * 0.07, screen.get_height() * fourth_size)), pygame.transform.scale(one_1_image, (screen.get_width() * 0.07, screen.get_height() * 0.002))]
    one_2_image_trans = [pygame.transform.scale(one_2_image, (screen.get_width() * 0.07, screen.get_width() * 0.07)), pygame.transform.scale(one_2_image, (screen.get_width() * 0.07, screen.get_height() * second_size)), pygame.transform.scale(one_2_image, (screen.get_width() * 0.07, screen.get_height() * third_size)), pygame.transform.scale(one_2_image, (screen.get_width() * 0.07, screen.get_height() * fourth_size)), pygame.transform.scale(one_2_image, (screen.get_width() * 0.07, screen.get_height() * 0.002))]
    one_3_image_trans = [pygame.transform.scale(one_3_image, (screen.get_width() * 0.07, screen.get_width() * 0.07)), pygame.transform.scale(one_3_image, (screen.get_width() * 0.07, screen.get_height() * second_size)), pygame.transform.scale(one_3_image, (screen.get_width() * 0.07, screen.get_height() * third_size)), pygame.transform.scale(one_3_image, (screen.get_width() * 0.07, screen.get_height() * fourth_size)), pygame.transform.scale(one_3_image, (screen.get_width() * 0.07, screen.get_height() * 0.002))]
    one_4_image_trans = [pygame.transform.scale(one_4_image, (screen.get_width() * 0.07, screen.get_width() * 0.07)), pygame.transform.scale(one_4_image, (screen.get_width() * 0.07, screen.get_height() * second_size)), pygame.transform.scale(one_4_image, (screen.get_width() * 0.07, screen.get_height() * third_size)), pygame.transform.scale(one_4_image, (screen.get_width() * 0.07, screen.get_height() * fourth_size)), pygame.transform.scale(one_4_image, (screen.get_width() * 0.07, screen.get_height() * 0.002))]
    one_5_image_trans = [pygame.transform.scale(one_5_image, (screen.get_width() * 0.07, screen.get_width() * 0.07)), pygame.transform.scale(one_5_image, (screen.get_width() * 0.07, screen.get_height() * second_size)), pygame.transform.scale(one_5_image, (screen.get_width() * 0.07, screen.get_height() * third_size)), pygame.transform.scale(one_5_image, (screen.get_width() * 0.07, screen.get_height() * fourth_size)), pygame.transform.scale(one_5_image, (screen.get_width() * 0.07, screen.get_height() * 0.002))]
    two_1_image_trans = [pygame.transform.scale(two_1_image, (screen.get_width() * 0.07, screen.get_width() * 0.07)), pygame.transform.scale(two_1_image, (screen.get_width() * 0.07, screen.get_height() * second_size)), pygame.transform.scale(two_1_image, (screen.get_width() * 0.07, screen.get_height() * third_size)), pygame.transform.scale(two_1_image, (screen.get_width() * 0.07, screen.get_height() * fourth_size)), pygame.transform.scale(two_1_image, (screen.get_width() * 0.07, screen.get_height() * 0.002))]
    two_2_image_trans = [pygame.transform.scale(two_2_image, (screen.get_width() * 0.07, screen.get_width() * 0.07)), pygame.transform.scale(two_2_image, (screen.get_width() * 0.07, screen.get_height() * second_size)), pygame.transform.scale(two_2_image, (screen.get_width() * 0.07, screen.get_height() * third_size)), pygame.transform.scale(two_2_image, (screen.get_width() * 0.07, screen.get_height() * fourth_size)), pygame.transform.scale(two_2_image, (screen.get_width() * 0.07, screen.get_height() * 0.002))]
    two_3_image_trans = [pygame.transform.scale(two_3_image, (screen.get_width() * 0.07, screen.get_width() * 0.07)), pygame.transform.scale(two_3_image, (screen.get_width() * 0.07, screen.get_height() * second_size)), pygame.transform.scale(two_3_image, (screen.get_width() * 0.07, screen.get_height() * third_size)), pygame.transform.scale(two_3_image, (screen.get_width() * 0.07, screen.get_height() * fourth_size)), pygame.transform.scale(two_3_image, (screen.get_width() * 0.07, screen.get_height() * 0.002))]
    two_4_image_trans = [pygame.transform.scale(two_4_image, (screen.get_width() * 0.07, screen.get_width() * 0.07)), pygame.transform.scale(two_4_image, (screen.get_width() * 0.07, screen.get_height() * second_size)), pygame.transform.scale(two_4_image, (screen.get_width() * 0.07, screen.get_height() * third_size)), pygame.transform.scale(two_4_image, (screen.get_width() * 0.07, screen.get_height() * fourth_size)), pygame.transform.scale(two_4_image, (screen.get_width() * 0.07, screen.get_height() * 0.002))]
    two_5_image_trans = [pygame.transform.scale(two_5_image, (screen.get_width() * 0.07, screen.get_width() * 0.07)), pygame.transform.scale(two_5_image, (screen.get_width() * 0.07, screen.get_height() * second_size)), pygame.transform.scale(two_5_image, (screen.get_width() * 0.07, screen.get_height() * third_size)), pygame.transform.scale(two_5_image, (screen.get_width() * 0.07, screen.get_height() * fourth_size)), pygame.transform.scale(two_5_image, (screen.get_width() * 0.07, screen.get_height() * 0.002))]
    three_1_image_trans = [pygame.transform.scale(three_1_image, (screen.get_width() * 0.07, screen.get_width() * 0.07)), pygame.transform.scale(three_1_image, (screen.get_width() * 0.07, screen.get_height() * second_size)), pygame.transform.scale(three_1_image, (screen.get_width() * 0.07, screen.get_height() * third_size)), pygame.transform.scale(three_1_image, (screen.get_width() * 0.07, screen.get_height() * fourth_size)), pygame.transform.scale(three_1_image, (screen.get_width() * 0.07, screen.get_height() * 0.002))]
    three_2_image_trans = [pygame.transform.scale(three_2_image, (screen.get_width() * 0.07, screen.get_width() * 0.07)), pygame.transform.scale(three_2_image, (screen.get_width() * 0.07, screen.get_height() * second_size)), pygame.transform.scale(three_2_image, (screen.get_width() * 0.07, screen.get_height() * third_size)), pygame.transform.scale(three_2_image, (screen.get_width() * 0.07, screen.get_height() * fourth_size)), pygame.transform.scale(three_2_image, (screen.get_width() * 0.07, screen.get_height() * 0.002))]
    three_3_image_trans = [pygame.transform.scale(three_3_image, (screen.get_width() * 0.07, screen.get_width() * 0.07)), pygame.transform.scale(three_3_image, (screen.get_width() * 0.07, screen.get_height() * second_size)), pygame.transform.scale(three_3_image, (screen.get_width() * 0.07, screen.get_height() * third_size)), pygame.transform.scale(three_3_image, (screen.get_width() * 0.07, screen.get_height() * fourth_size)), pygame.transform.scale(three_3_image, (screen.get_width() * 0.07, screen.get_height() * 0.002))]
    three_4_image_trans = [pygame.transform.scale(three_4_image, (screen.get_width() * 0.07, screen.get_width() * 0.07)), pygame.transform.scale(three_4_image, (screen.get_width() * 0.07, screen.get_height() * second_size)), pygame.transform.scale(three_4_image, (screen.get_width() * 0.07, screen.get_height() * third_size)), pygame.transform.scale(three_4_image, (screen.get_width() * 0.07, screen.get_height() * fourth_size)), pygame.transform.scale(three_4_image, (screen.get_width() * 0.07, screen.get_height() * 0.002))]
    three_5_image_trans = [pygame.transform.scale(three_5_image, (screen.get_width() * 0.07, screen.get_width() * 0.07)), pygame.transform.scale(three_5_image, (screen.get_width() * 0.07, screen.get_height() * second_size)), pygame.transform.scale(three_5_image, (screen.get_width() * 0.07, screen.get_height() * third_size)), pygame.transform.scale(three_5_image, (screen.get_width() * 0.07, screen.get_height() * fourth_size)), pygame.transform.scale(three_5_image, (screen.get_width() * 0.07, screen.get_height() * 0.002))]

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
    global chest_ajar_image
    global chest_ajar_trans
    global chest_ajar_rect
    global chest_open_image
    global chest_open_trans
    global chest_open_rect

    global chest_image_finished
    global chest_image_finished_rect

    # original value for transform was screen.get_width() * 0.07, screen.get_height * 0.11
    chest_image = pygame.image.load('graphics/neutral/chest_closed.png').convert_alpha()
    chest_image_trans = pygame.transform.scale(chest_image, (screen.get_width() * 0.10, screen.get_height() * 0.15))
    chest_image_rect = chest_image_trans.get_rect(center = (screen.get_width() * 0.89, screen.get_height() * 0.12))

    chest_ajar_image = pygame.image.load('graphics/neutral/chest_ajar.png').convert_alpha()
    chest_ajar_trans = pygame.transform.scale(chest_ajar_image, (screen.get_width() * 0.10, screen.get_height() * 0.15))
    chest_ajar_rect = chest_ajar_trans.get_rect(center = (screen.get_width() * 0.89, screen.get_height() * 0.13))

    chest_open_image = pygame.image.load('graphics/neutral/chest_open.png').convert_alpha()
    chest_open_trans = pygame.transform.scale(chest_open_image, (screen.get_width() * 0.10, screen.get_height() * 0.15))
    chest_open_rect = chest_open_trans.get_rect(center = (screen.get_width() * 0.89, screen.get_height() * 0.13))

    chest_image_finished = pygame.transform.scale(chest_image, (screen.get_width() * 0.50, screen.get_height() * 0.53))
    chest_image_finished_rect = chest_image_finished.get_rect(center = (screen.get_width() * 0.50, screen.get_height() * 0.50))

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

    ball_1_list = [pygame.transform.scale(ball_1_image, (screen.get_width() * 0.04, screen.get_height() * 0.07)), pygame.transform.scale(ball_1_image, (screen.get_width() * 0.03, screen.get_height() * 0.06)), pygame.transform.scale(ball_1_image, (screen.get_width() * 0.015, screen.get_height() * 0.03))]
    ball_2_list = [pygame.transform.scale(ball_2_image, (screen.get_width() * 0.04, screen.get_height() * 0.07)), pygame.transform.scale(ball_2_image, (screen.get_width() * 0.03, screen.get_height() * 0.06)), pygame.transform.scale(ball_2_image, (screen.get_width() * 0.015, screen.get_height() * 0.03))]
    ball_3_list = [pygame.transform.scale(ball_3_image, (screen.get_width() * 0.04, screen.get_height() * 0.07)), pygame.transform.scale(ball_3_image, (screen.get_width() * 0.03, screen.get_height() * 0.06)), pygame.transform.scale(ball_3_image, (screen.get_width() * 0.015, screen.get_height() * 0.03))]
    ball_4_list = [pygame.transform.scale(ball_4_image, (screen.get_width() * 0.04, screen.get_height() * 0.07)), pygame.transform.scale(ball_4_image, (screen.get_width() * 0.03, screen.get_height() * 0.06)), pygame.transform.scale(ball_4_image, (screen.get_width() * 0.015, screen.get_height() * 0.03))]

    ball_1_trans = pygame.transform.scale(ball_1_image, (screen.get_width() * 0.05, screen.get_height() * 0.07))
    ball_2_trans = pygame.transform.scale(ball_2_image, (screen.get_width() * 0.05, screen.get_height() * 0.07))
    ball_3_trans = pygame.transform.scale(ball_3_image, (screen.get_width() * 0.05, screen.get_height() * 0.07))
    ball_4_trans = pygame.transform.scale(ball_4_image, (screen.get_width() * 0.05, screen.get_height() * 0.07))

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

def button_images():
    global blue_button
    global a_button_rect
    global b_button_rect
    global c_button_rect
    global d_button_rect
    global e_button_rect
    global f_button_rect
    global g_button_rect
    global h_button_rect
    global i_button_rect
    global j_button_rect

    global letter_selection
    global letter_selection_rect

    global a_letter
    global b_letter
    global c_letter
    global d_letter
    global e_letter
    global f_letter
    global g_letter
    global h_letter
    global i_letter
    global j_letter

    global reward_selection
    global reward_selection_rect
    global blue_button_rewards
    global trophy_button_rect
    global coin_button_rect
    global candy_button_rect
    global trophy_text
    global coin_text
    global candy_text

    blue_button = pygame.image.load('graphics/buttons/blue_button.png').convert_alpha()
    blue_button = pygame.transform.scale(blue_button, (screen.get_width() * 0.10, screen.get_height() * 0.10))
    blue_button_rewards = pygame.transform.scale(blue_button, (screen.get_width() * 0.20, screen.get_height() * 0.20))

    # this section is for letter selection
    button_height_position = 0.13

    a_button_rect = blue_button.get_rect(center = (screen.get_width() * 0.07, screen.get_height() * button_height_position))
    b_button_rect = blue_button.get_rect(center = (screen.get_width() * 0.21, screen.get_height() * button_height_position))
    c_button_rect = blue_button.get_rect(center = (screen.get_width() * 0.35, screen.get_height() * button_height_position))
    d_button_rect = blue_button.get_rect(center = (screen.get_width() * 0.49, screen.get_height() * button_height_position))
    e_button_rect = blue_button.get_rect(center = (screen.get_width() * 0.63, screen.get_height() * button_height_position))
    f_button_rect = blue_button.get_rect(center = (screen.get_width() * 0.77, screen.get_height() * button_height_position))
    g_button_rect = blue_button.get_rect(center = (screen.get_width() * 0.91, screen.get_height() * button_height_position))
    h_button_rect = blue_button.get_rect(center = (screen.get_width() * 0.07, screen.get_height() * (button_height_position + 0.15)))
    i_button_rect = blue_button.get_rect(center = (screen.get_width() * 0.21, screen.get_height() * (button_height_position + 0.15)))
    j_button_rect = blue_button.get_rect(center = (screen.get_width() * 0.35, screen.get_height() * (button_height_position + 0.15)))

    letter_selection = pixel_font_large.render('SELECT A LETTER', False, 'White')
    letter_selection_rect = letter_selection.get_rect(center = (screen.get_width() * 0.5, screen.get_height() * 0.04))
    a_letter = pixel_font_large.render('A', False, 'White')
    b_letter = pixel_font_large.render('B', False, 'White')
    c_letter = pixel_font_large.render('C', False, 'White')
    d_letter = pixel_font_large.render('D', False, 'White')
    e_letter = pixel_font_large.render('E', False, 'White')
    f_letter = pixel_font_large.render('F', False, 'White')
    g_letter = pixel_font_large.render('G', False, 'White')
    h_letter = pixel_font_large.render('H', False, 'White')
    i_letter = pixel_font_large.render('I', False, 'White')
    j_letter = pixel_font_large.render('J', False, 'White')

    ## this section is for reward selection
    reward_selection = pixel_font_large.render('SELECT A REWARD', False, 'White')
    reward_selection_rect = reward_selection.get_rect(center = (screen.get_width() * 0.5, screen.get_height() * 0.04))

    trophy_button_rect = blue_button_rewards.get_rect(center = (screen.get_width() * 0.5, screen.get_height() * 0.2))
    coin_button_rect = blue_button_rewards.get_rect(center = (screen.get_width() * 0.5, screen.get_height() * 0.4))
    candy_button_rect = blue_button_rewards.get_rect(center = (screen.get_width() * 0.5, screen.get_height() * 0.6))

    trophy_text = pixel_font_large.render('TROPHY', False, 'White')
    coin_text = pixel_font_large.render('COIN', False, 'White')
    candy_text = pixel_font_large.render('CANDY', False, 'White')

def reward_image(img):
    global reward_img
    reward_img = pygame.image.load(img).convert_alpha()
    reward_img = pygame.transform.scale(reward_img, (screen.get_width() * 0.20, screen.get_height() * 0.20))

# rects for card images

initiate_cariboo_circles_text_board()
button_images()
initiate_menu_buttons()
initiate_cariboo_state()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        # if event.type == pygame.VIDEORESIZE:
        #     screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        #     main_board = pygame.Rect((screen.get_width() * 0.05, screen.get_height() * 0.05), (screen.get_width() * 0.90, screen.get_height() * 0.90))
        #     blue_ball_area = pygame.Rect((screen.get_width() * 0.80, screen.get_height() * 0.05), (screen.get_width() * 0.15, screen.get_height() * 0.90))
        #     # resize circles
        #     circle_1_image_transform = pygame.transform.scale(circle_1_image, (screen.get_width() * 0.04, screen.get_height() * 0.08))
        #     circle_2_image_transform = pygame.transform.scale(circle_1_image, (screen.get_width() * 0.04, screen.get_height() * 0.08))
        #     circle_3_image_transform = pygame.transform.scale(circle_1_image, (screen.get_width() * 0.04, screen.get_height() * 0.08))

        #     # re-position rects
        #     circle_1_rect = circle_1_image_transform.get_rect(center = (screen.get_width() * 0.15, screen.get_height() * 0.12))
        #     circle_2_rect = circle_2_image_transform.get_rect(center = (screen.get_width() * 0.43, screen.get_height() * 0.12))
        #     circle_3_rect = circle_3_image_transform.get_rect(center = (screen.get_width() * 0.71, screen.get_height() * 0.12))

        #     # resize title text
        #     cariboo_font = pygame.font.Font('fonts/cariboo/LuckiestGuy-Regular.ttf', int(screen.get_width() * 0.03))
        #     game_title = cariboo_font.render('Cariboo', True, (233,169,21))
        #     game_title_rect = game_title.get_rect(center = (screen.get_width() * 0.57, screen.get_height() * 0.13))

        #     up_text = cariboo_font.render('Up', True, (185,136,235))
        #     up_text_rect = up_text.get_rect(center = (screen.get_width() * 0.32, screen.get_height() * 0.13))

        #     step_text = cariboo_font.render('Step', True, (117,198,184))
        #     step_text_rect = step_text.get_rect(center = (screen.get_width() * 0.27, screen.get_height() * 0.13))

        #     # resize all flash cards
        #     images_and_rect_trans()
        #     chest_update()
        #     ball_update()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Collider for inserting balls to the top circles
            if game_state == 'cariboo':
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
            if game_state == 'cariboo_finished':
                if restart_button_rect.collidepoint(event.pos) and chest_animation >= 2:
                    print('game restarting')
                    restart_cariboo(True)
                if chest_animation_state == 'finished':
                    if chest_closed_zoom_rect.collidepoint(event.pos) and chest_animation == 0:
                        chest_open()

            if game_state == 'cariboo_init':
                if a_button_rect.collidepoint(event.pos):
                    words_selector('a_initial')
                    initialize_cariboo()
                    game_state = 'cariboo_reward'

                if b_button_rect.collidepoint(event.pos):
                    words_selector('b_initial')
                    initialize_cariboo()
                    game_state = 'cariboo_reward'

                if c_button_rect.collidepoint(event.pos):
                    words_selector('c_initial')
                    initialize_cariboo()
                    game_state = 'cariboo_reward'

                if d_button_rect.collidepoint(event.pos):
                    words_selector('d_initial')
                    initialize_cariboo()
                    game_state = 'cariboo_reward'

                if e_button_rect.collidepoint(event.pos):
                    words_selector('e_initial')
                    initialize_cariboo()
                    game_state = 'cariboo_reward'

                if f_button_rect.collidepoint(event.pos):
                    words_selector('f_initial')
                    initialize_cariboo()
                    game_state = 'cariboo_reward'

                if g_button_rect.collidepoint(event.pos):
                    words_selector('g_initial')
                    initialize_cariboo()
                    game_state = 'cariboo_reward'

                if h_button_rect.collidepoint(event.pos):
                    words_selector('h_initial')
                    initialize_cariboo()
                    game_state = 'cariboo_reward'
                if i_button_rect.collidepoint(event.pos):
                    words_selector('i_initial')
                    initialize_cariboo()
                    game_state = 'cariboo_reward'
                
                if j_button_rect.collidepoint(event.pos):
                    words_selector('j_initial')
                    initialize_cariboo()
                    game_state = 'cariboo_reward'
            
            elif game_state == 'cariboo_reward':
                if trophy_button_rect.collidepoint(event.pos):
                    reward_image('graphics/rewards/trophy.png')
                    game_state = 'cariboo'
                if coin_button_rect.collidepoint(event.pos):
                    reward_image('graphics/rewards/coin.png')
                    game_state = 'cariboo'
                if candy_button_rect.collidepoint(event.pos):
                    reward_image('graphics/rewards/candy.png')
                    game_state = 'cariboo'

            if game_state != 'main_menu':
                if close_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    exit()

                if back_button_rect.collidepoint(event.pos):
                    game_state = 'cariboo_init'

    if game_state == 'cariboo_init':
        screen.fill((94,129,162))
        screen.blit(letter_selection, letter_selection_rect)
        screen.blit(blue_button, a_button_rect)
        screen.blit(a_letter, (screen.get_width() * 0.06, screen.get_height() * 0.1))
        screen.blit(blue_button, b_button_rect)
        screen.blit(b_letter, (screen.get_width() * 0.20, screen.get_height() * 0.1))
        screen.blit(blue_button, c_button_rect)
        screen.blit(c_letter, (screen.get_width() * 0.34, screen.get_height() * 0.1))
        screen.blit(blue_button, d_button_rect)
        screen.blit(d_letter, (screen.get_width() * 0.48, screen.get_height() * 0.1))
        screen.blit(blue_button, e_button_rect)
        screen.blit(e_letter, (screen.get_width() * 0.62, screen.get_height() * 0.1))
        screen.blit(blue_button, f_button_rect)
        screen.blit(f_letter, (screen.get_width() * 0.76, screen.get_height() * 0.1))
        screen.blit(blue_button, g_button_rect)
        screen.blit(g_letter, (screen.get_width() * 0.90, screen.get_height() * 0.1))
        screen.blit(blue_button, h_button_rect)
        screen.blit(h_letter, (screen.get_width() * 0.06, screen.get_height() * 0.255))
        screen.blit(blue_button, i_button_rect)
        screen.blit(i_letter, (screen.get_width() * 0.205, screen.get_height() * 0.255))
        screen.blit(blue_button, j_button_rect)
        screen.blit(j_letter, (screen.get_width() * 0.34, screen.get_height() * 0.255))

    if game_state == 'cariboo_reward':
        screen.fill((94,129,162))
        screen.blit(reward_selection, reward_selection_rect)
        screen.blit(blue_button_rewards, trophy_button_rect)
        screen.blit(trophy_text, (screen.get_width() * 0.445, screen.get_height() * 0.17))
        screen.blit(blue_button_rewards, coin_button_rect)
        screen.blit(coin_text, (screen.get_width() * 0.465, screen.get_height() * 0.37))
        screen.blit(blue_button_rewards, candy_button_rect)
        screen.blit(candy_text, (screen.get_width() * 0.455, screen.get_height() * 0.57))


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
        pygame.draw.rect(screen, (38, 121, 163), blue_ball_area, 0, 20)
        pygame.draw.rect(screen, 'Yellow', main_board, 0, 20)

        # draw black rects behind flash cards. This is purely for asthetic reasons
        # first row of black rects
        pygame.draw.rect(screen, 'Black', (one_1_rect.left - screen.get_width() * 0.0007, one_1_rect.top - screen.get_height() * 0.0011, screen.get_width() * 0.072, screen.get_width() * 0.072))
        pygame.draw.rect(screen, 'Black', (one_2_rect.left - screen.get_width() * 0.0007, one_2_rect.top - screen.get_height() * 0.0011, screen.get_width() * 0.072, screen.get_width() * 0.072))
        pygame.draw.rect(screen, 'Black', (one_3_rect.left - screen.get_width() * 0.0007, one_3_rect.top - screen.get_height() * 0.0011, screen.get_width() * 0.072, screen.get_width() * 0.072))
        pygame.draw.rect(screen, 'Black', (one_4_rect.left - screen.get_width() * 0.0007, one_4_rect.top - screen.get_height() * 0.0011, screen.get_width() * 0.072, screen.get_width() * 0.072))
        pygame.draw.rect(screen, 'Black', (one_5_rect.left - screen.get_width() * 0.0007, one_5_rect.top - screen.get_height() * 0.0011, screen.get_width() * 0.072, screen.get_width() * 0.072))
        # second row of black rects
        pygame.draw.rect(screen, 'Black', (two_1_rect.left - screen.get_width() * 0.0007, two_1_rect.top - screen.get_height() * 0.0011, screen.get_width() * 0.072, screen.get_width() * 0.072))
        pygame.draw.rect(screen, 'Black', (two_2_rect.left - screen.get_width() * 0.0007, two_2_rect.top - screen.get_height() * 0.0011, screen.get_width() * 0.072, screen.get_width() * 0.072))
        pygame.draw.rect(screen, 'Black', (two_3_rect.left - screen.get_width() * 0.0007, two_3_rect.top - screen.get_height() * 0.0011, screen.get_width() * 0.072, screen.get_width() * 0.072))
        pygame.draw.rect(screen, 'Black', (two_4_rect.left - screen.get_width() * 0.0007, two_4_rect.top - screen.get_height() * 0.0011, screen.get_width() * 0.072, screen.get_width() * 0.072))
        pygame.draw.rect(screen, 'Black', (two_5_rect.left - screen.get_width() * 0.0007, two_5_rect.top - screen.get_height() * 0.0011, screen.get_width() * 0.072, screen.get_width() * 0.072))
        # third row of black rects
        pygame.draw.rect(screen, 'Black', (three_1_rect.left - screen.get_width() * 0.0007, three_1_rect.top - screen.get_height() * 0.0011, screen.get_width() * 0.072, screen.get_width() * 0.072))
        pygame.draw.rect(screen, 'Black', (three_2_rect.left - screen.get_width() * 0.0007, three_2_rect.top - screen.get_height() * 0.0011, screen.get_width() * 0.072, screen.get_width() * 0.072))
        pygame.draw.rect(screen, 'Black', (three_3_rect.left - screen.get_width() * 0.0007, three_3_rect.top - screen.get_height() * 0.0011, screen.get_width() * 0.072, screen.get_width() * 0.072))
        pygame.draw.rect(screen, 'Black', (three_4_rect.left - screen.get_width() * 0.0007, three_4_rect.top - screen.get_height() * 0.0011, screen.get_width() * 0.072, screen.get_width() * 0.072))
        pygame.draw.rect(screen, 'Black', (three_5_rect.left - screen.get_width() * 0.0007, three_5_rect.top - screen.get_height() * 0.0011, screen.get_width() * 0.072, screen.get_width() * 0.072))
        
        
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
            # if chest_animation <= 1:
            #     chest_animation += 0.02
            #     screen.blit(chest_ajar_trans, chest_ajar_rect)
            # if chest_animation > 1:
            #     screen.blit(chest_open_trans, chest_open_rect)
            screen.blit(chest_image_trans, chest_image_rect)
            game_state = 'cariboo_finished'

        # animate the balls going into the holes
        try:   
            if ball_1_animation < 1:
                screen.blit(ball_1_list[0], ball_1_rect_list[0])
                if ball_1_animation == 0:
                    ball_drop_audio.play()
                ball_1_animation += 0.03
            elif ball_1_animation < 2:
                screen.blit(ball_1_list[1], ball_1_rect_list[1])
                if round(ball_1_animation, 2) == 1.02:
                    ball_drop_audio.play()
                ball_1_animation += 0.03
            elif ball_1_animation < 3:
                screen.blit(ball_1_list[2], ball_1_rect_list[2])
                if round(ball_1_animation, 2) == 2.01:
                    ball_drop_audio.play()
                ball_1_animation += 0.03
            elif ball_1_animation < 4:
                if round(ball_1_animation, 2) == 3.03:
                    ball_drop_audio.play()
                    ball_1_animation += 0.03
                pass
        except: pass
        try:
            if ball_2_animation < 1:
                screen.blit(ball_2_list[0], ball_2_rect_list[0])
                if ball_2_animation == 0:
                    ball_drop_audio.play()
                ball_2_animation += 0.03
            elif ball_2_animation < 2:
                screen.blit(ball_2_list[1], ball_2_rect_list[1])
                if round(ball_2_animation, 2) == 1.02:
                    ball_drop_audio.play()
                ball_2_animation += 0.03
            elif ball_2_animation < 3:
                screen.blit(ball_2_list[2], ball_2_rect_list[2])
                if round(ball_2_animation, 2) == 2.01:
                    ball_drop_audio.play()
                ball_2_animation += 0.03
            elif ball_2_animation < 4:
                if round(ball_2_animation, 2) == 3.03:
                    ball_drop_audio.play()
                    ball_2_animation += 0.03
                pass            
        except: pass
        try:
            if ball_3_animation < 1:
                screen.blit(ball_3_list[0], ball_3_rect_list[0])
                if ball_3_animation == 0:
                    ball_drop_audio.play()
                ball_3_animation += 0.03
            elif ball_3_animation < 2:
                screen.blit(ball_3_list[1], ball_3_rect_list[1])
                if round(ball_3_animation, 2) == 1.02:
                    ball_drop_audio.play()
                ball_3_animation += 0.03
            elif ball_3_animation < 3:
                screen.blit(ball_3_list[2], ball_3_rect_list[2])
                if round(ball_3_animation, 2) == 2.01:
                    ball_drop_audio.play()
                ball_3_animation += 0.03
            elif ball_3_animation < 4:
                if round(ball_3_animation, 2) == 3.03:
                    ball_drop_audio.play()
                    ball_3_animation += 0.03
                pass     
        except: pass

        try:
            if ball_4_animation < 1:
                screen.blit(ball_4_list[0], ball_4_rect_list[0])
                if ball_4_animation == 0:
                    ball_drop_audio.play()
                ball_4_animation += 0.03
            elif ball_4_animation < 2:
                screen.blit(ball_4_list[1], ball_4_rect_list[1])
                if round(ball_4_animation, 2) == 1.02:
                    ball_drop_audio.play()
                ball_4_animation += 0.03
            elif ball_4_animation < 3:
                screen.blit(ball_4_list[2], ball_4_rect_list[2])
                if round(ball_4_animation, 2) == 2.01:
                    ball_drop_audio.play()
                ball_4_animation += 0.03
            elif ball_4_animation < 4:
                if round(ball_4_animation, 2) == 3.03:
                    ball_drop_audio.play()
                    ball_4_animation += 0.03
                pass     
        except: pass

    if game_state == 'cariboo_finished':
        # screen.blit(restart_button_image, restart_button_rect)
        # screen.blit(restart_text, restart_text_rect)
        # screen.blit(game_text, game_text_rect)
        
        ## blue screen fade in
        if fade_in_animation != 'finished':
            fade_in()

        # screen.blit(win_text, win_text_rect)

        ## do the chest animation

        if chest_animation_state != 'finished':
            image_zoom(chest_image_finished, chest_image_finished_rect)
        if chest_animation_state == 'finished':
            if chest_animation == 0:
                screen.blit(chest_closed_zoom, chest_closed_zoom_rect)
                screen.blit(win_text, win_text_rect)
                screen.blit(push_text, push_text_rect)
            elif chest_animation < 1:
                chest_animation += 0.02
                screen.blit(chest_closed_zoom, chest_closed_zoom_rect)
            elif chest_animation < 2:
                chest_animation += 0.02
                screen.blit(chest_ajar_zoom, chest_ajar_zoom_rect)
            elif chest_animation < 3:
                screen.blit(chest_open_zoom, chest_open_zoom_rect)
                if reward_animation == 'not_finished':
                    reward_jump(reward_img)
                else:
                    screen.blit(reward_img, reward_img_rect)
                # screen.blit(reward_img, (screen.get_width() * 0.4, screen.get_height() * 0.4))
                screen.blit(restart_text, restart_text_rect)

    if game_state != 'main_menu':
        screen.blit(back_button, back_button_rect)
        screen.blit(close_button, close_button_rect)

    # update the game
    pygame.display.update()
    # set fps to 60
    clock.tick(60)
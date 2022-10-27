import pygame
from gamestate import game_state, set_game_state
import sqlite3
import tkinter as tk
from random import randint
from sys import exit

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

flash_game_state = 'flash_init'

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

back_button = pygame.image.load('graphics/buttons/backward_btn.png')
close_button = pygame.image.load('graphics/buttons/close_btn.png')

back_button = pygame.transform.scale(back_button, (screen.get_width() * 0.03, screen.get_height() * 0.06))
close_button = pygame.transform.scale(close_button, (screen.get_width() * 0.03, screen.get_height() * 0.06))

back_button_rect = back_button.get_rect(topleft = (screen.get_width() * 0.01, screen.get_height() * 0.01))
close_button_rect = close_button.get_rect(topright = (screen.get_width() - (screen.get_width() * 0.01) , screen.get_height() * 0.01))

random_picture_selector = randint(0, 14)
random_selector_prev = random_picture_selector

def words_selector(table):
    global flash_words_and_paths

    conn = sqlite3.connect('words_database/words-database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM ' + table)
    flash_words_and_paths = c.fetchall()
    conn.close()

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
    global k_button_rect
    global l_button_rect
    global m_button_rect
    global n_button_rect
    global o_button_rect
    global p_button_rect
    global q_button_rect
    global r_button_rect
    global s_button_rect
    global t_button_rect
    global u_button_rect
    global v_button_rect
    global w_button_rect
    global x_button_rect
    global y_button_rect
    global z_button_rect

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
    global k_letter
    global l_letter
    global m_letter
    global n_letter
    global o_letter
    global p_letter
    global q_letter
    global r_letter
    global s_letter
    global t_letter
    global u_letter
    global v_letter
    global w_letter
    global x_letter
    global y_letter
    global z_letter

    global pixel_font_large

    blue_button = pygame.image.load('graphics/buttons/blue_button.png').convert_alpha()
    blue_button = pygame.transform.scale(blue_button, (screen.get_width() * 0.10, screen.get_height() * 0.10))
    pixel_font_large = pygame.font.Font('fonts/pixel/Pixeltype.ttf', int(screen.get_width() * 0.05))

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
    k_button_rect = blue_button.get_rect(center = (screen.get_width() * 0.49, screen.get_height() * (button_height_position + 0.15)))
    l_button_rect = blue_button.get_rect(center = (screen.get_width() * 0.63, screen.get_height() * (button_height_position + 0.15)))
    m_button_rect = blue_button.get_rect(center = (screen.get_width() * 0.77, screen.get_height() * (button_height_position + 0.15)))
    n_button_rect = blue_button.get_rect(center = (screen.get_width() * 0.91, screen.get_height() * (button_height_position + 0.15)))
    o_button_rect = blue_button.get_rect(center = (screen.get_width() * 0.07, screen.get_height() * (button_height_position + 0.30)))
    p_button_rect = blue_button.get_rect(center = (screen.get_width() * 0.21, screen.get_height() * (button_height_position + 0.30)))
    q_button_rect = blue_button.get_rect(center = (screen.get_width() * 0.35, screen.get_height() * (button_height_position + 0.30)))
    r_button_rect = blue_button.get_rect(center = (screen.get_width() * 0.49, screen.get_height() * (button_height_position + 0.30)))
    s_button_rect = blue_button.get_rect(center = (screen.get_width() * 0.63, screen.get_height() * (button_height_position + 0.30)))
    t_button_rect = blue_button.get_rect(center = (screen.get_width() * 0.77, screen.get_height() * (button_height_position + 0.30)))
    u_button_rect = blue_button.get_rect(center = (screen.get_width() * 0.91, screen.get_height() * (button_height_position + 0.30)))
    v_button_rect = blue_button.get_rect(center = (screen.get_width() * 0.21, screen.get_height() * (button_height_position + 0.45)))
    w_button_rect = blue_button.get_rect(center = (screen.get_width() * 0.35, screen.get_height() * (button_height_position + 0.45)))
    x_button_rect = blue_button.get_rect(center = (screen.get_width() * 0.49, screen.get_height() * (button_height_position + 0.45)))
    y_button_rect = blue_button.get_rect(center = (screen.get_width() * 0.63, screen.get_height() * (button_height_position + 0.45)))
    z_button_rect = blue_button.get_rect(center = (screen.get_width() * 0.77, screen.get_height() * (button_height_position + 0.45)))

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
    k_letter = pixel_font_large.render('K', False, 'White')
    l_letter = pixel_font_large.render('L', False, 'White')
    m_letter = pixel_font_large.render('M', False, 'White')
    n_letter = pixel_font_large.render('N', False, 'White')
    o_letter = pixel_font_large.render('O', False, 'White')
    p_letter = pixel_font_large.render('P', False, 'White')
    q_letter = pixel_font_large.render('Q', False, 'White')
    r_letter = pixel_font_large.render('R', False, 'White')
    s_letter = pixel_font_large.render('S', False, 'White')
    t_letter = pixel_font_large.render('T', False, 'White')
    u_letter = pixel_font_large.render('U', False, 'White')
    v_letter = pixel_font_large.render('V', False, 'White')
    w_letter = pixel_font_large.render('W', False, 'White')
    x_letter = pixel_font_large.render('X', False, 'White')
    y_letter = pixel_font_large.render('Y', False, 'White')
    z_letter = pixel_font_large.render('Z', False, 'White')

def flash_cards_init():
    global flash_words_and_paths

    # load all images
    one_1_image = pygame.image.load(flash_words_and_paths[0][1]).convert_alpha()
    one_2_image = pygame.image.load(flash_words_and_paths[1][1]).convert_alpha()
    one_3_image = pygame.image.load(flash_words_and_paths[2][1]).convert_alpha()
    one_4_image = pygame.image.load(flash_words_and_paths[3][1]).convert_alpha()
    one_5_image = pygame.image.load(flash_words_and_paths[4][1]).convert_alpha()
    two_1_image = pygame.image.load(flash_words_and_paths[5][1]).convert_alpha()
    two_2_image = pygame.image.load(flash_words_and_paths[6][1]).convert_alpha()
    two_3_image = pygame.image.load(flash_words_and_paths[7][1]).convert_alpha()
    two_4_image = pygame.image.load(flash_words_and_paths[8][1]).convert_alpha()
    two_5_image = pygame.image.load(flash_words_and_paths[9][1]).convert_alpha()
    three_1_image = pygame.image.load(flash_words_and_paths[10][1]).convert_alpha()
    three_2_image = pygame.image.load(flash_words_and_paths[11][1]).convert_alpha()
    three_3_image = pygame.image.load(flash_words_and_paths[12][1]).convert_alpha()
    three_4_image = pygame.image.load(flash_words_and_paths[13][1]).convert_alpha()
    three_5_image = pygame.image.load(flash_words_and_paths[14][1]).convert_alpha()

    one_1_image = pygame.transform.scale(one_1_image, (screen.get_width() * 0.20, screen.get_height() * 0.40))
    one_2_image = pygame.transform.scale(one_2_image, (screen.get_width() * 0.20, screen.get_height() * 0.40))
    one_3_image = pygame.transform.scale(one_3_image, (screen.get_width() * 0.20, screen.get_height() * 0.40))
    one_4_image = pygame.transform.scale(one_4_image, (screen.get_width() * 0.20, screen.get_height() * 0.40))
    one_5_image = pygame.transform.scale(one_5_image, (screen.get_width() * 0.20, screen.get_height() * 0.40))
    two_1_image = pygame.transform.scale(two_1_image, (screen.get_width() * 0.20, screen.get_height() * 0.40))
    two_2_image = pygame.transform.scale(two_2_image, (screen.get_width() * 0.20, screen.get_height() * 0.40))
    two_3_image = pygame.transform.scale(two_3_image, (screen.get_width() * 0.20, screen.get_height() * 0.40))
    two_4_image = pygame.transform.scale(two_4_image, (screen.get_width() * 0.20, screen.get_height() * 0.40))
    two_5_image = pygame.transform.scale(two_5_image, (screen.get_width() * 0.20, screen.get_height() * 0.40))
    three_1_image = pygame.transform.scale(three_1_image, (screen.get_width() * 0.20, screen.get_height() * 0.40))
    three_2_image = pygame.transform.scale(three_2_image, (screen.get_width() * 0.20, screen.get_height() * 0.40))
    three_3_image = pygame.transform.scale(three_3_image, (screen.get_width() * 0.20, screen.get_height() * 0.40))
    three_4_image = pygame.transform.scale(three_4_image, (screen.get_width() * 0.20, screen.get_height() * 0.40))
    three_5_image = pygame.transform.scale(three_5_image, (screen.get_width() * 0.20, screen.get_height() * 0.40))
    return [
        one_1_image, 
        one_2_image, 
        one_3_image,
        one_4_image,
        one_5_image,
        two_1_image,
        two_2_image,
        two_3_image,
        two_4_image,
        two_5_image,
        three_1_image,
        three_2_image,
        three_3_image,
        three_4_image,
        three_5_image,
        one_1_image.get_rect(center = (screen.get_width() * 0.5, screen.get_height() * 0.5))
        ]

flash_cards_list = []

def flash_cards_game():
    global flash_game_state
    global random_picture_selector
    global random_selector_prev
    global flash_cards_list

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if flash_game_state == 'flash_cards':
                if flash_cards_list[15].collidepoint(event.pos):
                    random_picture_selector = randint(0,14)
                    if random_picture_selector == random_selector_prev:
                        if random_selector_prev == 14:
                            random_picture_selector = random_selector_prev - 1
                        else:
                            random_picture_selector = random_selector_prev + 1
            if flash_game_state == 'flash_init':
                if a_button_rect.collidepoint(event.pos):
                    words_selector('a_initial')
                    flash_cards_list = flash_cards_init()
                    flash_game_state = 'flash_cards'

                if b_button_rect.collidepoint(event.pos):
                    words_selector('b_initial')
                    flash_cards_list = flash_cards_init()
                    flash_game_state = 'flash_cards'

                if c_button_rect.collidepoint(event.pos):
                    words_selector('c_initial')
                    flash_cards_list = flash_cards_init()
                    flash_game_state = 'flash_cards'

                if d_button_rect.collidepoint(event.pos):
                    words_selector('d_initial')
                    flash_cards_list = flash_cards_init()
                    flash_game_state = 'flash_cards'

                if e_button_rect.collidepoint(event.pos):
                    words_selector('e_initial')
                    flash_cards_list = flash_cards_init()
                    flash_game_state = 'flash_cards'

                if f_button_rect.collidepoint(event.pos):
                    words_selector('f_initial')
                    flash_cards_list = flash_cards_init()
                    flash_game_state = 'flash_cards'

                if g_button_rect.collidepoint(event.pos):
                    words_selector('g_initial')
                    flash_cards_list = flash_cards_init()
                    flash_game_state = 'flash_cards'

                if h_button_rect.collidepoint(event.pos):
                    words_selector('h_initial')
                    flash_cards_list = flash_cards_init()
                    flash_game_state = 'flash_cards'

                if i_button_rect.collidepoint(event.pos):
                    words_selector('i_initial')
                    flash_cards_list = flash_cards_init()
                    flash_game_state = 'flash_cards'
                
                if j_button_rect.collidepoint(event.pos):
                    words_selector('j_initial')
                    flash_cards_list = flash_cards_init()
                    flash_game_state = 'flash_cards'
                
                if k_button_rect.collidepoint(event.pos):
                    words_selector('k_initial')
                    flash_cards_list = flash_cards_init()
                    flash_game_state = 'flash_cards'

                if l_button_rect.collidepoint(event.pos):
                    words_selector('l_initial')
                    flash_cards_list = flash_cards_init()
                    flash_game_state = 'flash_cards'

                if m_button_rect.collidepoint(event.pos):
                    words_selector('m_initial')
                    flash_cards_list = flash_cards_init()
                    flash_game_state = 'flash_cards'

                if n_button_rect.collidepoint(event.pos):
                    words_selector('n_initial')
                    flash_cards_list = flash_cards_init()
                    flash_game_state = 'flash_cards'
                
                if o_button_rect.collidepoint(event.pos):
                    words_selector('o_initial')
                    flash_cards_list = flash_cards_init()
                    flash_game_state = 'flash_cards'

                if p_button_rect.collidepoint(event.pos):
                    words_selector('p_initial')
                    flash_cards_list = flash_cards_init()
                    flash_game_state = 'flash_cards'

                if q_button_rect.collidepoint(event.pos):
                    words_selector('q_initial')
                    flash_cards_list = flash_cards_init()
                    flash_game_state = 'flash_cards'

                if r_button_rect.collidepoint(event.pos):
                    words_selector('r_initial')
                    flash_cards_list = flash_cards_init()
                    flash_game_state = 'flash_cards'

                if s_button_rect.collidepoint(event.pos):
                    words_selector('s_initial')
                    flash_cards_list = flash_cards_init()
                    flash_game_state = 'flash_cards'

                if t_button_rect.collidepoint(event.pos):
                    words_selector('t_initial')
                    flash_cards_list = flash_cards_init()
                    flash_game_state = 'flash_cards'                  

                if u_button_rect.collidepoint(event.pos):
                    words_selector('u_initial')
                    flash_cards_list = flash_cards_init()
                    flash_game_state = 'flash_cards'

                if v_button_rect.collidepoint(event.pos):
                    words_selector('v_initial')
                    flash_cards_list = flash_cards_init()
                    flash_game_state = 'flash_cards'

                if w_button_rect.collidepoint(event.pos):
                    words_selector('w_initial')
                    flash_cards_list = flash_cards_init()
                    flash_game_state = 'flash_cards'

                if x_button_rect.collidepoint(event.pos):
                    words_selector('x_initial')
                    flash_cards_list = flash_cards_init()
                    flash_game_state = 'flash_cards'

                if y_button_rect.collidepoint(event.pos):
                    words_selector('y_initial')
                    flash_cards_list = flash_cards_init()
                    flash_game_state = 'flash_cards'

                if z_button_rect.collidepoint(event.pos):
                    words_selector('z_initial')
                    flash_cards_list = flash_cards_init()
                    flash_game_state = 'flash_cards'
            
            if close_button_rect.collidepoint(event.pos):
                pygame.quit()
                exit()
            
            if back_button_rect.collidepoint(event.pos) and flash_game_state == 'flash_init':
                set_game_state('main_menu')
            if back_button_rect.collidepoint(event.pos) and flash_game_state != 'flash_init':
                flash_game_state = 'flash_init'



    if flash_game_state == 'flash_init':
        screen.fill((140,183,230))
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
        screen.blit(blue_button, k_button_rect)
        screen.blit(k_letter, (screen.get_width() * 0.48, screen.get_height() * 0.255))
        screen.blit(blue_button, l_button_rect)
        screen.blit(l_letter, (screen.get_width() * 0.62, screen.get_height() * 0.255))
        screen.blit(blue_button, m_button_rect)
        screen.blit(m_letter, (screen.get_width() * 0.76, screen.get_height() * 0.255))
        screen.blit(blue_button, n_button_rect)
        screen.blit(n_letter, (screen.get_width() * 0.90, screen.get_height() * 0.255))
        screen.blit(blue_button, o_button_rect)
        screen.blit(o_letter, (screen.get_width() * 0.06, screen.get_height() * 0.405))
        screen.blit(blue_button, p_button_rect)
        screen.blit(p_letter, (screen.get_width() * 0.20, screen.get_height() * 0.405))
        screen.blit(blue_button, q_button_rect)
        screen.blit(q_letter, (screen.get_width() * 0.34, screen.get_height() * 0.405))
        screen.blit(blue_button, r_button_rect)
        screen.blit(r_letter, (screen.get_width() * 0.48, screen.get_height() * 0.405))
        screen.blit(blue_button, s_button_rect)
        screen.blit(s_letter, (screen.get_width() * 0.62, screen.get_height() * 0.405))
        screen.blit(blue_button, t_button_rect)
        screen.blit(t_letter, (screen.get_width() * 0.76, screen.get_height() * 0.405))
        screen.blit(blue_button, u_button_rect)
        screen.blit(u_letter, (screen.get_width() * 0.90, screen.get_height() * 0.405))
        screen.blit(blue_button, v_button_rect)
        screen.blit(v_letter, (screen.get_width() * 0.20, screen.get_height() * 0.555))
        screen.blit(blue_button, w_button_rect)
        screen.blit(w_letter, (screen.get_width() * 0.34, screen.get_height() * 0.555))
        screen.blit(blue_button, x_button_rect)
        screen.blit(x_letter, (screen.get_width() * 0.48, screen.get_height() * 0.555))
        screen.blit(blue_button, y_button_rect)
        screen.blit(y_letter, (screen.get_width() * 0.62, screen.get_height() * 0.555))
        screen.blit(blue_button, z_button_rect)
        screen.blit(z_letter, (screen.get_width() * 0.76, screen.get_height() * 0.555))
    
    if flash_game_state == 'flash_cards':
        screen.fill((140,183,230))
        print(flash_cards_list)
        screen.blit(flash_cards_list[random_picture_selector], flash_cards_list[15])
    
    screen.blit(back_button, back_button_rect)
    screen.blit(close_button, close_button_rect)
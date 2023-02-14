import pygame
import tkinter as tk
from gamestate import set_game_state

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

pygame.init()

# set display size
if screen_height == 1440:
    screen = pygame.display.set_mode((2560, 1440), pygame.FULLSCREEN)
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

lucky_font_large = pygame.font.Font('fonts/pixel/Pixeltype.ttf', int(screen.get_width() * 0.10))
se_font = lucky_font_large.render('SpyingEnvelope', True, (255,255,255))
productions_font = lucky_font_large.render('Productions', True, (255,255,255))
se_font_rect = se_font.get_rect(center = (screen.get_width() * 0.5, screen.get_height() * 0.4))
productions_font_rect = productions_font.get_rect(center = (screen.get_width() * 0.5, screen.get_height() * 0.6))
fade_bg = pygame.Surface((screen.get_width(), screen.get_height()))
fade_bg.fill((94,129,162))

pixel_font_large = pygame.font.Font('fonts/pixel/Pixeltype.ttf', int(screen.get_width() * 0.10))
the_font = pixel_font_large.render('THE', False, (255, 102, 102))
speech_font = pixel_font_large.render('SPEECH', True, (127, 0, 255))
games_font = pixel_font_large.render('GAMES', True, (255,255,255))
the_rect = the_font.get_rect(center = (screen.get_width() * 0.5, screen.get_height() * 0.4))
speech_rect = speech_font.get_rect(center = (screen.get_width() * 0.5, screen.get_height() * 0.5))
games_rect = games_font.get_rect(center = (screen.get_width() * 0.5, screen.get_height() * 0.6))

left_envelope = pygame.image.load('graphics/intro/left_envelope.png').convert_alpha()
right_envelope = pygame.image.load('graphics/intro/right_envelope.png').convert_alpha()
left_envelope = pygame.transform.scale(left_envelope, (screen.get_width() * 0.2, screen.get_height() * 0.2))
right_envelope = pygame.transform.scale(right_envelope, (screen.get_width() * 0.2, screen.get_height() * 0.2))

envelope_rect = left_envelope.get_rect(center = (screen.get_width() * 0.5, screen.get_height() * 0.2))

intro_animation = 'playing'
text_playing = 'se_prod'

def fade_in():
    fade = pygame.Surface((screen.get_width(), screen.get_height()))
    fade.fill((94,129,162))

    for alpha in range(250, 0, -1):
        if text_playing == 'se_prod':
            screen.blit(left_envelope, envelope_rect)
            screen.blit(se_font, se_font_rect)
            screen.blit(productions_font, productions_font_rect)
        elif text_playing == 'games':
            screen.blit(the_font, the_rect)
            screen.blit(speech_font, speech_rect)
            screen.blit(games_font, games_rect)
        fade.set_alpha(alpha)
        screen.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(2)
    
    if text_playing == 'se_prod':
        pygame.time.delay(200)
        screen.blit(right_envelope, envelope_rect)
        pygame.display.update()
        pygame.time.delay(300)
        screen.blit(left_envelope, envelope_rect)
        pygame.display.update()
        pygame.time.delay(300)
        screen.blit(right_envelope, envelope_rect)
        pygame.display.update()
        pygame.time.delay(300)
    else:
        pygame.time.delay(1100)

def fade_out():
    global intro_animation

    fade = pygame.Surface((screen.get_width(), screen.get_height()))
    fade.fill((94,129,162))

    for alpha in range(0, 250):
        if text_playing == 'se_prod':
            screen.blit(right_envelope, envelope_rect)
            screen.blit(se_font, se_font_rect)
            screen.blit(productions_font, productions_font_rect)
        elif text_playing == 'games':
            screen.blit(the_font, the_rect)
            screen.blit(speech_font, speech_rect)
            screen.blit(games_font, games_rect)
        fade.set_alpha(alpha)
        screen.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(2)
    
    intro_animation = 'done'

def intro_screen():
    global text_playing

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if intro_animation == 'playing':
            pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)

    if intro_animation == 'done':
        pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
        set_game_state('main_menu')
    
    if intro_animation == 'playing':
        screen.blit(fade_bg, (0,0))

        screen.blit(se_font,se_font_rect)
        screen.blit(productions_font, productions_font_rect)

        fade_in()
        fade_out()

        ### UNCOMMENT THIS SECTION TO ADD THE SPEECH GAMES TITLE SCREEN #####
        # text_playing = 'games'

        # pygame.time.delay(100)

        # fade_in()
        # fade_out()

    
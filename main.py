import pygame
import os
import random
from PIL import Image
from pygame.locals import *

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()

icon = pygame.image.load("images/icon.png")

display_width = 500
display_height = 500
fps = 75

width_half = display_width / 2
height_half = display_height / 2

os.environ['SDL_VIDEO_CENTERED'] = "1"

pygame.display.set_icon(icon)
pygame.display.set_caption("Collapsing Grid")
gameDisplay = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()

global screen_mode
screen_mode = 1

def screen_switch():
    global screen_mode
    if screen_mode == 1:
        gameDisplay = pygame.display.set_mode((display_width,display_height), pygame.FULLSCREEN)
        screen_mode = 2
    else:
        gameDisplay = pygame.display.set_mode((display_width,display_height))
        screen_mode = 1

def line(line_color, start_X, start_y, end_x, end_y):
    pygame.draw.line(gameDisplay, line_color, (start_X, start_y), (end_x, end_y))

def random_color():

    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

def main():

    up = True

    line1color = random_color()

    line1start_xcounter = 0
    line1start_ycounter = 0
    line1start_x = 0
    line1start_y = 0

    line1end_xcounter = 0
    line1end_ycounter = 0
    line1end_x = 0
    line1end_y = 0

    line2start_xcounter = 0
    line2start_ycounter = 0
    line2start_x = 500
    line2start_y = 0

    line2end_xcounter = 0
    line2end_ycounter = 0
    line2end_x = 500
    line2end_y = 0

    line3start_xcounter = 0
    line3start_ycounter = 0
    line3start_x = 0
    line3start_y = 500

    line3end_xcounter = 0
    line3end_ycounter = 0
    line3end_x = 0
    line3end_y = 500

    line4start_xcounter = 0
    line4start_ycounter = 0
    line4start_x = 500
    line4start_y = 500

    line4end_xcounter = 0
    line4end_ycounter = 0
    line4end_x = 500
    line4end_y = 500

    while up:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F4 or event.key == pygame.K_ESCAPE:
                    screen_switch()

        gameDisplay.fill((0,0,0))

        line(line1color, line1start_x, line1start_y, line1end_x, line1end_y)
        line(line1color, line2start_x, line2start_y, line2end_x, line2end_y)
        line(line1color, line3start_x, line3start_y, line3end_x, line3end_y)
        line(line1color, line4start_x, line4start_y, line4end_x, line4end_y)

        #line 1
        if 500 > line1start_xcounter >= 250:
            line1start_x += 1
        elif line1start_xcounter == 500:
            line1start_x = 0
            line1start_xcounter = 0

        if 500 > line1start_ycounter <= 250:
            line1start_y += 1
        elif line1start_ycounter == 500:
            line1start_y = 0
            line1start_ycounter = 0

        if 500 > line1end_xcounter <= 250:
            line1end_x += 1
        elif line1end_xcounter == 500:
            line1end_x = 0
            line1end_xcounter = 0

        if 500 > line1end_ycounter >= 250:
            line1end_y += 1
        elif line1end_ycounter == 500:
            line1end_y = 0
            line1end_ycounter = 0

        #line 2
        if 500 > line2start_xcounter <= 250:
            line2start_x -= 1
        elif line2start_xcounter >= 500:
            line2start_x = 500
            line2start_xcounter = 0

        if 500 > line2start_ycounter >= 250:
            line2start_y += 1
        elif line2start_ycounter == 500:
            line2start_y = 0
            line2start_ycounter = 0

        if 500 > line2end_xcounter >= 250:
            line2end_x -= 1
        elif line2end_xcounter == 500:
            line2end_x = 500
            line2end_xcounter = 0

        if 500 > line2end_ycounter <= 250:
            line2end_y += 1
        elif line2end_ycounter == 500:
            line2end_y = 0
            line2end_ycounter = 0

        #line 3
        if 500 > line3start_xcounter >= 250:
            line3start_x += 1
        elif line3start_xcounter >= 500:
            line3start_x = 0
            line3start_xcounter = 0

        if 500 > line3start_ycounter <= 250:
            line3start_y -= 1
        elif line3start_ycounter == 500:
            line3start_y = 500
            line3start_ycounter = 0

        if 500 > line3end_xcounter <= 250:
            line3end_x += 1
        elif line3end_xcounter == 500:
            line3end_x = 0
            line3end_xcounter = 0

        if 500 > line3end_ycounter >= 250:
            line3end_y -= 1
        elif line3end_ycounter == 500:
            line3end_y = 500
            line3end_ycounter = 0

        #line 4
        if 500 > line4start_xcounter >= 250:
            line4start_x -= 1
        elif line4start_xcounter >= 500:
            line4start_x = 500
            line4start_xcounter = 0

        if 500 > line4start_ycounter <= 250:
            line4start_y -= 1
        elif line4start_ycounter == 500:
            line4start_y = 500
            line4start_ycounter = 0

        if 500 > line4end_xcounter <= 250:
            line4end_x -= 1
        elif line4end_xcounter == 500:
            line4end_x = 500
            line4end_xcounter = 0

        if 500 > line4end_ycounter >= 250:
            line4end_y -= 1
        elif line4end_ycounter == 500:
            line4end_y = 500
            line4end_ycounter = 0
            line1color = random_color()

        line1start_xcounter += 1
        line1start_ycounter += 1
        line1end_xcounter += 1
        line1end_ycounter += 1

        line2start_xcounter += 1
        line2start_ycounter += 1
        line2end_xcounter += 1
        line2end_ycounter += 1

        line3start_xcounter += 1
        line3start_ycounter += 1
        line3end_xcounter += 1
        line3end_ycounter += 1

        line4start_xcounter += 1
        line4start_ycounter += 1
        line4end_xcounter += 1
        line4end_ycounter += 1

        pygame.display.update()
        clock.tick(fps)

main()
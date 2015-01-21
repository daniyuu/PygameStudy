#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      daniyuu
#
# Created:     21/01/2015
# Copyright:   (c) daniyuu 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#!/usr/bin/env python

background_image_filename = 'sushiplate.jpg'
mouse_image_filename = 'fugu.png'

import pygame
from pygame.locals import *
from sys import exit


def main():
    pygame.init()

    screen = pygame.display.set_mode((640, 480), 0, 32)
    pygame.display.set_caption("Hello, World!")
    background = pygame.image.load(background_image_filename).convert()
    mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                print event.type
                print QUIT
                exit()

        screen.blit(background, (0,0))

        x, y = pygame.mouse.get_pos()
        x-= mouse_cursor.get_width() / 2
        y-= mouse_cursor.get_height() / 2
        screen.blit(mouse_cursor, (x, y))
        pygame.display.update()


if __name__ == '__main__':
    main()

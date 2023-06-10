from pygame.math import Vector2
import pygame
from os import walk



# get path image for animation
def get_path_animation(path):
    pass


#creen 
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
TITLE_SIZE = 64


pygame.init()
text_font = pygame.font.Font(None, 50)


def get_mouse_pos():
    mouse_pos = pygame.mouse.get_pos()
    print(mouse_pos)
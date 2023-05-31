import pygame
import pygame
import random

pygame.init()

# Game window settings
WIDTH = 288
HEIGHT = 512
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Assets
BG_IMG = pygame.image.load('assets/background.png').convert()
BIRD_IMG = pygame.image.load('assets/bird.png').convert_alpha()
PIPE_IMG = pygame.image.load('assets/pipe.png').convert_alpha()

# Bird class
class Bird:
    GRAVITY = 0.5
    JUMP_VEL = -8

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 0
        self.img = BIRD_IMG

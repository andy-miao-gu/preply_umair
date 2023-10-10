import pygame as gg
import numpy as np
import pygame.mixer as pmx

gg.init()
pmx.init()


pmx.music.load("andy.mp3")

WHITE = (255,255,255)
BLACK = (0,0,0)
HEIGHT = 600
WIDTH = 600
GRID_H = HEIGHT// 20
GRID_W = WIDTH// 20
pos_x = 0
pos_y = 0



box_color = (0,0,255)

screen = gg.display.set_mode((500,600))
gg.display.set_caption("Andy's Tetris")
game_over = False

objects = [

np.array([ [0,1,0],[1,1,1] ]),
np.array([ [1,1,1],[0,1,0] ]),



]

def make_grid():
    for i in range(0,HEIGHT,GRID_H):
        gg.draw.line(screen, WHITE,(i,0),(i,HEIGHT) )
    for bye in range(0,WIDTH,GRID_W):
        gg.draw.line(screen, WHITE,(0,bye),(WIDTH,bye) )
#pmx.music.play(-1)
key_pressed = False
while not game_over:
    for event in gg.event.get():
        if event.type == gg.QUIT:
            game_over = True

        if event.type == gg.KEYDOWN and not key_pressed:
            
            if keys[gg.K_RIGHT]:
                pos_x = pos_x+GRID_W
            elif keys[gg.K_LEFT]:
                pos_x = pos_x-GRID_W

            key_pressed = True
        
    # Handle user input for moving and rotating Tetrominoes
    make_grid( )
    gg.draw.rect(screen, box_color,(pos_x,pos_y,GRID_H,GRID_W) )
    keys = gg.key.get_pressed()
    if not keys:
        key_pressed = False

    # Update game logic: move Tetrominoes, check for collisions, clear lines, etc.
 

        
    # Draw the game: Tetrominoes, grid, score, etc.

    gg.display.update()
    
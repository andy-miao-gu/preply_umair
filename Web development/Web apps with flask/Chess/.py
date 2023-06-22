import pygame as gm
## here i am importing pygame

gm.init()

board_width = 400
board_height = 400

logo_width = 50
logo_height = 50

step_size = 50

logo_x = board_width //2 - logo_width //2
logo_y = board_height//2 - logo_height//2

logo_direction = "forward"

chessboard = gm.Surface(board_width,board_height)
chessboard.fill(255,255,255)


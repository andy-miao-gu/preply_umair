import pygame
import chess
import chess.svg

pygame.init()

size = (400, 400)
screen = pygame.display.set_mode(size)

board = chess.Board

while not board.is_game_over():
    svg_board = chess.svg.board(board=board).encode("UTF-8")
    svg_image = pygame.image.frombuffer(svg_board, size)
    screen.blit(svg_image, (0, 0))
    pygame.display.flip
    if board.turn == chess.WHITE:
        move = input("white's move")
    else :
        move = input("black's move")
    try:
        board.push_san(move)
    except ValueError:
        print("invalid move")
print(board.result)
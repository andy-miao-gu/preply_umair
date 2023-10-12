import pygame

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 600
BLOCK_SIZE = 30
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Initialize the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Game variables
piece_x = 5  # Initial piece position

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        piece_x -= 1
    if keys[pygame.K_RIGHT]:
        piece_x += 1

    screen.fill(WHITE)  # Clear the screen
    pygame.draw.rect(
        screen,
        RED,  # Color
        pygame.Rect(piece_x * BLOCK_SIZE, HEIGHT - BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE),
    )
    pygame

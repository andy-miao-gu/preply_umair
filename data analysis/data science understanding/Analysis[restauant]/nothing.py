import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Plants vs. Zombies Lite")

# Player (plant) properties
player_x = WIDTH // 2
player_y = HEIGHT - 50
player_width = 50
player_height = 50
player_speed = 5

# Bullet properties
bullet_width = 10
bullet_height = 20
bullet_speed = 10

bullets = []

# Zombie properties
zombie_width = 50
zombie_height = 50
zombie_x = random.randint(0, WIDTH - zombie_width)
zombie_y = 0
zombie_speed = 2

def draw_player(x, y):
    pygame.draw.rect(screen, RED, (x, y, player_width, player_height))

def draw_bullet(x, y):
    pygame.draw.rect(screen, RED, (x, y, bullet_width, bullet_height))

def draw_zombie(x, y):
    pygame.draw.rect(screen, WHITE, (x, y, zombie_width, zombie_height))

def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
            player_x += player_speed

        # Fire a bullet
        if keys[pygame.K_SPACE]:
            bullet_x = player_x + player_width / 2 - bullet_width / 2
            bullet_y = player_y
            bullets.append([bullet_x, bullet_y])

        # Update bullet positions
        for bullet in bullets:
            bullet[1] -= bullet_speed

        # Update zombie position
        zombie_y += zombie_speed
        if zombie_y > HEIGHT:
            zombie_x = random.randint(0, WIDTH - zombie_width)
            zombie_y = 0

        # Collision detection
        for bullet in bullets:
            if (zombie_x < bullet[0] < zombie_x + zombie_width and
                zombie_y < bullet[1] < zombie_y + zombie_height):
                zombie_x = random.randint(0, WIDTH - zombie_width)
                zombie_y = 0
                bullets.remove(bullet)

        # Draw everything
        screen.fill((0, 0, 0))
        draw_player(player_x, player_y)
        for bullet in bullets:
            draw_bullet(bullet[0], bullet[1])
        draw_zombie(zombie_x, zombie_y)
        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

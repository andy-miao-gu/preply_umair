import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Plants vs. Zombies")

# Load image assets
background_image = pygame.image.load("background.png")
sunflower_image = pygame.image.load("sunflower.png")
peashooter_image = pygame.image.load("peashooter.png")
cherrybomb_image = pygame.image.load("cherrybomb.png")
zombie_image = pygame.image.load("zombie.png")
wallnut_image = pygame.image.load("wallnut.png")
snowpea_image = pygame.image.load("snowpea.png")
repeater_image = pygame.image.load("repeater.png")
threepeater_image = pygame.image.load("threepeater.png")
firepea_image = pygame.image.load("firepea.png")
boomerang_image = pygame.image.load("boomerang.png")
watermelon_image = pygame.image.load("watermelon.png")
torchwood_image = pygame.image.load("torchwood.png")
cattail_image = pygame.image.load("cattail.png")

# Plant class
class Plant(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.health = 100  # Plant health

    def update(self):
        # Plant behavior logic
        pass

# Create groups for plants and zombies
all_sprites = pygame.sprite.Group()
plants = pygame.sprite.Group()

# Create plants
peashooter = Plant(100, 100, peashooter_image)
sunflower = Plant(200, 100, sunflower_image)
cherrybomb = Plant(300, 100, cherrybomb_image)
wallnut = Plant(400, 100, wallnut_image)
snowpea = Plant(500, 100, snowpea_image)
repeater = Plant(600, 100, repeater_image)
threepeater = Plant(700, 100, threepeater_image)
firepea = Plant(100, 200, firepea_image)
boomerang = Plant(200, 200, boomerang_image)
watermelon = Plant(300, 200, watermelon_image)
torchwood = Plant(400, 200, torchwood_image)
cattail = Plant(500, 200, cattail_image)

# Add plants to the sprite groups
all_sprites.add(peashooter, sunflower, cherrybomb, wallnut, snowpea, repeater, threepeater, firepea, boomerang, watermelon, torchwood, cattail)
plants.add(peashooter, sunflower, cherrybomb, wallnut, snowpea, repeater, threepeater, firepea, boomerang, watermelon, torchwood, cattail)

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic
    all_sprites.update()

    # Drawing
    window.blit(background_image, (0, 0))

    all_sprites.draw(window)

    # Update the display
    pygame.display.update()

# Quit the game
pygame.quit()

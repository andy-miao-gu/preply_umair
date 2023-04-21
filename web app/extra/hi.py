import pygame
import random

pygame.init()

# set up the game window
WINDOW_WIDTH = 288
WINDOW_HEIGHT = 512
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# set up the game clock
clock = pygame.time.Clock()

# load the background image
background_image = pygame.image.load("background.png").convert()

# load the bird image
bird_image = pygame.image.load("bird.png").convert()
bird_image.set_colorkey((255, 255, 255))

# set up the bird sprite
class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = bird_image
        self.rect = self.image.get_rect()
        self.rect.center = (50, WINDOW_HEIGHT // 2)
        self.velocity = 0

    def update(self):
        self.velocity += 0.5
        self.rect.y += self.velocity

    def flap(self):
        self.velocity = -8

# set up the pipe sprite
class Pipe(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.Surface((52, 320))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = position
        self.velocity = -3

    def update(self):
        self.rect.x += self.velocity

# set up the game loop
def game_loop():
    bird = Bird()
    pipes = pygame.sprite.Group()
    score = 0
    while True:
        # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.flap()

        # update game objects
        bird.update()
        pipes.update()

        # add new pipes
        if len(pipes) < 4:
            if random.randint(0, 100) == 0:
                top_pipe = Pipe((WINDOW_WIDTH, random.randint(50, 250)))
                bottom_pipe = Pipe((WINDOW_WIDTH, top_pipe.rect.bottom + 100))
                pipes.add(top_pipe)
                pipes.add(bottom_pipe)

        # remove offscreen pipes
        for pipe in pipes:
            if pipe.rect.right < 0:
                pipes.remove(pipe)

        # check for collisions
        if pygame.sprite.spritecollide(bird, pipes, False):
            pygame.quit()
            quit()

        # draw game objects
        game_window.blit(background_image, (0, 0))
        pipes.draw(game_window)
        game_window.blit(bird_image, bird.rect)
        pygame.display.update()

        # update score
        score += 1
        if score % 100 == 0:
            print("Score:", score)

        # cap the frame rate
        clock.tick(60)

game_loop()

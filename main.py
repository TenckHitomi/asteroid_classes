import pygame
import sys


class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__
        self.image = pygame.image.load('../images/background.png').convert_alpha()


# Display window
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter")
clock = pygame.time.Clock()

# Game Loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Delta time
    dt = clock.tick() / 1000

    # Draw the frame
    pygame.display.update()

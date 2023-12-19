import random
import pygame

pygame.init()

#screen tingz
width = 1000
height = 800
WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption("On Task!!")

#color defs
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRASS = (0, 204, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
PURPLE = (127, 0, 255)
PINK = (255, 51, 255)
TEAL = (0, 255, 255)

run = True
while run:

    WIN.fill(PURPLE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                run = False
    
    pygame.display.flip()
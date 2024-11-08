#While Loop



#For Loop




#Pygame use case
import pygame
import sys

pygame.init()

window = pygame.display.set_mode((400,600))

pygame.display.set_caption('CS24-25')

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    
    pygame.display.flip()

    clock.tick(60)
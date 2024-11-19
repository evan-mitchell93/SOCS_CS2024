#Evan Mitchell
#11/19

import pygame
import sys

pygame.init()

window = pygame.display.set_mode((500,500))

pygame.display.set_caption('CS SHAPES')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    window.fill((200,200,200))
    pygame.display.flip()

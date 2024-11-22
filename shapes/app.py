#Evan Mitchell
#11/19

import pygame
import sys
import random
from circle import Circle

pygame.init()

window = pygame.display.set_mode((500,500))

pygame.display.set_caption('CS SHAPES')
clock = pygame.time.Clock()

circles = [] #list used to keep track of multiple circles
first_circle = Circle(10,250) # define a circle
circles.append(first_circle) #add the circle to our list
circles.append(Circle(300,27)) # we can also define a new circle in the append

while True:
    window.fill((100,100,100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        #Add a new circle once spacebar is released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                circles.append(Circle(random.randint(50,450),random.randint(50,450)))

    #Determine if the boundary has been reached
    #circles is a collection that we can loop over
    for c in circles:
        c.check_boundary()
        #update our x and y values with directional variables
        c.y += c.y_dir
        c.x += c.x_dir
        pygame.draw.circle(window,c.color,(c.x,c.y),10)
    pygame.display.flip()
    clock.tick(120)
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

#auto movement
ydirection = -1
xdirection = 1
first_circle = Circle(10,250)
circles = [] #how do we represent a circle? List of lists? Other collection? Class?
circles.append(first_circle)
second_circle = Circle(300,25)
circles.append(second_circle)

while True:
    window.fill((100,100,100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    
    #Determine if the boundary has been reached
    #Move this into a function (Friday)
    #Keep track of circle data independently (multiple circles)
    for c in circles:
        if c.y <= 0 or c.y >= 500:
            ydirection *= -1
            
        if c.x <= 0 or c.x >= 500:
            xdirection *= -1

        #Independent x and y direction variables
        c.y += ydirection
        c.x += xdirection

        pygame.draw.circle(window,c.color,(c.x,c.y),10)
    pygame.display.flip()
    clock.tick(120)
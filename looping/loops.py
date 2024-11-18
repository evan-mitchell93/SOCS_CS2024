#While Loop
#control variable
x = 0
while x < 10:
    #loop body
    #print(x)
    x = x + 1


#Infinite loop are bad: usually an error with conditional or update
y = 10
while y > 0:
    #print(y)
    y = y - 1



#For Loop
for r in range(0,10,2):
    print(r)

for j in range(10,0,-2):
    print(j)


#Pygame use case
import pygame
import sys

pygame.init()

window = pygame.display.set_mode((400,600))

pygame.display.set_caption('CS24-25')



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    pygame.draw.circle(window,(255,255,0),(100,100),10,10)
    pygame.display.flip()

import pygame
import math
import sys
import bubble

shoot_angle = math.pi
shoot_x = 250
shoot_y = 600
bubbles = []
current_bubble = bubble.Bubble(shoot_x,shoot_y,shoot_angle)
bubbles.append(current_bubble)
pygame.init()

window = pygame.display.set_mode((500,600))

pygame.display.set_caption('Bubble Shooter')

clock = pygame.time.Clock()

#check if bubble has collided with another bubble
def check_collision(bubble,list_of_bubbles):
    for bub in list_of_bubbles:
        #offset to prevent the bubbles from stopping immediately
        if bub != bubble and bubble.pos_y < 475:
            #the distance between the center of both bubbles is less than 48
            d = math.sqrt((bub.pos_x - bubble.pos_x) ** 2 + (bub.pos_y - bubble.pos_y) ** 2)
            if abs(d) <= 48:
                #if they have the same color we want to keep track of that in a list
                #that way we can delete sets of 3 or more. The problem is going to be
                #finding out how we would like to connect two separate neighbors
                #without looping through the entire set of bubbles every iteration.
                if(bubble.color == bub.color):
                    bub.neighbors.append(bubble)
                    for neighbor in bub.neighbors:
                        if neighbor != bubble:
                            bubble.neighbors.append(neighbor)
                if(len(bubble.neighbors) > 2):
                    for b in bubble.neighbors:
                        bubbles.remove(b)
                bubble.moving = False
                break

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                current_bubble.set_moving()
                new_bubble = bubble.Bubble(shoot_x,shoot_y,shoot_angle)
                current_bubble = new_bubble
                bubbles.append(new_bubble)

    #Angle controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        shoot_angle -= 0.01
        current_bubble.angle = shoot_angle
    if keys[pygame.K_d]:
        shoot_angle += 0.01
        current_bubble.angle = shoot_angle
    window.fill('grey')

    #update position and draw each circle
    for bub in bubbles:
        if bub.moving == True:
            bub.check_sides(500)
            check_collision(bub,bubbles)
            bub.check_top()
            bub.update_pos()
        pygame.draw.circle(window,bub.get_color(),(bub.pos_x,bub.pos_y),25,2)
        
    #draw our aiming line    
    pygame.draw.line(window,(0,255,255),(shoot_x,shoot_y),(shoot_x - math.sin(shoot_angle) * 30, shoot_y + math.cos(shoot_angle) * 30),2)
    pygame.display.flip()

    clock.tick(120)
    

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
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        shoot_angle -= 0.01
        current_bubble.angle = shoot_angle
    if keys[pygame.K_d]:
        shoot_angle += 0.01
        current_bubble.angle = shoot_angle
    window.fill('grey')
    for bub in bubbles:
        if bub.moving == True:
            bub.check_sides(500)
            bub.check_top(600)
            bub.update_pos()
        pygame.draw.circle(window,bub.get_color(),(bub.pos_x,bub.pos_y),25,25)
            
    pygame.draw.line(window,(0,255,255),(shoot_x,shoot_y),(shoot_x - math.sin(shoot_angle) * 30, shoot_y + math.cos(shoot_angle) * 30),2)
    pygame.display.flip()

    clock.tick(120)
    

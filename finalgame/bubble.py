import random
import math

class Bubble:
    colors = [(255,0,0),(0,255,0),(0,0,255)]
    def __init__(this,pos_x,pos_y,angle):
        this.neighbors = []
        this.pos_x = pos_x
        this.pos_y = pos_y
        this.angle = angle
        this.moving = False
        #generate a random color
        this.color = random.choice(this.colors)
        this.neighbors = [this]
    def update_pos(this):
        if this.moving == True:
            this.pos_x = this.pos_x - math.sin(this.angle) * 2
            this.pos_y = this.pos_y + math.cos(this.angle) * 2
    
    def check_sides(this,width):
        if this.pos_x <= 0 or this.pos_x >= width:
            this.angle *= -1

    #be replaced with code to check collision with other bubbles 
    def check_top(this):
        if this.pos_y <= 0:
            this.moving = False
    
    def get_color(this):
        return this.color
    
    def set_moving(this):
        this.moving = True
    


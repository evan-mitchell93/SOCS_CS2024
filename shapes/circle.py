#Class for representing a circle
#On Friday 11/22 we saw that our circles move in the 
#same direction and change directions at the same time.
#one circle may not hit a boundary but still changes
#we need to add independent directional data for each circle

import random

class Circle:
    #init function runs everytime we create a class
    def __init__(self,pos_x,pos_y):
        self.x = pos_x
        self.y = pos_y
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        #randomly generate the direction values
        self.x_dir = random.choice([-1,1])
        self.y_dir = random.choice([-1,1])
        self.radius = random.randint(10,75)

    #Move our boundary check into the class.
    def check_boundary(self):
        if self.x <= 0 or self.x >= 500:
            self.x_dir *= -1
        if self.y <= 0 or self.y >= 500:
            self.y_dir *= -1
        
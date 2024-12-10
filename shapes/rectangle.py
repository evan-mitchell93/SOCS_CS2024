import random

class Rectangle:
    def __init__(self,pos_x,pos_y,length,width):
        self.x = pos_x
        self.y = pos_y
        self.length = length
        self.width = width
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.x_dir = random.choice([-1,1])
        self.y_dir = random.choice([-1,1])

    #Move our boundary check into the class.
    def check_boundary(self):
        if self.x <= 0 or self.x >= 500:
            self.x_dir *= -1
        if self.y <= 0 or self.y >= 500:
            self.y_dir *= -1
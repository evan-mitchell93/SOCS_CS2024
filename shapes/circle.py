#Class for representing a circle
import random

class Circle:
    #init function runs everytime we create a class
    def __init__(self,pos_x,pos_y):
        self.x = pos_x
        self.y = pos_y
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        
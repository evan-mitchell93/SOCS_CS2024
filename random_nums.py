import math
import random

# a random number between 0.0 and .999
num1 = random.random()
print(num1)
#multiply random number by 10
num1 = num1 * 10
print(num1)
#remove the decimal places
num1 = math.floor(num1)
print(num1)

# 1- 10
rannum = math.floor(random.random() * 10) + 1
print(rannum)

#0-10
rannum = math.floor(random.random() * 11)
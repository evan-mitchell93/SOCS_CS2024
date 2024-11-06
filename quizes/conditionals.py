#Evan Mitchell
#11/6/2024
#Solution for Quiz over Conditionals

import math
import random

ran1 = math.floor(random.random() * 10)
ran2 = math.floor(random.random() * 10)

if ran1 > ran2:
    print(ran1," is larger")
elif ran2 > ran1:
    print(ran2, " is larger")
else:
    print("Numbers are equal")

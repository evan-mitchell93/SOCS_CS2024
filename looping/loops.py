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
    y = y + 1 #creates infinite loop



#For Loops iterate over a collection
#The range function returns a list of numbers between start and stop
#The third argument is the step value between each number

for r in range(0,10,2):
    print(r)

for j in range(10,0,-2):
    print(j)


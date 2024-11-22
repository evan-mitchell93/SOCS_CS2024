#Functions

#Blocks of code that are only executed when called
#Pass arguments/parameters to the function

#defining the function
def myFunction():
    #Indented section is the function body
    print("Hello World")

#calling the function
myFunction()

my_x = 5
my_y = 5
#Arguments/Parameters
def my_addition(x,y):
    x += 1
    y += 1
    return x + y

#order matters but names do not
#my_y gets mapped to x parameter and my_x gets mapped to y

z = my_addition(my_y,my_x)

#default values
#we can assign a default value and omit passing an argument
#in the function call
def my_default(x, y=1):
    return x + y

print(my_default(3)) #we only pass in an x value, y defaults to 1
print(my_default(3,3)) #we pass both arguments y is set to 3


#Variable number of arguments use the *
def my_var(*args):
    #the variable name args will contain a collection
    #of the passed in values
    #becaue it is a collection we can for loop through the values
    for value in args:
        print(value)

print("First run: ")
my_var(1)
print("Second run: ")
my_var(1,"bob","hello",3,2,4)

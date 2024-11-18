#Functions

#Blocks of code that are only executed when called
#Pass arguments/parameters to the function
#Useful for readability, tasks that need to executed in many different
#places or multiple times as well as abstraction.

#defining the function
def myFunction():
    #Indented section is the function body
    print("Hello World")

#calling the function
#myFunction()

x = 5
y = 5
#Arguments/Parameters
def my_addition(x):
    x += 1
    y += 1
    return x + y

#order matters but names do not
z = my_addition(x)
print(z)
print(y)
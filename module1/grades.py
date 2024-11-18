score = int(input("Enter a score or -1 to quit: ")) #Initial control value
QUIT = -1
number_tests = 0 #Accumulator
test_sum = 0 #Accumulator

while score != QUIT:#Test our control
    number_tests += 1 #Increment counter 
    test_sum += score #Add score to our total
    score = int(input("Enter another score or -1 to quit: "))#Update control variable

avg = test_sum/number_tests
if avg >= 90:
    print("A")
elif avg >= 80:
    print("B")
elif avg >=70:
    print("C")
elif avg >= 60:
    print("D")
else:
    print("F")


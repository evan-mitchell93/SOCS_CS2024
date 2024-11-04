import random

def generate_unique_id(n):
    numbers = set()
    while len(numbers) < n:
        number = random.randint(1000,9999)
        numbers.add(number)
    return list(numbers)

def save_ids(l):
    f = open("student_4_digit.txt","a")
    for id in l:
        f.write(str(id)+"\n")
    
    f.close()


list_of_ids = generate_unique_id(569)
save_ids(list_of_ids)

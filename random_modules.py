import math;
import random;

radians = 0.7
height = math.sin(radians)
print("height :", height)

def show_type(type):
    print(type)

def show_length(data):
    return len(data)

for i in range(5):
    randomNumber = random.random();
    print("number between 0 and 1,", i, ":", randomNumber)

for i in range(5):
    randomNumber = random.randint(5, 10);
    print("number between 5 and 10,", i, ":", randomNumber)

for i in range(5):
    randomNumber = random.choice([2, 7, 9]);
    print("number between pointed :",  randomNumber)

show_type(show_length)
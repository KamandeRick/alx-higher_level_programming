#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number == 0:
    digLast = 0
elif number > 0:
    digLast = int(str(number)[-1])
else:
    digLast = -1 * (int(str(number)[-1]))
if digLast > 5:
    str = "and is greater than 5"
elif digLast == 0:
    str = "and is 0"
elif digLast < 6 and digLast != 0:
    str = "and is less than 6 and not 0"
print(f"Last digit of {number:d} is {digLast:d} {str}")

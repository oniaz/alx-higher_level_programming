#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    digit = ((number * -1) % 10) * -1
else:
    digit = number % 10
if digit == 0:
    str = "and is 0"
elif digit > 5:
    str = "and is greater than 5"
else:
    str = "and is less than 6 and not 0"
print(f"Last digit of {number:d} is {digit:d} {str}")

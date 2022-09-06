#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = int(str(number)[-1])
if last > 5:
    print(f'Last digit of {number} is {last} and is greater than 5')
if last == 0:
    print(f'Last digit of {number} is {last} and is zero')
if last < 6 or number != 0:
    print(f'Last digit of {number} is {last} and is less than 6 and not 0')

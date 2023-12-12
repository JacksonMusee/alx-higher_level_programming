#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_dig = 0
tail = ""

if number < 0:
    number_n = number * -1
    last_dig = (number_n % 10) * -1
else:
    last_dig = number % 10
tail = ""

if last_dig > 5:
    tail = "is greater than 5"
if last_dig == 0:
    tail = "is 0"
if last_dig < 6 and last_dig != 0:
    tail = "is less than 6 and not 0"

print(f"Last digit of {number} is {last_dig} and " + f"{tail}")

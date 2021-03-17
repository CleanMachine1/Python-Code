#!/usr/bin/python3.7

# Multiples of:
# fizz = 3 
# buzz = 5
# fizzbuzz = 3 and 5

for number in range(1, 16):
    if number % 3 ==  0 and number % 5 == 0:
        print("fizzbuzz") 
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)
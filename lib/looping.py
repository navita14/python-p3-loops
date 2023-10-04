#!/usr/bin/env python3

def happy_new_year():
    i = 0
    while i <= 10:
        print(i)
        print("Happy New Year!")
        i += 1

happy_new_year()


def square_integers(int_list):
    squared_nums = []
    for nums in int_list:
        squared_nums.append(nums ** 2)
    return squared_nums

    

def fizzbuzz():
    for num in range(1,101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
    

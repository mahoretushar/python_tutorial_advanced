#!/usr/bin/env python3
def main():
    print("Inside main Function\n")
    x = int(input("Enter a value you want to find a Square of:\n"))
    sq = square(x)
    function()
    print(sq)
    return 0

def square(x):
    """
    A Simple function to calculate square of a number by addition
    """
    sum_so_far = 0
    for counter in range(x):
        sum_so_far = sum_so_far + x
    return sum_so_far

def function():
    print("This is what it is")
    return 0

main()

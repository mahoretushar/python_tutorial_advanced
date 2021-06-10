#!/usr/bin/env python3

# Below is the main function which I am going to use like the C-Lang main() function

def add():
    print("Entering Addiition Functio\n") # Displaying output on screen
    x = int(input("Enter Value of X\n")) # Converting input into Integer
    y = int(input("\nEnter Value of Y\n"))
    print("\nThe Addition of X and Y is:",x+y)
    return 0

def main():
    print("Entering in Main Function\n")
    add()
    print("Exiting Main Function\n")
    return 0 # A return statement which right now is not going to return anything or it is returning 0

main()

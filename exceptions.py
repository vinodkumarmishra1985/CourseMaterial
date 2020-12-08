import sys

try:
    x = int (input("x:"))
    y = int (input("y:"))
except ValueError:
    print ("Error invalid input")
    sys.exit(1)

try:
    result = x/y
except ZeroDivisionError:
    print ("Error: Cannnot divide by 0.")
    sys.exit(1) #exit the program with status code 1. 1 means something went wrong.

print (f"{x} / {y} is {result}")

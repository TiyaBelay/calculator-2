"""Calculate various mathematical functions"""
#imports all arithmetic.py (module)
from arithmetic import *

#initiate blank prompt for user input
user_input_raw = raw_input()
#create a list from the raw input
user_input_list = user_input_raw.split(" ")
#Assign variables to list elements
operator = user_input_list[0]
num1 = int(user_input_list[1])
num2 = int(user_input_list[2])

#Evaluate operator variable
if operator == "+": 
    #Create variable for module call
    answer = add(num1,num2)
    print answer

elif operator == "-":
    answer = subtract(num1, num2)
    print answer

elif operator == "*":
    answer = multiply(num1, num2)
    print answer

elif operator == "/":
    answer = divide(num1, num2)
    print answer

elif operator == "*":
    answer = square(num1)
    print answer

elif operator == "*":
    answer = cube(num1)
    print answer

elif operator == "**":
    answer = power(num1, num2)
    print answer

elif operator == "%":
    answer = mod(num1, num2)
    print answer
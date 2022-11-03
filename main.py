# Program make a simple calculator
from contextlib import nullcontext
import logging
import sys
import inspect

from calculate import add, subtract, multiply, divide
from exit import isExit

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(u'[%(asctime)s] %(message)s')
file_handler = logging.FileHandler('output.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide") 

while True:
    # take input from the xuser
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = None # 숫자가 아닌 값이 들어갈 경우 except에 의해 이전값이 사용될 수 있으니 초기화.
            num2 = None
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            logging.info(f'INFO: input numbers are {num1} and {num2}')
        except ValueError as e:
            logging.error(f'Errorno: {e}')
            print('Please enter only numbers')
            next_calculation = isExit()
            if next_calculation == "no":
                break
            elif next_calculation == "yes":
                continue


        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
    
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
           
        elif choice == '4':
            try:         
                print(num1, "/", num2, "=", divide(num1, num2))
            except ZeroDivisionError as e:
                print("Not divisible by zero")
                logger.error(f'Error: {e}')


        next_calculation = isExit()
        if next_calculation == "no":
            break
        elif next_calculation == "yes":
            continue


    else:
        logging.warning("Warning: Invalid Input")
        print("Invalid Input. Please select one of 1,2,3,4")

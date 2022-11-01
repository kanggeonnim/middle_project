# Program make a simple calculator
import logging
import sys
import inspect

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(u'[%(asctime)s] %(message)s')
file_handler = logging.FileHandler('output.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
# This function adds two numbers
def add(x, y):
    result = x + y
    logger.info(f'{inspect.currentframe().f_code.co_name} {y}, {x} result = {result}')
    return result

# This function subtracts two numbers
def subtract(x, y):
    result = x - y
    logger.info(f'{inspect.currentframe().f_code.co_name} {y}, {x} result = {result}')
    return result

# This function multiplies two numbers
def multiply(x, y):
    result = x * y
    logger.info(f'{inspect.currentframe().f_code.co_name} {y}, {x} result = {result}')
    return result

#Need to define divide function.
def divide (x,y):
    result = x / y
    logger.info(f'{inspect.currentframe().f_code.co_name} {y}, {x} result = {result}')
    return result

yesno_list = ['yes', 'y', 'no', 'n']

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide") 


while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            logging.info(f'INFO: input numbers are {num1} and {num2}')
        except ValueError as e:
            logging.error(f'Errorno: {e}')

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

        # check if user wants another calculation
        # break the while loop if answer is no

        next_calculation = (input("Let's do next calculation? (yes/no): ")).lower()
        while True:
            if next_calculation in yesno_list:
                break
            else:
                next_calculation = (input("Please answer only (yes/no): ")).lower()
        if next_calculation == "no" or next_calculation == "n":
            break
        elif next_calculation =="yes" or next_calculation == 'y':
            continue


    else:
        logging.warning("Warning: Invalid Input")
        print("Invalid Input. Please select one of 1,2,3,4")

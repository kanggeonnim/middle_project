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

yes_list = ['yes', 'y']
no_list = ['no', 'n']

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
            
            if next_calculation in yes_list:    # 계산을 더 하고 싶을 때
                break
            elif next_calculation in no_list:   # 더이상 계산을 하지 않을 때
                exit_answer = (input("Are you sure? (yes/no): ")).lower()   # 한번 더 물어봄

                while True: # yes 또는 no로만 대답을 받을 때 까지 질문함.

                    if exit_answer in yes_list or exit_answer in no_list:
                        break
                    else:   # 선택지에 없는 입력을 받았을 경우
                        exit_answer = (input("Quit the calculator? Please answer only (yes/no): ")).lower()

                if exit_answer in no_list: # 사실 속마음은 프로그램 종료를 원하지 않을 경우
                    next_calculation = "yes"
                elif exit_answer in yes_list: # 정말로 프로그램 종료를 원하는 경우
                    break

            else:   # 선택지에 없는 입력을 받았을 경우
                next_calculation = (input("Calculation again? Please answer only (yes/no): ")).lower()

        if next_calculation in no_list:
            break
        elif next_calculation in yes_list:
            continue


    else:
        logging.warning("Warning: Invalid Input")
        print("Invalid Input. Please select one of 1,2,3,4")

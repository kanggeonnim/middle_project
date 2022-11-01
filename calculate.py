import logging
import sys
import inspect

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

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




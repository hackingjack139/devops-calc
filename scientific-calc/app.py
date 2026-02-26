import math
import logging
from pythonjsonlogger import jsonlogger
import os

# Create logs directory if it doesn't exist
os.makedirs('logs', exist_ok=True)

logger = logging.getLogger('devops-calc')
logger.setLevel(logging.INFO)

logHandler = logging.FileHandler('logs/calc.log')
formatter = jsonlogger.JsonFormatter('%(asctime)s %(levelname)s %(name)s %(message)s')
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)

def displayMenu():
    print('Select an option:')
    print('1: Square root function - \u221ax')
    print('2: Factorial function - x!')
    print('3: Natural logarithm (base е) - ln(x)')
    print('4: Power function - x^b')
    print('5: Exit')

def squareRoot(x):
    if x < 0:
        logger.error("Square root failed: negative input", extra={"operation": "sqrt", "input": x})
        raise ValueError('Square root for negative numbers is not defined')
    else:
        result = math.sqrt(x)
        logger.info("Square root calculated", extra={"operation": "sqrt", "input": x, "result": result})
        return result

def factorial(x):
    if x < 0:
        logger.error("Factorial failed: negative input", extra={"operation": "factorial", "input": x})
        raise ValueError('Factorial for negative numbers is not defined')
    else:
        result = math.factorial(x)
        logger.info("Factorial calculated", extra={"operation": "factorial", "input": x, "result": result})
        return result
    
def naturalLogarithm(x):
    if x <= 0:
        logger.error("Natural log failed: input <= 0", extra={"operation": "ln", "input": x})
        raise ValueError('Natural logarithm for numbers less than or equal to 0 is not defined')
    else:
        result = math.log(x)
        logger.info("Natural log calculated", extra={"operation": "ln", "input": x, "result": result})
        return result

def powerFunction(x, b):
    if x == 0 and b < 0:
        logger.error("Power function failed: 0 to negative power", extra={"operation": "power", "base": x, "exponent": b})
        raise ZeroDivisionError('0.0 cannot be raised to a negative power')
    result = math.pow(x, b)
    logger.info("Power calculated", extra={"operation": "power", "base": x, "exponent": b, "result": result})
    return result

def main():
    while True:
        displayMenu()

        userInput = input()

        try:
            if userInput == '1':
                x = float(input('Enter a value for x:'))
                y = squareRoot(x)
                print(f'Result: {y}')
            
            elif userInput == '2':
                x = int(input('Enter a value for x:'))
                y = factorial(x)
                print(f'Result: {y}')
            
            elif userInput == '3':
                x = float(input('Enter a value for x:'))
                y = naturalLogarithm(x)
                print(f'Result: {y}')
            
            elif userInput == '4':
                x = float(input('Enter a value for x:'))
                b = float(input('Enter a value for b:'))
                y = powerFunction(x, b)
                print(f'Result: {y}')

            elif userInput == '5':
                print('Exiting.')
                break
            
            else:
                print('Invalid input. Please try again.')

        except ValueError as e:
            print(f'Input error: {e}. Please try again.')

        except Exception as e:
            print(f'Error: {e}. Please try again.')
        

if __name__ == '__main__':
    main()
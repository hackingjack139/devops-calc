import math

def displayMenu():
    print('Select an option:')
    print('1: Square root function - √x')
    print('2: Factorial function - x!')
    print('3: Natural logarithm (base е) - ln(x)')
    print('4: Power function - x^b')
    print('5: Exit')

def squareRoot(x):
    if x < 0:
        raise ValueError('Square root for negative numbers is not defined')
    else:
        return math.sqrt(x)

def factorial(x):
    if x < 0:
        raise ValueError('Factorial for negative numbers is not defined')
    else:
        return math.factorial(x)
    
def naturalLogarithm(x):
    if x <= 0:
        raise ValueError('Natural logarithm for numbers less than or equal to 0 is not defined')
    else:
        return math.log(x)

def powerFunction(x, b):
    return math.pow(x, b)

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
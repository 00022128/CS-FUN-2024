import math

def sqrt():
    try:
        a = float(input("Enter a number: "))
        if a < 0:
            print("Error! Unable to compute the square root of a negative number.")
        else:
            sqrt_result = math.sqrt(a)
            print(f'sqrt of {a} = {sqrt_result:.2}')

    except ValueError:
        print("Invalid input. Please enter numbers")

sqrt()
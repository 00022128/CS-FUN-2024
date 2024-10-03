# Function definition
def power(a,b):
    return f'{a} ** {b} = {pow(a, b)}'

# Direct function call
print(power(2,3))

# Variable call
x = 3
y = 5
print(power(x,y))

# Expression call
print(power(2 + 1, 2 * 3))
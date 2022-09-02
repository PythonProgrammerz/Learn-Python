# SQUARE
def squarenum():
    x = float(input("Enter a number: "))
    print("The square is ",square(x))

def square(n):
    return n * n

# CUBE
def cubenum():
    x = float(input("Enter a number: "))
    print("The cube is ",cube(x))

def cube(n):
    return n * n * n

#Power
def powernum():
    x = float(input("Enter a number: "))
    y = float(input("Enter a exponent: "))
    print("The power is ",power(x,y))

def power(x,y):
    return pow(x,y)

# Now using are own function
squarenum()
cubenum()
powernum()
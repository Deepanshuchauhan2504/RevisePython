
import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def square(a):
    return a ** 2

def square_root(a):
    return math.sqrt(a)

def remainder(a, b):
    return a % b

def main():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /, ^, sqrt, %): ")

    match op:
        case '+':
            print(f"{a} + {b} = {add(a, b)}")

        case '-':
            print(f"{a} - {b} = {sub(a, b)}")

        case '*':
            print(f"{a} * {b} = {mul(a, b)}")

        case '/':
            print(f"{a} / {b} = {div(a, b)}")

        case '^':
            print(f"Square of {a} = {square(a)}")

        case 'sqrt':
            if a < 0:
                print("Cannot calculate square root of a negative number")
            else:
                print(f"Square root of {a} = {square_root(a)}")

        case '%':
            if b == 0:
                print("Cannot calculate remainder with zero")
            else:
                print(f"{a} % {b} = {remainder(a, b)}")

        case _:
            print("Invalid operation")

if __name__ == '__main__':
    main()

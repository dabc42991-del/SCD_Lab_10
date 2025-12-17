def add(a, b):
    return a + b

print("Sum:", add(5, 3))

'''updated code with exception'''
def divide(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return num1 / num2
'''usage example'''
try:
    result = divide(10, 0)
    print(result)
except ZeroDivisionError as e:
    print(e)

def multiply(a, b):
    return a * b

print("Multiplication:", multiply(2, 3))

def subtract(a, b):
    return a - b

print("Difference:", subtract(10, 4))

def mod(a, b):
    if b == 0:
        raise ZeroDivisionError("Modulo by zero is not allowed")
    return a % b

print("Modulus:", mod(10, 3))



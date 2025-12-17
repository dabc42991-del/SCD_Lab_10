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

def subtract(a, b, absolute=False):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers (int or float).")

    result = a - b

    if absolute:
        return abs(result)

    return result


try:
    print("Difference:", subtract(10, 4))
    print("Absolute Difference:", subtract(4, 10, absolute=True))
except TypeError as error:
    print("Error:", error)


def mod(a, b):
    if b == 0:
        raise ZeroDivisionError("Modulo by zero is not allowed")
    return a % b

print("Modulus:", mod(10, 3))




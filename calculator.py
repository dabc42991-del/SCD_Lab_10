def add(a, b):
    return a + b

print("Sum:", add(5, 3))

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

print("Division:", divide(10, 2))

def multiply(a, b):
    return a * b

print("Multiplication:", multiply(2, 3))

def subtract(a, b):
    return a - b

print("Difference:", subtract(10, 4))

def mod(a, b):
    if b != 0:
        return a % b
    else:
        return "Error: Division by zero"

print("Modulus:", mod(10, 3))

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

num = int(input("Enter your number: "))
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if num == 1:
    print(add(a, b))
elif num == 2:
    print(subtract(a, b))
elif num == 3:
    print(multiply(a, b))
elif num == 4:
    print(divide(a, b))
else:
    print("Invalid choice")

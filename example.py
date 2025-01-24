# Function for addition
def add(a, b):
    return a + b

# Function for subtraction
def substractiion(a, b):
    return a - b


# Function for division
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed!"

# Main program
print("Basic Arithmetic Operations")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("\nResults:")
print(f"Addition: {add(num1, num2)}")
print(f"Subtraction: {subtract(num1, num2)}")
print(f"Multiplication: {multiply(num1, num2)}")
print(f"Division: {divide(num1, num2)}")

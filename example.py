# Function for addition
def add(a, b):
    return a + b

# Function for subtraction
def substractiion(a, b):
    return a - b
#### Marie please create again the multiplication function here...

# Function for division
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed!"

##### Laura please create a pow function and print it.

# Main program ##### Paco please change the print down here for a different and creative text.
print("Basic Arithmetic Operations")
print("Hello, How was your day?")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("\nResults:")
print(f"Addition: {add(num1, num2)}")
print(f"Subtraction: {subtract(num1, num2)}")
print(f"Multiplication: {multiply(num1, num2)}")
print(f"Division: {divide(num1, num2)}")

# add two numbers
def add(x, y):
    return x + y

# subtract two numbers
def subtract(x, y):
    return x - y

# multiply two numbers
def multiply(x, y):
    return x * y

# divide two numbers
def divide(x, y):
    if y == 0:
        return "Division by zero is not allowed."
    else:
        return x / y

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice(1-4):")

    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))

    if choice == '1':
        print(n1, "+", n2, "=", add(n1, n2))
    elif choice == '2':
        print(n1, "-", n2, "=", subtract(n1, n2))
    elif choice == '3':
        print(n1, "*", n2, "=", multiply(n1, n2))
    elif choice == '4':
        print(n1, "/", n2, "=", divide(n1, n2))
    else:
        print("Invalid input")

calculator()
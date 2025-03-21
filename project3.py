# project3.py

def greet(name):
    return f"Hello, {name}! Welcome to the Python world."

def add_numbers(a, b):
    return a + b

def main():
    name = input("Enter your name: ")
    print(greet(name))
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print(f"The sum of {num1} and {num2} is: {add_numbers(num1, num2)}")

if __name__ == "__main__":
    main()

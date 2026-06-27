# 1. Missing quotes in input()
# name = input(Enter your name)
# Output:
# SyntaxError: invalid syntax

# Correct
name = input("Enter your name: ")
print(name)

# 2. Missing quotes in print()
# print(Hello)
# Output:
# NameError: name 'Hello' is not defined

# Correct
print("Hello")

# 3. Missing closing bracket
# print("Welcome"
# Output:
# SyntaxError: '(' was never closed

# Correct
print("Welcome")

# 4. Adding string and integer
# age = input("Enter age: ")
# print(age + 5)
# Output:
# TypeError: can only concatenate str (not "int") to str

# Correct
age = int(input("Enter age: "))
print(age + 5)

# 5. Forgetting int() for numbers
a = input("Enter first number: ")
b = input("Enter second number: ")
print(a + b)
# Input:
# 10
# 20
# Output:
# 1020

# Correct
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a + b)
# Output:
# 30

# 6. Wrong function name
# Print("Python")
# Output:
# NameError: name 'Print' is not defined

# Correct
print("Python")

# 7. Wrong input function name
# Input("Enter: ")
# Output:
# NameError: name 'Input' is not defined

# Correct
input("Enter: ")

# 8. Printing undefined variable
# print(x)
# Output:
# NameError: name 'x' is not defined

# Correct
x = 100
print(x)
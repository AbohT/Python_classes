# A simple calculator app

print('''**********************
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exponetial
*******************''')
print("Addition")
print("Enter two numbers to add")
#prompt user for first number
first_number = float(input("First Number:"))
# prompt uswer to input second number
second_number = float(input("Second Number:"))
sum = first_number + second_number
print(f"{first_number} + {second_number} = {sum}")

print("*************************")
print('Subtraction')
print("Enter two numbers to subtract")
#prompt user for first number
first_number = float(input("First Number:"))
# prompt uswer to input second number
second_number = float(input("Second Number:"))
sub = first_number - second_number
print(f"{first_number} - {second_number} = {sub}")

print("**********************")
print('Multiplication')
print("Enter two numbers to multiply")
#prompt user for first number
first_number = float(input("First Number:"))
# prompt uswer to input second number
second_number = float(input("Second Number:"))
mul = first_number * second_number
print(f"{first_number} * {second_number} = {mul}")

print("**********************")
print("Enter two numbers to divide")
#prompt user for first number
first_number = input("First Number:")
# prompt uswer to input second number
second_number = input("Second Number:")
div = float(first_number) /  float(second_number)
print(f"{first_number} / {second_number} = {div}")
print("**********************")
print("Exponential")
first_number = input("First Number:")
second_number = input("Second Number:")
exp = float(first_number) **  float(second_number)
print(f"{first_number} ** {second_number} = {exp}")


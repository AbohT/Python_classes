# A simple calculator app

print('''**********************
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exponential
6. Floor division
*******************''')
print("Addition")
print("Enter two numbers to add")
#prompt user for first number
first_number = input("First Number:")
# prompt uswer to input second number
second_number = input("Second Number:")
sum = float(first_number) + float(second_number)
print(f"{first_number} + {second_number} = {sum:.2f}")

print("*************************")
print('Subtraction')
print("Enter two numbers to subtract")
#prompt user for first number
first_number = input("First Number:")
# prompt uswer to input second number
second_number = input("Second Number:")
sub = float(first_number) - float(second_number)
print(f"{first_number} - {second_number} = {sub:.2f}")

print("**********************")
print('Multiplication')
print("Enter two numbers to multiply")
#prompt user for first number
first_number = input("First Number:")
# prompt uswer to input second number
second_number = input("Second Number:")
mul = float(first_number) * float(second_number)
print(f"{first_number} * {second_number} = {mul:.2f}")

print("**********************")
print("Enter two numbers to divide")
#prompt user for first number
first_number = input("First Number:")
# prompt uswer to input second number
second_number = input("Second Number:")
div = float(first_number) /  float(second_number)
print(f"{first_number} / {second_number} = {div:.2f}")

print("**********************")
print("Exponential")
first_number = input("First Number:")
second_number = input("Second Number:")
exp = float(first_number) **  float(second_number)
print(f"{first_number} ** {second_number} = {exp:.2f}")

print("**********************")
print("Floor Division")
first_number = input("First Number:")
second_number = input("Second Number:")
floor_div = float(first_number) //  float(second_number)
print(f"{first_number} // {second_number} = {floor_div:.2f}")


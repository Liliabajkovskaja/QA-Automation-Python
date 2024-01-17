"""task 1
Write a program that can convert temperature from C to Fahrenheit and Kelvin
For example: the temperature in Celsius is 25 C
Fahrenheit: 77F - calculated by the formula C * 9/5 + 32
Kelvin: 298.16K - calculated by the formula C + 273.15
The user enters the temperature in degrees Celsius,
 the program outputs the temperature in Fahrenheit and Kelvin
while we will not check in any way whether the person entered a number or not,
so it is assumed that there will always be a number (int or float)"""

temperature_celsius = float(input("Please enter the temperature "))

temperature_fahrenheit = temperature_celsius * 9 / 5 + 32

temperature_kelvin = temperature_celsius + 273.15

print(f"temperature celsius: {temperature_celsius}C")
print(f"temperature fahrenheit: {temperature_fahrenheit}F")
print(f"temperature kelvin: {temperature_kelvin}K")

""""task 2
Write a calculator with the following operations: +, -, *, /
The user enters two numbers and an arithmetic operation
Remember that you cannot divide by 0 - the program must handle such a scenario and not crash
while we will not check in any way whether the person entered a number or not,
 so it is assumed that there will always be a number (int or float)"""

fist_number = float(input("Please enter number "))
second_number = float(input("Please enter number "))
operation = input("Please enter operation ")
if operation == "/" and second_number == 0:
    print("You cannot divide by zero ")
elif operation == "+":
    print(f"{fist_number} + {second_number} = {fist_number + second_number}")
elif operation == "-":
    print(f"{fist_number} - {second_number} = {fist_number - second_number}")
elif operation == "*":
    print(f"{fist_number} * {second_number} = {fist_number * second_number}")
elif operation == "/":
    print(f"{fist_number} / {second_number} = {fist_number / second_number}")

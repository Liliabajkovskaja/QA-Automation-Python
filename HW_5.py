"""1. Given a list str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
Create and print a dictionary of squares of these numbers using only map, lambda, zip (optional) functions
Expected result: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}"""

str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
fin_list = dict(map(lambda x: (int(x), int(x) ** 2), str_list))
print(fin_list)

""" 2. Write an interactive calculator. It assumes that the user enters a formula consisting of a number, 
an operator (at least * and /), and another number separated by a space (for example, 2 * 5).
If the input does not consist of three elements, generate and catch your own FormulaError exception.
If the second element is not "*" or "/", throw and catch your own WrongOperatorError exception
If the entered numbers cannot be floats, catch ValueError
Also catch the error when dividing by 0
For each error you catch, type an explanation of what went wrong
Provide three attempts to use the calculator, if the entered data is incorrect, 
if it does not work - print that the attempts are over
The result of the formula is a float number with two decimal places"""

#
# class FormulaError(Exception):
#     pass
#
#
# class WrongOperatorError(Exception):
#     pass
#
#
# counter_error = 3
#
# while counter_error > 0:
#     try:
#         user_input = input("Please enter your formula, in format 'number operator number' ")
#
#         elements = user_input.split()
#
#         num1, operator, num2 = elements
#
#         if len(elements) != 3:
#             raise FormulaError("Invalid input format.  Please use format 'number operator number' ")
#
#         num1 = float(num1)
#         num2 = float(num2)
#
#         if operator == '*':
#             result = num1 * num2
#         elif operator == '/':
#             if num2 == 0:
#                 raise ZeroDivisionError("Division by zero")
#             result = num1 / num2
#         else:
#             raise WrongOperatorError("Wrong operator please use '*' or '/'.")
#
#         print(f"Result: {result:.2f}")
#
#         break
#     except FormulaError as x:
#         print(f"FormulaError: {x}")
#     except WrongOperatorError as y:
#         print(f"WrongOperatorError: {y}")
#     except ValueError as z:
#         print(f"ValueError: {z}")
#     except ZeroDivisionError as c:
#         print(f"ZeroDivisionError: {c} ")
#     except Exception as e:
#         print(f"Error: {e}")
#     counter_error -= 1
#
# if counter_error == 0:
#     print("The attempts are over. Incorrect data entered three times.")

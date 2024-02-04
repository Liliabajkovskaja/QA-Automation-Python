""" 1.Write a script where
1) data will be read from the file
2) all workers in departments where expenses are less than profit will be increased by 10%
3) then write these (updated) data into a file named new_costs.json
That is, how it will look like:
I add a file with a fixed name to the folder (let it be departments.json)
I run the script
I receive a new new_costs.json file in the same folder, in which new salaries will be calculated
The old file is not changed"""

# import json
#
# file_path = 'departments.json'
#
# with open(file_path, 'r') as file:
#     data = json.load(file)
#
# print(data)
#
# for department in data['departments']:
#     expenses = department['expenses']
#     income = department['income']
#     id_department = department['id']
#     if expenses < income:
#         for employee in department['employees']:
#             employee['salary'] = int(employee['salary'] + employee['salary'] * 0.1)
# new_file_path = 'new_costs.json'
# with open(new_file_path, 'w') as new_file:
#     json.dump(data, new_file, indent=2)
#
# print("New file has created")

"""2. Create 2 functions
get_sum and print_table (names can be specified at your discretion)
1) get_sum calls print_table inside itself
2) get_sum takes 2 values: a number and the operation +,* (i.e. get_sum(num: int, operation:str) ) 
and returns the result of adding a number and the next 9 after it (i.e. the result of adding 10 digits)
3) print_table prints a table with the number and operation passed in get_sum from 1 to 10
assume that the user always enters the correct operation and number
Example of a call:
if __name__ == '__main__':
  print('sum is', get_sum(5, '*'))
Example output:
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50
sum is 95 # 5+6+7+8+9+10+11+12+13+14 = 95 """


def get_sum(number: int, operation: str):
    def print_table():
        i = 1
        while i <= 10:
            if operation == "*":
                print(f" {number} * {i} = {number * i}")
            elif operation == "/":
                result = number / i
                print(f"{number} / {i} = {result:.2f}")
            elif operation == "+":
                print(f" {number} + {i} = {number + i}")
            elif operation == "-":
                print(f" {number} - {i} = {number - i}")
            i += 1

    print_table()

    sum_numbers = 0

    for number in range(number, number + 10):
        sum_numbers += number

    print(f"Sum is {sum_numbers}")


if __name__ == '__main__':
    get_sum(5, "*")




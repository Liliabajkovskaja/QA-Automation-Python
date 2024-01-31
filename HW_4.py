"""
1.There are 3 groups of people (sets): australia_blacklist, poker_blacklist, alcohol_blacklist.
Names are indicated in each group. Display those who won the jackpot (in 3 lists at once)"""

# australia_blacklist = {"Nick", "Anna", "Bill", "Vova"}
# poker_blacklist = {"Anna", "Bob", "Charlie", "David", "Vova"}
# alcohol_blacklist = {"Vova", "Anna", "Frank", "Grace"}
#
# winners = australia_blacklist.intersection(poker_blacklist, alcohol_blacklist)
#
# print(f"Those who won the jackpot: {winners}")

"""2.The dictionary has the following data: {'Alex': 'house', 'Max': 'Flat', 'Olha': 'Appartments', 'Oleh': 'Trench'}
Using f-string output: "User_name is living in place_name" for each user. Use a loop"""

# dictionary = {
#     'Alex': 'House',
#     'Max': 'Flat',
#     'Olha': 'Appartments',
#     'Oleh': 'Trench'}
#
# for user in dictionary:
#     print(f"{user} is living in  {dictionary[user]}")

"""3.There is a list ['Jack', 'Leon', 'Alice', None, 32, 'Bob']
Output ONLY correct names (strings). Use Continue."""

# list_names = ['Jack', 'Leon', 'Alice', None, 32, 'Bob']
# correct_list_names = []
#
# for el in list_names:
#     if type(el) != str:
#         continue
#     correct_list_names.append(el)
# print(correct_list_names)

"""4.Count and print the number of letters in a line.
The user enters something (input)
Your task is to print the number of each character of what he entered."""

# user_input = input(f"Please enter some text ")
# if user_input == '':
#     print(f'You didn`t write anything. Program has stopped')
#     exit()
#
# letter_counts = {}
# for symbol in user_input:
#     if symbol.isalpha():
#         letter_counts[symbol] = letter_counts.get(symbol, 0) + 1
# print(letter_counts)

"""5.You create a list in which there may be None (or there may not be)
Purpose: Print "There is no None" if None is not found in the list
Conditions:
We go through the list in a cycle
Do not create variables (except for the list mentioned above)
use if 1 time
Do not use methods/functions/classes"""

# my_list = ['Bob', 'Kate', 'Vasyl', None, 3]
#
# found_none = False
#
# for el in my_list:
#     if el is None:
#         found_none = True
#         break
#
# if not found_none:
#     print('There is no None in my_list')

"""6. Solve task 4 without a dictionary in 2 terms:
1 line is input
The 2nd line is the decision."""

# user_input = input(f"Please enter some text ")
# [print(f"{k}: {user_input.count(k)}") for k in set(user_input) if k.isalpha()]

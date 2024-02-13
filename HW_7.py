"""1. Create a decorator that outputs the name of the called function to the console.
For example, create a pair of functions for the arithmetic operations of addition and multiplication.
When these functions are called, the result of the operation must be returned,
 and the name of the called function must be displayed on the console along with the result. Use __name__"""
#
# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Function name is: ", func.__name__)
#         result = func(*args, **kwargs)
#         return result
#
#     return wrapper
#
#
# @my_decorator
# def add_numbers(x, y):
#     print(f"{x} + {y} = {x + y}")
#     return x + y
#
#
# @my_decorator
# def multiplication_numbers(x, y):
#     print(f"{x} * {y} = {x * y}")
#     return x * y
#
#
# print()
# add_numbers(2, 3)
# print()
# multiplication_numbers(2, 4)


"""2.Create a function that can print the squares of even numbers from 0 to 1000000000 inclusive. 
The solution should work and not freeze the computer."""

# def get_squares_even(n):
#     for i in range(n + 1):
#         if i % 2 == 0:
#             yield i
#
#
# sequence = get_squares_even(1000000000)
#
# for num in sequence:
#     print(f"{num} squared is: {num ** 2}")


"""3. Create a decorator that returns the result of the function.
 and also prints the time for which it was completed. 
 Hint (to fix the time, import the time module: import time)"""

#
# import time
#
#
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"Time execution function - {func.__name__}: {round((end_time - start_time), 3)} sec.")
#         return result
#
#     return wrapper
#
#
# @timer
# def sleep_function():
#     time.sleep(2)
#
#
# sleep_function()


"""4.Create a function that will return a Fibonacci number, 
the function accepts a number in the Fibonacci sequence as input. 
Use recursion.
Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, ...
How the sequence is built: the first and second numbers are 0 and 1"""

# def get_fibonach(n):
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     return get_fibonach(n - 1) + get_fibonach(n - 2)
#
# if __name__ == '__main__':
#     print(get_fibonach(1))
#     print(get_fibonach(5))
#     print(get_fibonach(10))
#     print(get_fibonach(15))
#     print(get_fibonach(20))

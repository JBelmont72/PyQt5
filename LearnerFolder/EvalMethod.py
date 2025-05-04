from math import *
# https://www.geeksforgeeks.org/eval-in-python/
# def secret_function():
#     return "Secret key is 1234"

# def function_creator():

#     # expression to be evaluated
#     expr = input("Enter the function(in terms of x):")

#     # variable used in expression
#     x = float(input("Enter the value of x:"))

#     # passing variable x in safe dictionary
#     safe_dict['x'] = x

#     # evaluating expression
#     y = eval(expr, {}, safe_dict)

#     # printing evaluated result
#     print("y = {}".format(y))


# if __name__ == "__main__":

#     # list of safe methods
#     safe_list = ['acos', 'asin', 'atan', 'atan2', 'ceil', 'cos',
#                  'cosh', 'degrees', 'e', 'exp', 'fabs', 'floor',
#                  'fmod', 'frexp', 'hypot', 'ldexp', 'log', 'log10',
#                  'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt',
#                  'tan', 'tanh']

#     # creating a dictionary of safe methods
#     safe_dict = {}
#     for safe_key in safe_list:
#         safe_dict[safe_key] = locals().get(safe_key)
#         print(f"Added safe method: {safe_key}")
#     print(safe_dict)
#     # adding secret function to the safe dictionary
#     safe_dict['secret_function'] = secret_function
#     print("Added secret function: secret_function")
#     # creating function
#     print("Creating function...")
#     print("You can use the following safe methods:")
#     print(safe_list)
#     print("You can also use the secret function: secret_function()")
#     print("Enter your function in terms of x, e.g., 'sin(x) + cos(x)'")
#     print("You can use 'x' as a variable in your function.")
#     # calling function creator

#     function_creator()

# safe_list = ['acos',1, 'asin',2, 'atan', 3,'atan2',4, 'ceil', 'cos']
# safe_dict = {}
# for safe_key in safe_list:
#     safe_dict[safe_key] = locals().get(safe_key)
# print(safe_dict)
# print(safe_dict['acos'](0.5))  # Example usage of a safe method
# print(safe_dict['asin'](0.5))  # Example usage of another safe method
# print(safe_dict['atan'](1))    # Example usage of another safe method

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)
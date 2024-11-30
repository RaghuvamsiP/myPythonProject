# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.



# Creating a Function
# ways to create a function
# 1. function doesn't take arguments and not return any value (None)
# 2. function doesn't take arguments but return some value
# 3. function take arguments but no return value
# 4. function  take arguments and also return  value


# def my_function():
#     print("Hello from a function")

# Calling a Function
# def my_function():
#     print("Hello from a function")
#
#
# my_function()

"""Arguments"""

# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses.
# You can add as many arguments as you want, just separate them with a comma.

# def my_function(name):
#     print("Hello", name)
#
#
# my_function("Raghu")
# my_function("Vamsi")

"""Parameters or Arguments?"""


# The terms parameter and argument can be used for the same thing: information that are passed into a function.
# From a function's perspective:
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.

# Passing number of arguments
# def my_function(fname, lname):
#     print(fname + " " + lname)
#
#
# my_function("Raghu", "Vamsi")


# Return
# def cal(a, b):
#     return a+b
#
#
# # sum = cal(10, 20)
# # print(sum)
# # or
# print(cal(10,20))

# Return None
# def fun():
#     return
#
#
# print(fun())


# Print instead of return
def function(a, b):
    print(a + b)


function(100, 200)


# # num1 = 10
# # num2 = int(input("number2 "))
# #
# # total = num1 + num2
# # print(total)
# def sumOf2Numbers(num2):
#     return 10 + num2
#
#
# result = sumOf2Numbers(5)
# print(result)
# # or
# # print(sumOf2Numbers(num2=20))
#

import math

# def triangle(a, b, c):
#     s = (a + b + c) / 2
#     # print(s)
#     # area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
#     # area2 = math.sqrt(187500000)
#     # area3 = (150 * 50 * 50 * 50) ** 0.5
#
#     return (s * (s - a) * (s - b) * (s - c)) ** 0.5
#     # print(int(area))
#     # print(int(area2))
#     # print(int(area3))
#
#
# def triangle_gpt(a, b, c):
#     s = (a + b + c) / 2  # Calculate the semi-perimeter of the triangle
#     area = (s * (s - a) * (s - b) * (s - c)) ** 0.5  # Calculate the area using Heron's formula
#     return area


# print(triangle_gpt(a=100, b=100, c=100))

# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module
import cmath
import math

# a = 10
# b = 5
# c = 1

# # calculate the discriminant
# d = ((b ** 2) - (4 * a * c)) * -1
#
# print(math.sqrt(d))
# # # find two solutions
# sol1 = (-b - cmath.sqrt(d)) / (2 * a)
# sol2 = (-b + cmath.sqrt(d)) / (2 * a)
#
# print(sol1, sol2)

""" """
p = 10
q = 5
p = p + q
print(p)
p = p - q
print(p)
p = p * q
print(p)
p = p / q  # float
print(p)
p = p // q  # int
print(p)

abc = 2.5
pqr = -2

sqrt = abc ** pqr
print(f"Result {sqrt}")

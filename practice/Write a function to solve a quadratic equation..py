# import complex math module
import cmath
import math


def qtr_eq(a, b, c):
    # calculate the discriminant
    d = ((b ** 2) - (4 * a * c))

    print(math.sqrt(d))
    # # find two solutions
    sol1 = (-b - cmath.sqrt(d)) / (2 * a)
    sol2 = (-b + cmath.sqrt(d)) / (2 * a)

    return sol1, sol2


print(qtr_eq(1, 6, 4))

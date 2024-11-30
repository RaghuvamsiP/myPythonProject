# range() function in pythin
print(list(range(10)))  # 0 to 9 (last value will be excluded in range)
print(list(range(0, 10)))  # 0 to 9
# print only odd numbers b/w 1-10
print(list(range(1, 10, 2)))  # 1 starting point, 10 ending point, 2 increment
# print only even numbers b/w 1-10
print(list(range(2, 10, 2)))

print(list(range(10, 0, -1)))
print(list(range(-10, -5)))
print(list(range(-10, -2, 2)))
print(list(range(-10, -2, -3)))  # empty list


# slicing
a = '0123'
print(a[0:4])
print(a[0:4:2])

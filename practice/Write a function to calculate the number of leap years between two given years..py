# def count_leap_years(start_year, end_year):
#     leaf_year_count = 0
#     not_leaf_year_count = 0
#
#     for i in range(start_year, end_year + 1):
#         if (i % 400 == 0) and (i % 100 == 0):
#             print(i)
#             leaf_year_count = leaf_year_count + 1
#             print(leaf_year_count)
#         elif (i % 4 == 0) and (i % 100 != 0):
#             print(i)
#             leaf_year_count = leaf_year_count + 1
#             print(leaf_year_count)
#         else:
#             print(i)
#             not_leaf_year_count = not_leaf_year_count + 1
#
#     return leaf_year_count, not_leaf_year_count
#
#
# print(count_leap_years(2000, 2020))


# def count_leap_years(start_year, end_year):
#     res = 0
#
#     for i in range(start_year, end_year + 1):
#         if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
#             res += 1
#             print("if", i)
#         else:
#             print("else", i)
#
#     return res
#
#
# print(count_leap_years(2000, 2020))
#
# a = 0
# b = 10
# if a and b > 0:
#     print(True)


n = int(input(2))
while n > 0:
    if n % 2 == 0:
        print("even")
    else:
        print("odd")
    n = n - 1

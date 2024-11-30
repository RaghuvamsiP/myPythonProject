# Program to Check Leap Year
year = 2000

if (year % 400 == 0) and (year % 100 == 0):
    print(f"{year} is a leap year")
elif (year % 4 == 0) and (year % 100 != 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


# using function
# def lead_year(year):
#     if (year % 400 == 0) and (year % 100 == 0):
#         return "Leap Year"
#     elif (year % 4 == 0) and (year % 100 != 0):
#         return "Leap Year"
#     else:
#         return "Not Year"
#
#
# print(lead_year(2032))


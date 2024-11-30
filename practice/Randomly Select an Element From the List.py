# Using random module
# import random
#
# my_list = [1, 'a', 32, 'c', 'd', 31]
# print(random.choice(my_list))

# Using secrets module
# import secrets
#
# my_list = [1, 'a', 32, 'c', 'd', 31]
# rand = secrets.choice(my_list)
# print(rand)


# Converting Kilometers to Miles
# oneKm = 1
# oneMile = 1.6
# conv = float(oneKm / oneMile)
# print(conv)
# kms = int(input("enter kilometers: "))
# Miles = kms / conv
# print(Miles)


# Converting kilometers into miles ny using function
# def miles(kms):
#     conv = 0.625
#     return kms / conv
#     print(kms)
#
#
# print(miles(kms=100))

#  Convert Celsius To Fahrenheit: fahrenheit = celsius * 1.8 + 32
# def Fahrenheit(celsius):
#     return celsius * 1.8 + 32
#
#
# print(int(Fahrenheit(10)))


#  Convert Fahrenheit To celsius: celsius = (fahrenheit - 32) / 1.8
def celsius(fahrenheit):
    return (fahrenheit - 1.8) + 32


print(int(celsius(10)))

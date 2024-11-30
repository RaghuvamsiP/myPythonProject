# Program to generate a random number between 0 and 9

# importing the random module
import random


# print(random.randint(0, 9))
#
# # learn 1
# for i in range(10):
#     print(random.randint(0, 9))

# print(random.random())  # it will generate some random number, It may me float or int
# print(random.randrange(1, 10))

# experiment
def alter(num):
    num = num + 10
    return num


num = 10

print(num)
num = alter(num)
print(num)


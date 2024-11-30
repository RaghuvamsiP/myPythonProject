# Tuple is a collection which is ordered and unchangeable
# Tuple is immutable
# Tuples are written with round brackets ()

# Example 1: creating tuple

mytuple = ("apple", "banana", "cherry")
mytuple01 = (1243, "banana", "90", 10.56, 100)
mytuple02 = ()  # empty tuple
print(mytuple)

# Example 2: access tuple items

mytuple = ("apple", "banana", "cherry")
print(mytuple[1])
print(mytuple[-1])

# Example 3: range of indexes

mytuple3 = ("apple", "banana", "cherry", "mango", "kiwi", "grape")
print(mytuple3[2:5])
print(mytuple3[-5:-1])

# Example 4: changing tuple items

# By default doesn't allow to change the values bcz it is immutable
# But there work around
# tuple--> list--> tuple
mytuple4 = ("apple", "banana", "cherry", "mango", "kiwi", "grape")

mylist = list(mytuple4)
print(mylist)
# now we can modify the list and later we convert  into tuple
mylist[0] = "papaya"
print(mylist)

mytuple4 = tuple(mylist)
print(mytuple4)

# Example 5: reading tuple items using loop

mytuple5 = ("apple", "banana", "cherry", "mango", "kiwi", "grape")
for i in mytuple5:
    print(mytuple5)

# or
thisTuple = ("apple", "banana", "cherry")
for i in range(len(thisTuple)):
    print(thisTuple[i])

# Example 6: check item is existed or search the item

mytuple6 = ("apple", "banana", "cherry", "mango", "kiwi", "grape")
if "kiwi" in mytuple5:
    print("kiwi existed")
else:
    print("kiwi not in the tuple")

# Example 7: count the items in a tuple
mytuple7 = ("apple", "banana", "cherry", "mango", "kiwi", "grape")
print(len(mytuple7))

# Example 8: add items into tuple : not possible bcz tuple is immutable - cannot change the items

# Example 9: copy tuple
mytuple9_a = ("apple", "banana", "cherry")
mytuple9_b = mytuple9_a
# or
mytuple9_c = tuple(mytuple9_a)

print(mytuple9_b)
print(mytuple9_c)

# # Example 10: del tuple
# mytuple10 = ("apple", "banana", "cherry", "mango", "kiwi", "grape")
# del mytuple10
# print(mytuple10)

# Example 11: Joining tuples
mytuple11_a = ("apple", "banana", "cherry")
mytuple11_b = ("mango", "kiwi", "grape")
mytuple11_c = mytuple11_a + mytuple11_b
print(mytuple11_c)

# Example 12: compare tuples
mytuple11_a = ("apple", "banana", "cherry")
mytuple11_b = ("mango", "kiwi", "grape")
if mytuple9_a == mytuple11_b:
    print("tuples are same")
else:
    print("tuples are not same")

# Example 13: Multiply Tuples

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)

# Tuple Methods
"""
Method	Description
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found"""
# count()
fruits = ("apple", "banana", "cherry", "apple", "apple")
num = fruits.count("apple")
print(num)

# index()
fruits = ("apple", "banana", "cherry")
num = fruits.index("apple")
print(num)

# Packing and packing a Tuple

# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
# fruits = ("apple", "banana", "cherry")
# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
# Unpacking a tuple:
# fruits = ("apple", "banana", "cherry")
# (green, yellow, red) = fruits
# print(green)
# print(yellow)
# print(red)
# Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.

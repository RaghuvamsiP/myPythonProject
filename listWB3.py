"""Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.(mutable)
Tuple is a collection which is ordered and unchangeable. Allows duplicate members. (immutable)
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members."""
from typing import List

# Allow duplicates
# thisList = ["apple", "banana", "cherry", "apple", "cherry"]
# print(thisList)

# List Length
# thisList = ["apple", "banana", "cherry"]
# print(len(thisList))

# List Items - Data Types
# list1 = ["apple", "banana", "cherry"]
# list2 = [1, 5, 7, 9, 3]
# list3 = [True, False, False]

# # A list can contain different data types:
# list1 = ["abc", 34, True, 40, "male"]
# print(list1)

# # type()
# # From Python's perspective, lists are defined as objects with the data type 'list':
# myList = ["apple", "banana", "cherry"]
# print(type(myList))

# The list() Constructor
# It is also possible to use the list() constructor when creating a new list.
# thisList = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thisList)

# Access Items
# List items are indexed and you can access them by referring to the index number:
# thisList = ["apple", "banana", "cherry"]
# print(thisList[1])
# The first item has index 0.

# # Negative Indexing
# # Negative indexing means start from the end
# # -1 refers to the last item, -2 refers to the second last item etc.
# thisList = ["apple", "banana", "cherry"]
# print(thisList[-1])

# # Range of Indexes
# # You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new list with the specified items.
# thisList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# thisList2 = thisList[2:5]
# print(thisList2)  # Note: The search will start at index 2 (included) and end at index 5 (not included).

# # By leaving out the start value, the range will start at the first item:
# thisList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thisList[:4])

# By leaving out the end value, the range will go on to the end of the list:
# thisList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thisList[0:])


# Range of Negative Indexes
# This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
# thisList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thisList[-4:-1])

# Check if Item Exists
# To determine if a specified item is present in a list use the in keyword:
# thisList = ["apple", "banana", "cherry"]
# if "apple" in thisList:
#     print("Yes, 'apple' is in the fruits list")
# else:
#     print("No, 'apple' is not in the fruits list")

# Change Item Value
# To change the value of a specific item, refer to the index number:
# thisList = ["apple", "banana", "cherry"]
# thisList[1] = "blackcurrant"
# print(thisList)

# Change a Range of Item Values
"""To change the value of items within a specific range, 
define a list with the new values, and refer to the range of index numbers where you want to insert the new values:"""

# thisList = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thisList[1:3] = ["blackcurrant", "watermelon"]
# print(thisList)

"""If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:"""
# thisList = ["apple", "banana", "cherry"]
# thisList[1:2] = ["blackcurrant", "watermelon"]
# print(thisList)
#  Note: The length of the list will change when the number of items inserted does not match the number of items replaced.

"""If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:"""
# thisList = ["apple", "banana", "cherry"]
# thisList[1:3] = ["watermelon"]
# print(thisList)

# Insert Items
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.
# The insert() method inserts an item at the specified index:
# thisList = ["apple", "banana", "cherry"]
# thisList.insert(2, "watermelon")
# print(thisList)


# # Python - Add List Items

# To add an item to the end of the list, use the append() method:
# thisList = ["apple", "banana", "cherry"]
# thisList.append("orange")
# print(thisList)

# Extend List
# To append elements from another list to the current list, use the extend() method.
# thisList = ["apple", "banana", "cherry"]
# thisList2 = ["mango", "pineapple", "papaya"]
# thisList.extend(thisList2)
# print(thisList)

# Add Any Iterable
"""The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.)."""
# Example
# thisList = ["apple", "banana", "cherry"]
# thisTuple = ("kiwi", "orange")
# thisList.extend(thisTuple)
# print(thisList)


# Remove List Items

# The remove() method removes the specified item.
# thisList = ["apple", "banana", "cherry"]
# thisList.remove("banana")
# print(thisList)

"""If there are more than one item with the specified value, the remove() method removes the first occurrence:"""
# thisList = ["apple", "banana", "cherry", "banana", "kiwi"]
# thisList.remove("banana")
# print(thisList)

# Remove Specified Index
# The pop() method removes the specified index.
# thisList = ["apple", "banana", "cherry"]
# thisList.pop(1)
# print(thisList)
"""If you do not specify the index, the pop() method removes the last item."""
# thisList = ["apple", "banana", "cherry"]
# thisList.pop()
# print(thisList)

# Delete
# The del keyword also removes the specified index:
# thisList = ["apple", "banana", "cherry"]
# del thisList[0]
# print(thisList)

"""The del keyword can also delete the list completely."""
# thisList = ["apple", "banana", "cherry"]
# del thisList

# Clear the List
# The clear() method empties the list.
# The list still remains, but it has no content.
# thisList = ["apple", "banana", "cherry"]
# thisList.clear()
# print(thisList)

# Python - Loop Lists

# Loop Through a List
# thisList = ["apple", "banana", "cherry"]
# for x in thisList:
#     print(x)

# Loop Through the Index Numbers
# Use the range() and len() functions to create a suitable iterable.
# thisList = ["apple", "banana", "cherry"]
# for i in range(len(thisList)):
#     print(thisList[i])

# Using a While Loop

# thisList = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thisList):
#     print(thisList[i])
#     i = i + 1

# ###Python - List Comprehension---> Will check later

# Python - Sort Lists
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
#
# thisList = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thisList.sort()
# print(thisList)

# Sort Descending
# To sort descending, use the keyword argument reverse = True:
# thisList = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thisList.sort(reverse=True)
# print(thisList)

"""Perform a case-insensitive sort of the list"""
# thisList = ["banana", "Orange", "Kiwi", "cherry"]
# thisList.sort(key=str.lower)
# print(thisList)

# Reverse Order
# What if you want to reverse the order of a list, regardless of the alphabet?
# The reverse() method reverses the current sorting order of the elements.
# thisList = ["banana", "Orange", "Kiwi", "cherry"]
# thisList.reverse()
# print(thisList)


# Copy a List
# Ex 1:
# thisList = ["apple", "banana", "cherry"]
# myList = thisList.copy()
# print(myList)
#
# # Ex 2:
# thisList = ["apple", "banana", "cherry"]
# myList = list(thisList)
# print(myList)


# Join Two Lists
# Ex1:
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# list3 = list1 + list2
# print(list3)

# Ex2:
# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]
# for x in list2:
#   list1.append(x)
#
# print(list1)

# Ex3:
# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]
# list1.extend(list2)
# print(list1)



# List Methods
"""
Method	    Description
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()   	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list """




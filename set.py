# set is a collection which is unordered/Unindexed & Unique Elements (do not allow duplicate elements)
# sets are written with curly brackets {}
# set is mutable

# # Example 1: Create a tuple
# mySet = {"apple", "banana", "cherry"}
# mySet01 = {}
#  print(mySet)
# print(mySet01)

# Example 2: Accessing items from the set
# mySet = {"apple", "banana", "cherry"}
# for i in mySet:
#     print(i)  # we cant extract specific value from the set since the values position is not constant

# Example 3: values exist in set or not
# mySet = {"apple", "banana", "cherry"}
# print("banana" in mySet)
# print("mango" in mySet)
# or
# if "banana" in mySet:
#     print("Yes, Banana exist")
# else:
#     print("No!")

# Example 4: adding items to set

# add() we can add only single item
# mySet = {"apple", "banana", "cherry"}
# mySet.add("kiwi")
# print(mySet)

# update() we can add multiple items

# mySet = {"apple", "banana", "cherry"}
# mySet.update(["berry", "grape", "papaya"])
# mySet.update(["Orange"])
# print(mySet)
#
# mySet1 = {"apple", "banana", "cherry"}
# mySet1.update("Orange")  # it will iterate each index of the string
# print(mySet1)

# Example 5: length of set

# mySet = {"apple", "banana", "cherry"}
# print(len(mySet))

# Example 6: remove item from set
# Method 1
# mySet = {"apple", "banana", "cherry"}
# mySet.remove("banana")
# mySet.remove("xyz") # It will give keyError
# print(mySet)
# Method 2
# mySet = {"apple", "banana", "cherry"}
# mySet.discard("apple")
# print(mySet)
# mySet.discard("xyz")  # It will not give any

# Example 7: clear all items from the set

# mySet = {"apple", "banana", "cherry"}
# mySet.clear()
# print(mySet)  # will return empty set
# del mySet  # it will delete entire set

# Example 8: Joining 2 sets  # we can't join 2 sets by concatenating

# mySet1 = {"apple", "banana", "cherry"}
# mySet2 = {1, 2, 3}
# mySet1.update(mySet2)
# print(mySet1)

# mySet1 = {"apple", "banana", "cherry"}
# mySet2 = {"abc", "xyz", "PQR"}
# mySet3 = mySet1.union(mySet2)
# print(mySet3)

# Use | to join two sets:

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = set1 | set2
# print(set3)


# Join Multiple Sets
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}
#
# mySet = set1.union(set2, set3, set4)
# print(mySet)

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}

# mySet = set1 | set2 | set3 | set4
# print(mySet)

# Join a Set and a Tuple
# x = {"a", "b", "c"}
# y = (1, 2, 3)
# z = x.union(y)
# print(z)


# Example 9: Intersection > ONLY the duplicates values

# Join set1 and set2, but keep only the duplicates:

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.intersection(set2)
# print(set3)  # apple

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1 & set2
# print(set3)
"""Note: The & operator only allows you to join sets with sets,
and not with other data types like you can with the intersection() method."""

"""The intersection_update() method will also keep ONLY the duplicates,
 but it will change the original set instead of returning a new set."""
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set1.intersection_update(set2)
# print(set1)

"""The values True and 1 are considered the same value. The same goes for False and 0."""
# set1 = {"apple", 1,  "banana", 0, "cherry"}
# set2 = {False, "google", 1, "apple", 2, True}
# set3 = set1.intersection(set2)
# print(set3)


# Example 10: Difference
"""The difference() method will return a new set that will contain only the items 
from the first set that are not present in the other set."""

# set1 = {"apple", "banana", "cherry", "Green apple", 'KIWI'}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.difference(set2)
# print(set3)

"""You can use the - operator instead of the difference() method,
 and you will get the same result."""
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1 - set2
# print(set3)

"""Note: The - operator only allows you to join sets with sets, and not with other data types like you can with the difference() method."""

"""The difference_update() method will also keep the items from the first set that are not in the other set,
 but it will change the original set instead of returning a new set."""
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set1.difference_update(set2)
# print(set1)


# Example 11: Symmetric Differences

"""The symmetric_difference() method will keep only 
the elements that are NOT present in both sets."""
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.symmetric_difference(set2)
# print(set3)

"""You can use the ^ operator instead of the symmetric_difference() method,
 and you will get the same result."""
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1 ^ set2
# print(set3)

"""Note: The ^ operator only allows you to join sets with sets, 
and not with other data types like you can with the symmetric_difference() method."""

"""The symmetric_difference_update() method will also keep all but the duplicates, 
but it will change the original set instead of returning a new set."""
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set1.symmetric_difference_update(set2)
# print(set1)

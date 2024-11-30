# A dictionary is a collection which is ordered, changeable (mutable) , indexed and Duplicates Not Allowed
# These are written in curly brackets, and they have keys & values

# Example 1: Create dictionary

# thisDict = {"brand": "Ford", "model": "Mustang", "year": 1964,}
# print(thisDict)
# print(thisDict["brand"])

# # Duplicates Not Allowed
# thisDict = {"brand": "Ford", "model": "Mustang", "year": 1964, "year": 2020}
# print(thisDict)  # Duplicate values will overwrite existing values:

# Example 2: Accessing Items

# thisDict = {"brand": "Ford", "model": "Mustang", "year": 1964}
# print(thisDict["brand"])
#
# # or
#
# thisDict = {"brand": "Ford", "model": "Mustang", "year": 1964}
# x = thisDict.get("brand")
# print(x)

# How get only keys & values
# thisDict = {"brand": "Ford", "model": "Mustang", "year": 1964}
# print(thisDict.keys())
# print(thisDict.values())
# print(thisDict.items())


# Example 3: change values in dictionary
# thisDict = {"brand": "Ford", "model": "Mustang", "year": 1964}
# print(thisDict)
# thisDict["year"] = 2024
# print(thisDict)

# Example 4: read items from dictionary using loop

# thisDict = {"brand": "Ford", "model": "Mustang", "year": 1964}
# for i in thisDict:
#     # print(i)  # It will return only keys
#     print(thisDict["brand"])
#     print(x)

# or

# thisDict = {"brand": "Ford", "model": "Mustang", "year": 1964}
# for i in thisDict:
#     print(thisDict[i])

# print keys along with the values
# thisDict = {"brand": "Ford", "model": "Mustang", "year": 1964}
# for x, y in thisDict.items():   # x,y are key and values
#     print(x, y)

# Example 5: Key is exist or not
# thisDict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# if "model" in thisDict:
#     print("Yes, 'model' is one of the keys in the thisDict dictionary")
# else:
#     print("No")
# or
# print("model" in thisDict)


# Example 6: find num of item in disc

# thisDict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# print(len(thisDict))

# Example 7: Adding items to disc

# thisDict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# thisDict["color"] = 'RED'
# print(thisDict)

# or

# thisDict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisDict.update({"year": 2020})
# print(thisDict)

# Example 8: remove item from disc
#
# thisDict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# thisDict.pop("year")
# print(thisDict)
# # or
# del thisDict["model"]
# print(thisDict)

# The popitem() method removes the last inserted item
# thisDict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisDict.popitem()
# print(thisDict)

# if we want to delete entire disc
# del thisDict
# thisDict.clear() # return empty disc

# Example 9: copy

# thisDict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = thisDict.copy()
# print(mydict)


# Make a copy of a dictionary with the dict() function:

# thisDict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = dict(thisDict)
# print(mydict)

# Without using any method
# thisDict1 = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
#
# thisDict2 = thisDict1
# print(thisDict2)


# Example 10 : nested dictionary

# A dictionary can contain dictionaries, this is called nested dictionaries.

# Ex1 : Create a dictionary that contain three dictionaries:
# myFamily = {
#     "child1": {
#         "name": "Emil",
#         "year": 2004
#     },
#     "child2": {
#         "name": "Tobias",
#         "year": 2007
#     },
#     "child3": {
#         "name": "Linus",
#         "year": 2011
#     }
# }
# print(myFamily)

# EX 2: Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
# child1 = {
#     "name": "Emil",
#     "year": 2004
# }
# child2 = {
#     "name": "Tobias",
#     "year": 2007
# }
# child3 = {
#     "name": "Linus",
#     "year": 2011
# }
#
# myFamily = {
#     "dic1": child1,
#     "dic2": child2,
#     "dic3": child3
# }
# print(myFamily)

# Access Items in Nested Dictionaries
# myFamily = {
#     "child1": {
#         "name": "Emil",
#         "year": 2004
#     },
#     "child2": {
#         "name": "Tobias",
#         "year": 2007
#     },
#     "child3": {
#         "name": "Linus",
#         "year": 2011
#     }
# }
#
# print(myFamily["child2"]["name"])



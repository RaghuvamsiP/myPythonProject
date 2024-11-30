# list is collection which is ordered and changeable
# List is mutable and allow duplicates
# lists are written with square brackets  []

# Example 1: How to create a list

mylist = []
mylist1 = [10, 30, 10.6, 26, 100]
mylist2 = ["apple", "banana", "cherry"]
mylist3 = ["python", "welcome", 10, 20.8, 'crazy']

print(mylist)
print(mylist1)
print(mylist2)
print(mylist3)

# Example 2: Accessing items from the list
mylist02 = ["python", "welcome", 10, 20.8, 'crazy']

print(mylist02[0])  # index
print(mylist02[2])
print(mylist02[-1])  # last item will be printed
print(mylist02[-3])

# Example 3: range of indexes
mylist03 = ["python", "welcome", 10, 20.8, 'crazy', "mango", "credit"]
print(mylist03[2:5])  # last values will excluded
print(mylist03[-5:-1])

# Example 4: change item value
mylist04 = ["python", "welcome", 10, 20.8, 'crazy', "mango", "credit"]
mylist04[2] = "orange" # this will change the values based on index
print(mylist04)  # ['python', 'welcome', 'orange', 20.8, 'crazy', 'mango', 'credit']

# Example 5: read the list items using loop
mylist05 = ["python", "welcome", 'crazy', "mango", "credit"]

for i in mylist05:
    print(i)

# Example 6: check if the item is exist in the list or not
mylist06 = ["python", "welcome", 'crazy', "mango", "credit"]

if "mango" in mylist06:
    print("mango is present")
else:
    print("mango is not present")

# Example 7: counting number of items in a list
mylist07 = ["python", "welcome", 'crazy', "mango", "credit"]

print(len(mylist07))

# Example 8: add items to list append () insert()
mylist08 = ["python", "welcome", 'crazy', "mango", "credit"]
mylist08.append("banana")  # new item will be added at the end of the list
print(mylist08)

mylist08.insert(4, "grape")  # we can add at any position by indexing
print(mylist08)

# Example 9: remove item from the list
mylist09 = ["python", "welcome", 'crazy', "mango", "credit"]
# remove
mylist09.remove("credit")
print(mylist09)
# pop()
mylist09.pop(1)
print(mylist09)

# del
del mylist09[0]
print(mylist09)

# clear
mylist09.clear()  # it will clear all the items
print(mylist09)

# Example 10: copy list
mylist_01 = ["python", "welcome", "mango", "credit"]
mylist_02 = list(mylist_01)
print(mylist_01)
print(mylist_02)

# Copy()
mylist_01 = ["python", "welcome", "mango", "credit"]
mylist_02 = mylist_01.copy()
print(mylist_01)
print(mylist_02)

# Example 11: combine or join lists
# 1 using + operator
list_a = [1, 2, 3]
list_b = ["a", "b", "c"]
list_c = list_a + list_b
print(list_c)

# 2 using looping
list_a = [1, 2, 3]
list_b = ["a", "b", "c"]
for i in list_b:
    list_a.append(i)
print(list_a)

# 3 using extend()
list_a = [1, 2, 3]
list_b = ["a", "b", "c"]
list_a.extend(list_b)
print(list_a)

# Example 11: compare lists

list_a = [1, 2, 3]
list_b = ["a", "b", "c"]
if list_a == list_b:
    print("both lists are same")
else:
    print("both lists are not same")


























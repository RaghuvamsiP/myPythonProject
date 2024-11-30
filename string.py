# # ways to create string variables
#
# s = "welcome"
# s1 = 'welcome'
# s2 = str("welcome")
# s3 = str("welcome")
#
# #  Example 1: creating empty string variables
# name = ""
# name1 = ''
# name3 = str()
#
# #  Example 2
# # Mutable : Mutable data types are those whose values can be changed or new values can be assigned to them.
# # Immutable : which means they cannot be changed after they are created
# # A string is an immutable object which means we cannot change them after creating the objects. Whenever we change any string, a new instance (memory) is created.
#
# # string is immutable
# string = "welcome"
# print(id(string))
# string = string + "to python"
# print(id(string))
#
# # Example 3: + and * with string
#
# string = "welcome"
# print(string + ' to python')
# print(string * 2)
# # print(string + 8 ) # we cant cantact string with int
#
# # Example 4: slicing [start:stop:step]
#
# string = "welcome"
# print(string[1:5])  # 0=w,1=e,2=l,3=c,4=o,5=m,6=e Note: last value will be excluded
# print(string[:6])  # starting value is consider as 0
# print(string[3:])
# print(string[1:-1])  # -1 means, it will remove the last character in the string
# print(string[1:-2])  # -2 means, it will remove the last 2 characters in the string
#
# # Example 5 : ord() and chr() methods
#
# print(ord('Q'))  # It will return ASCII number , it case-sensitive
# print(chr(81))  # if we pass ASCII number, it will return respective character
#
# # Example 6 : max(), min(), len()
# fruit = 'banana'
# print(max(fruit))  # will return max character in a string
# print(min(fruit))  # will return min character in a string
# print(len(fruit))  # will return count of characters in a string
#
# # Example 7 : 'in' and 'not in' operators in a string--It will return boolean (true/false)
# fruit = 'banana'
# print('ban' in fruit)  # true
# print('cherry' in fruit)  # false
#
# print('cherry' not in fruit)  # true
# print('ban' not in fruit)  # false
#
# # Example 8 : String comparison --It will return boolean (true/false)
#
# print('tim' == 'tin')  # false
# print('tim' != 'tin')  # true
# print(
#     'mango' > 'mantra')  # it will compare each char from string 1 and string 2 from starting (g is not greater than t)
# print('right' >= 'left')
# print('teeth' < 'tee')
# print('yellow' <= 'fellow')
# print('abc' == '')
#
# # Example 9 : Testing strings --It will return true/false
# print('new line')
# st1 = 'welcome to python1'
# st2 = '2024A'
# st3 = '1234'
# st4 = 'python'
#
# """The method .isalnum() in Python checks whether all the characters in a string are alphanumeric (consist of only alphabetic characters (a-z, A-Z) and digits (0-9)) and if the string is not empty.
# Let's analyze the string 'welcome to python':
# The string contains spaces (' '), which are not alphanumeric characters.
# Alphanumeric characters include letters ('a'-'z', 'A'-'Z') and digits ('0'-'9').
# Since 'welcome to python' contains spaces, the method .isalnum() will return False because it expects all characters in the string to be alphanumeric.
# So, the output of print(st.isalnum()) will be: false"""
# print(st1.isalnum())  # false
# print(st2.isalnum())  # true
# print(st3.isalnum())  # true
# print(st4.isalnum())  # true
#
# """The .isalpha() method in Python checks whether all the characters in a string are alphabetic (consist of only alphabetic characters (a-z, A-Z)) and if the string is not empty."""
#
# print(st1.isalpha())  # false
# print(st2.isalpha())  # false
# print(st3.isalpha())  # false
# print(st4.isalpha())  # true
#
# """The .isdigit() method in Python checks whether all the characters in a string are digits (0-9) and if the string is not empty. It returns True if all characters are digits, otherwise False."""
# print(st1.isdigit())  # false
# print(st2.isdigit())  # false
# print(st3.isdigit())  # true
# print(st4.isdigit())  # false
#
# print(st1.islower())  # true
# print(st2.islower())  # false
# print(st3.islower())  # false
# print(st4.islower())  # true
#
# print(st1.isupper())  # false
# print(st2.isupper())  # true
# print(st3.isupper())  # false
# print(st4.isupper())  # false
#
# '''The .isspace() method in Python checks whether all the characters in a string are whitespace characters (spaces, tabs, newline characters, etc.) and if the string is not empty. It returns True if all characters are whitespace, otherwise False.'''
# print(st1.isspace())  # false
# print(st2.isspace())  # false
# print(st3.isspace())  # false
# print(st4.isspace())  # false
#
# print(st1.isidentifier())  # false
# print(st2.isidentifier())  # false
# print(st3.isidentifier())  # false
# print(st4.isidentifier())  # true
#
# # Example 10 : searching for sub string
#
# subString = 'welcome to python'
# print('searching for sub string')
# print(subString.endswith("Thon"))
# print(subString.endswith("thon"))
#
# print(subString.startswith("wel"))
# print(subString.startswith("come"))
#
# print(subString.find("wel"))  # it will return the position of sub string
# print(subString.find("come"))
# print(subString.find("to"))
#
# print(subString.find("well"))  # if  sub string is not available in the string then it will return -1
# print(subString.find("too"))
#
# print(subString.count("w"))  # it will return the count of the searching element
# print(subString.count("o"))
# print(subString.count("no element"))
#
# # Example 11 : string conversion
#
# stringEx = 'STRING in PYTHON. credit mantra'
# print('Example 11')
# stringEx1 = stringEx.capitalize()  # Only 1st char should be upper case
# print(stringEx1)
#
# stringEx2 = stringEx.title()  # all the starting char of a string will be in upper case
# print(stringEx2)
#
# stringEx3 = stringEx.lower()  # all the char will be in lower case
# print(stringEx3)
#
# stringEx4 = stringEx.upper()
# print(stringEx4)
#
# stringEx5 = stringEx.swapcase()
# print(stringEx5)
#
# stringEx6 = stringEx.replace("mantra", "repair cloud")
# print(stringEx6)
#
# # Example 11 : Reverse a string
# # Method 1
# c_name = "credit repair cloud"
# rev_c_name = ""
#
# for i in c_name:
#     rev_c_name = i + rev_c_name
#     rev_c_name = rev_c_name + i
# print(rev_c_name)
#
# # Method 2:  [start:stop:step]
#
# book_name = 'credit'  # credit = 012345
# rev_book_name = book_name[::-1]
# print(rev_book_name)

# rev_book_name = book_name[::1]
# print(rev_book_name) o/p= credit

# Method 3:
#
# book_name = 'credit'
# print(len(book_name))
# print(book_name[len(book_name)::-1])

#  -----------------
X = [1, 2, 3]
Y = "789"
X.extend(Y)  # it will iterate to each element of the string
print(X)





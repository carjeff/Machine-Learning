"""
Write a program in Python to prompt the user for two strings. Write logic to check if the second string is:
A prefix of the first string
A substring of the first string
A suffix of the first string
"""

str1 = str(input("please enter a string: "))
str2 = str(input("plesae enter anoter string: "))
if str1.startswith(str2):
    print(str2 + " is a prefix of the first string.")
elif str1.endswith(str2):
    print(str2 + " is a suffix of the first string.")
elif str2 in str1:
    print(str2 + " is a substring of the first string.")
else:
    print(str2 + " is not part of the first string")
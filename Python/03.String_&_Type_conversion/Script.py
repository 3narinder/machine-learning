# Strings: take extra space in memory because they are immutable. When we modify a string, a new string is created in memory, and the old string is discarded. This can lead to increased memory usage if we are performing many string operations.

# * It also save unicode value of string that's why it take some extra space.

# a ="A"
# print(ord(a))  # Output: 65 , string to unicode

# a =65
# print (chr(a))  # Output: A, unicode to string

# ? *** string Indexing **** 
# **Each character in a string has an index, starting from 0 for the first character. We can access individual characters using their index.

# user="John doe"

# print(user[0])  # Output: J, first character
# print(user[4])  # Output: o, fifth character, space is also counted as a character
# print(user[-1]) # Output: e, last character

# ? *** String Slicing ****
# **We can extract a substring from a string using slicing. The syntax is string[start:end:step], where start is the index of the first character to include, end is the index of the character to exclude, and step is the number of characters to skip.

# if i need end index of 4 i will add 4+1 =5 in end index because end index is exclusive.

# str = "hello world"
# print(str[0:5:1])

# no end index means it will go till the end of the string. The step value of 1 means it will include every character in the specified range. So, str[5::1] will return the substring starting from index 5 to the end of the string, which is " world".

# ? *** Type Conversion ****
# **Type conversion is the process of converting a value from one data type to another. In Python, we can use built-in functions like int(), float(), str(), etc. to perform type conversion.

# ** Explicit:  type conversion is when we manually convert a value from one data type to another using built-in functions. For example, we can convert a string to an integer using the int() function, or convert an integer to a string using the str() function.

# a="123"
# a = int(a)
# print(type(a))  # Output: <class 'int'>, string to integer

# b = 0
# print(bool(b))

# truthy values in Python include non-zero numbers, non-empty strings, and non-empty collections (like lists, tuples, and dictionaries). Falsy values include zero, empty strings, and empty collections.

# * Implicit: type conversion is when Python automatically converts a value from one data type to another based on the context in which it is used. For example, if we add an integer and a float, Python will automatically convert the integer to a float before performing the addition.

# a = 12
# print(type(a/3))  # Output: <class 'float'>, integer to float (implicit conversion)
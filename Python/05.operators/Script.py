# ****************************
#? ***** Operators *****
# ****************************


#? ******* Arithmetic Operators *******

# a=20
# b=20

# *Addition
#print("Addition:", a + b)

# *Subtraction
#print("Subtraction:", a - b)

# *Multiplication
#print("Multiplication:", a * b)

# *Division: p/q is always a float -> 1.0
#print("Division:", a / b)

# *Floor Division: p//q is always a int -> 1 , it removes the decimal part
# print("Floor Division:", a // b)

# *Exponentiation: p**q is always a int -> 1
# print("Exponentiation:", a ** b)

# *Modulus: p%q is always a int -> 0, it provides the remainder of the division
# print("Modulus:", a % b)

#Note:Python follows the BODMAS rule for arithmetic operations.

#? ******* Assignment Operators *******

#* used to assign values to variables

# *Assignment Operator:
a=30
print("Assignment Operator:", a)

#* Add and Assignment Operator:
# a+=10
# a+=40
# print("Add and Assignment Operator:", a)

#* Subtract and Assignment Operator:
# a-=10
# print("Subtract and Assignment Operator:", a)

#* Multiply and Assignment Operator:
# a*=10
# print("Multiply and Assignment Operator:", a)

#* Divide and Assignment Operator:
# a/=10
# print("Divide and Assignment Operator:", a)

#* Modulus and Assignment Operator:
# a%=10
# print("Modulus and Assignment Operator:", a)

#* Exponent and Assignment Operator:
# a**=10
# print("Exponent and Assignment Operator:", a)

#? ******* Comparison Operators *******

#* This returns a boolean value based on the comparison between two values.

a=20
b=10

#* Equal to: ==
#print("Equal to:", a == b) #False

#* Not Equal to: !=
#print("Not Equal to:", a != b) #True

#* Greater than: >
#print("Greater than:", a > b) #True

#* Less than: <
#print("Less than:", a < b) #False

#* Greater than or Equal to: >=
#print("Greater than or Equal to:", a >= b) #True

#* Less than or Equal to: <=
#print("Less than or Equal to:", a <= b) #False

#* Note: We can also compare strings using comparison operators. The comparison is done based on the ASCII values of the characters in the strings.
#print(ord("a")) #97
#print(ord("B")) #66
#print("String Comparison:", "a" > "b") #True

#? ******* Logical Operators *******
#* Logical operators are used to combine conditional statements.
#* Logical AND: and -> all need to be true for the result to be true
# a=20
# print("Logical AND:", a > 10 and a < 30) #True

#* Logical OR: or -> any one need to be true for the result to be true
# print("Logical OR:", a > 10 or a < 30) #True

#* Logical NOT: not -> reverses the result, returns False if the result is true
# print("Logical NOT:", not(a > 10)) #False
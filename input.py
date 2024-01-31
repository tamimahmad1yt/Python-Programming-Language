#How to use code intput from user?
'''Input from user means when user giving any input when program in the process 
and then the program use that value.  '''

name = input("Enter your name: ")
print(name)
print(type(name))      #check datatype

'''When we use input then it will always stored in string.
SO, We use type casting(it is use for coverting one datatype to another datatype)
Example= int(input("Enter age: "))'''

age = int(input("Enter your age:"))
print(age)
print(type(age))      #check datatype


# How to sum two numbers?

num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
sum = num1 + num2
print("The sum of these two numbers is", num1 + num2)
print("The sum of these two numbers is", sum)
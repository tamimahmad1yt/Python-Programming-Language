#How to use variables of different data type?

#string
name= "Tamim"

#integer
roll_number= 127

#floating number
percentage= 96.8

#boolean
is_student= True

print(name, roll_number, percentage, is_student)

#We can update data.
percentage= 93.1

print(name, roll_number, percentage, is_student)

#for checkig data type(class)
print(type(name))
print(type(roll_number))
print(type(percentage))
print(type(is_student))


'''if we want to concatenate(add) data type we can + for concatenate same data types.
We cannot use (+) for concatenate different data types.
We can use comma(, ) for 2 differ data types write in a sentance.'''
#example

print("My name is " + name + " and my roll number is", roll_number, ".")
print("I scored", percentage ,"% in my final exam. I am student is", is_student, ".")

#print expressins("+","-","*" or "/",etc...)
print("My percentage has changed to", percentage + 1, "after rechecking .")

#print with separator()
print(name, roll_number, percentage, is_student, sep=" - ")
V = 0    #0^2+0
W = 2    #1^2+1
X = 5    #2^2+2
Y = 28   #5^2+3
Z = "?"
print(V,W,X,Y,Z, sep=" => ")
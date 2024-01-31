#creating a tuple
colours = ("Green","Red", "Blue", "Black", "Yellow")
print(type(colours))
#creating a tuple only 1 element
fruits = ("Mango",)  #when we have only 1 element then put the comma(,) at the end of element.
print(type(fruits))
        #or
fruits = tuple("Apple")
print(type(fruits))
#accessing elements in tuple
print(colours[1])  #positive indexing
print(colours[-1])  #negative indexing
print(colours[1:4])  #range indexing
print(colours[-3:])  #negative range indexing
#check if an element exists in tuple
if "Blue" in colours :
    print("Blue is a part tuple.")
#traverse the tuple
for i in colours:
    print(i)
#concatenate 2 tuples
colours2 = ("White", "Pink")
colours3 = colours + colours2
print(colours3)
#unpacking of tuple
col1, col2, col3, col4, col5 = colours
print(col1, col2, col3, col4, col5)
#creating a set
names = {"Ram", "Sam", "Ravan", "Tannu"}
print(names)
print(len(names))  #lenth
print(type(names))
#accessing elements of set
for x in names:
    print(x)
#checking if an element exists in a set
if "Sam" in names:
    print("Sam is in the set.")
#add elements in set
names.add("Kareena")
print(names)
# add another sequence in a set 
names_list = ["Annu", "Kaveri"]
names.update(names_list)
print(names)
#removeing element from a set
names.remove("Ram")
print(names)
names.discard("Saim")  #this function will not throw an error if value is not present in set.
print(names)
#joining 2 sets
s1 = {'a', 'b', 'c'}
s2 = {'d', 'e', 'a'}
print(s1, s2)
s3 = s1.union(s2)
print(s3)
s1.update(s2)
print(s1)

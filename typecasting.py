#if we need to concatenate int(a=1,b=2,c=3) but output should shows in str(123) and datatype should  be int.

a = 4
b = 7
c = 3

a_str = str(a)
b_str = str(b)
c_str = str(c)

final_string = a_str + b_str + c_str
final_int = int(final_string)
print("Final int:", final_int, type(final_int))


#if we try to concatenate datatype it occurs TypeError
a = 4
f = "3"
print(a + f)
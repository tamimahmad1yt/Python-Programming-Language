# atithmetic operators
print("sum:", 34 + 43)                  #using for add(+)
print("difference:", 95 - 23)           #using for substract(-)
print("product:", 8 * 8)                #uning for multiplication(*)
print("division", 40 / 6)               #using for division(/)
print("floor division", 40 // 6)        #using for quotient from a divide(//). It will be always integer.
print("modulo", 40 % 6)                 #using for remainder from a divide(%)
print("exponentiation", 10 ** 4)        #using for exponent/power(**)


# relational oprators
'''It is use for compare two operands(operand example=(a=3),(b=1),ect...).
   it's output will be always boolean(true/false).'''
a = 6
b = 2
c = 6
print(a<b)          #less than(<)
print(b<c)          
print(a>b)          #greater than(>)
print(b>c)          
print(a==c)         #equal to(==)
print(a==b)         
print(a>=b)         #greater than or equal(>=)
print(b>=c)         
print(a<=b)         #less than or equal(<=)
print(b<=c)         
print(a!=b)         #not equal to(!=)
print(a!=c)         


#logical operation
'''it is used for compare b/w two expressions.'''
r = 5 <= 0   #false
x = 4 > 1    #true
y = 3 < 8    #true
z = 3 == 4   #false
print("exp1:", x and y)    #in (and) when both expressions true then output will be true otherwise false.
print("exp2:", y and z)    
print("exp3:", z or r)     #in (or) when both expressions false then output will be false otherwise true.
print("exp4:", x or z)
print("exp5:", not x)      #in (not) it will be turn the expression(if expression false it shows true and vice-versa)
print("exp6:", not(z))


#bitwise operators
'''In this operators, decimal numbers change in binnary(0/1) and then execute bitwise operators.
   it's output will be in decimal numbers.'''
m = 4
n = 7
o = 10
     #bitwise and(&)
print("m and n:",m & n)     #m=100(4) & n=111(7) == 100(4) in binnary (1&1=1, 1&0=0, 0/0=0)
print("m and o:",m & o)
     #bitwise or(|)
print("m or n:",m | n)      #m=100(4) & n=111(7) == 111(7) in binnary (1&1=1, 1&0=1, 0/0=0)
print("m or o:",m | o)
     #bitwise xor(^)
print("m xor n:",m ^ n)     #m=100(4) & n=111(7) == 011(3) in binnary (1&1=0, 1&0=1, 0/0=0)
print("m xor o:",m ^ o) 
     #bitwise not(~)

print("not m:",~m)          #
print("not o:",~o)
     #right shift
print("right sift2:",n>>2)       #n=111(7) after shifting >>2 == 001(1)
print("right sift3:",m>>3)       
     #left shift
print("left shift2:",n<<2)       #n=111(7) after shifting <<2 == 11100(28)
print("left shift3:",o<<3)

















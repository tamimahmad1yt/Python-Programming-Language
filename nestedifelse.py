#Take 3 positive int input and print the greatest of them by using nested.
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))
if num1 > num2:
    if num1 > num3:
        print(num1, "is greatest number.")
    else:
        print(num3, "is greatest number.")
else :
    if num2 > num3:
        print(num2, "is greatest number.")
    else:
        print(num3, "is greatest number.")



#Take positive int input and tell if it is divisible by 5 or 3 but not divisible by 15.
number = int(input("Enter a number: "))
if number % 15 == 0:
    print("Number is divisible by 15.")
else:
    if number % 3 == 0 or number % 5 == 0:
        print("The number is not divisible by 15 but divisible by 3 or 5.")
    else:
        print("The number is neither divisible by 3 nor by 5.")
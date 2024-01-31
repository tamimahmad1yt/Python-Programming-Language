#check any number is positive or negative.
number = int(input("Enter a number: "))
if number >= 0:
    print("The number is positive:", number)
else :
    print("The number is negative:", number)
    

#check any number is even or odd.
number = int(input("Enter a number:"))
if number % 2 == 0:
    print("The number is even:", number)
else:
    print("The number is odd:", number)


#Find a seller in profit or loss.
cost = int(input("Enter the cost price of product:"))
sell = int(input("Enter the selling price of product:"))
final = sell - cost
if cost > sell :
    print("You are in loss:", final)
elif cost < cost :
    print("You are in profit:", final)
else :
    print("You are neither profit nor loss.")

  
#grade of marks(91-100 = Excellent),(76-90 = Very Good),(61-75 = Good),(40-60= Average),(40> = Fail)
marks = int(input("Enter your obtained Marks: "))
if marks > 90:
    print(" ''EXCELLENT PERFORMANCE'' ")
elif marks > 75:
    print(" ''VERY GOOD PERFORMANCE'' ")
elif marks > 60:
    print(" ''GOOD PERFORMANCE'' ")
elif marks > 40:
    print(" ''AVERAGE PERFORAMNCE'' ")
else :
    print(" ''FAILED'' ")

    
#if we want to take more one condition.
eng_marks = int(input("Enter Your English Marks: "))
maths_marks = int(input("Enter Your Maths Marks: "))
if eng_marks > 80 and maths_marks > 80:
    print("GRADE->'A'")
elif eng_marks >80 or maths_marks > 80:
    print("GRADE->'B'")
else :
    print("GRADE->'C'")


#check four digits number or not(b/w 1000-9999).
number = int(input("Enter a number: "))
if number >= 1000 and number <= 9999:
    print(number, "is a four digits number.")
else:
    print(number,"is not a four digits number.")


#Take 3 positive int input and print the greatest of them.
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))
if num1 > num2 and num1 >num3:
    print(num1, "is greatest number.")
elif num2 > num3 and num2 > num1:
    print(num2, "is greatest number.")
else :
    print(num3, "is greatest number.")

#Write a program to check if number is odd or even using ternary operator.
number = int(input("Enter a number: "))
output = "Even." if number % 2 == 0 else "Odd."
print("Output is", output)
                #or
print("Output is", "Even." if number % 2 == 0 else "Odd.")
   
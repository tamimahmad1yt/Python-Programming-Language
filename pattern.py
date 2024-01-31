n = int(input("Enter rows: "))   #no. of rows
for _ in range(n):
    print("*" * 5)


n = int(input("Enter rows: "))
for i in range(n):
    for j in range(1, n+1):
        print(j, end=' ')
    print()


n = int(input("Enter rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()


n = int(input("Enter rows: "))
for i in range(n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()


n = int(input("Enter rows: "))
for i in range(1, n+1):
    print(" " * (n-i),end="")
    for j in range(1,2*i):
        print(j,end="")
    print()
n=int(input("Enter number of rows : "))
for i in range (0,n-1):
    for j in range (i,n):
        print(" ",end=" ")
    for j in range (0,i):
        print("*",end=" ")
    for j in range (0,i+1):
        print("*",end=" ")
    print()

for i in range (0,n):
    for j in range (0,i+1):
        print(" ",end=" ")
    for j in range (i,n-1):
        print("*",end=" ")
    for j in range (i,n):
        print("*",end=" ")
    print()

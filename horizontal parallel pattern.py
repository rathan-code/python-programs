n=int(input("Enter number of rows"))
for i in range (0,n):
    for j in range (0,n):
        if (i==0 or i==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

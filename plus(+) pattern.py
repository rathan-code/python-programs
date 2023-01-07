n=int(input("Enter number of rows: "))
for i in range (0,n):
    for j in range (0,n):
        if (i==n//2 or j==n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
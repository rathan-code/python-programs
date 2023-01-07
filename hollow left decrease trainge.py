n=int(input("Enter number of rows: "))
for i in range (0,n):
    for j in range (0,n):
        if ( i+j==n-1 or j==0 or i==0 ):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
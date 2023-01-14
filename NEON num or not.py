'''NEON Number is a number where "sum od square of the number is == Original number"
 for Eg:-
    9
    9 square == 81
    8 + 1 = 9 ==> it is divisible by 9(given number)
    '''
n=int(input("Enter the number : "))
m=n
sum=0;m=n*n
while m!=0:
    d=m%10
    sum=sum+d
    m=m//10
if sum==n:
    print("yes")
else:
    print("No")

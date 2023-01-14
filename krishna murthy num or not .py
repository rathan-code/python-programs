'''Check if a number is krishna murthy or not.
Whether the sum of factorial of digits is equal to the number or not
for Eg:- 
    145= 1! + 4! + 5!'''
import math 
n=int(input("Enter the Number : "))
m=n
sum=0
while m!=0:
    d=m%10
    sum=sum+math.factorial(d)
    m=m//10
if sum==n:
    print("Yes")
else:
    print("No")




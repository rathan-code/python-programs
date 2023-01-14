'''Special number is a number in which 
SUM of it digits + PRODUCT of its digits = ORIGINAL number 
for Eg:-
  59 = 5 + 9 + 5*9 '''
n=int(input("Enter the Number"))
m=n
sum=0;prod=1
while m!=0:
    d=m%10
    sum=sum+d;prod=prod*d
    m=m//10
if n==(sum+prod):
    print("Its a Special number")
else:
    print("Its not a Special number")

    '''
    OUT PUT 
    Enter the Number : 59
    Its a Special Number 
    
    because 59=5+9+5*9
    '''

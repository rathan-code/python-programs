#SPY number means (Sum of its  digits == Product of its digits)
n=int(input("Enter the number"))
m=n
sum=0;prod=1
while m!=0:
    d=m%10
    sum=sum+d;prod=prod*d
    m=m//10
if sum==prod:
    print("Its a SPY number")
else:
    print("Its not a SPY number")

    '''
    Enter the number 123
    Its a spy number 

    beacuse (1*2*3==1+2+3) 

    
    '''


'''DUCK NUMBER is a number which has ZEROS(0) in it 
    if the number has Zero then it is a duck number'''
n=int(input("Enter the Number : "))
m=n
count=0
while m!=0:
    d=m%10
    if d==0 : count+=1    #By replacing d==0 with d== any num we can get its ocuurence 
    m=m//10
if count > 0:
    print("Its a DUCK number and ")
else:
    print("Its not a DUCK number and ")
print(count,"times ZERO is present in the given number")
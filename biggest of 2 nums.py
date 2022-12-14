#To print the Biggest number
#while entering two values please separate with a space
# eg:- 2(space)3 
a,b=[int(a) for a in input ("Enter two Values: ").split()] #we can continue same for input of n values using a,b,c and so on...
if a>b:
    print("is the biggest number",a)
else:
    print("is the biggest number",b)

#while entering two values please separate with a space
# eg:- 2(space)3 
a,b=[int(a) for a in input ("Enter two Values: ").split()]
if a>b:
    print("is the biggest number",a)
else:
    print("is the biggest number",b)
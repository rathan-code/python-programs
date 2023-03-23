def plusMinus(arr):
    l=len(arr)
    p=n=z=0
    for i in range(l):
        if arr[i]>0:
            p+=1
        elif arr[i]<0:
            n+=1
        else:
            z+=1
    print(p/l)
    print(n/l)
    print(z/l)

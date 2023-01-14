n= int(input("Enter the num :"))
m = n
sum=0
while m!= 0:
    d = m % 10
    sum = sum * 10 + d
    m = m // 10
if sum == n:
    print("Its a palindrome")
else:
    print("Its not a palindrome")
n=int(input())
def Fizz_Buzz(input):
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    if (input % 3 == 0 and input % 5 == 0):
        return "FizzBuzz"
    return input
print(Fizz_Buzz(n))
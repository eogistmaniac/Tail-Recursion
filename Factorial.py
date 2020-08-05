def Factorial(n,val = 1):
    if(n == 0):
        return val
    else:
        return Factorial(n-1,n*val)
n = int(input("Enter the number you want factorial of :- "))
print(Factorial(n))
def Palindrome(s):
    if(len(s)<=1):
        return True
    if(s[0] != s[len(s)-1]):
        return False
    else:
        return Palindrome(s[1:((len(s))-1)])
n = input("Enter the string : ")
print(Palindrome(n))
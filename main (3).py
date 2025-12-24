def reverse(n):
    out=0
    stor=n
    while n>0:
        rem=n%10
        out=out*10+rem
        n=n//10
    if store==out:
        return"palindrome"
    else:
        return"not a palindrome"
            
n=int(input("enter the number"))
print(reverse(n))
        

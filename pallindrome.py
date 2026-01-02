#pallindrome number  
n = int(input("enter a number"))
orig = n
rev =0
while n > 0:
    digit = n % 10
    rev = rev  * 10+ digit 
    n = n // 10
    if orig == rev:
        print(f"{orig} is a palindrome number.")
    else:
        print (f"{orig} is not a palindrome number.")
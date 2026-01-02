#armstrong number...
n = int(input("enter a number :"))
orig = n
rev =0
while n > 0:
    digit = n % 10
    sum = sum + digit ** 3
    n = n // 10
    if orig == sum:
        print(f"{orig} is an armstrong number.")
    else:
        print (f"{orig} is not an armstrong number.")
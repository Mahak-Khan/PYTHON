def revNum(n):

    if n <=0:
        return
    lastDigit = n%10
    rem = n//10
    print(lastDigit, end="")
    revNum(rem)

num = int(input("Enter a number:"))
if num == 0:
    print("0")

else:
    revNum(num)
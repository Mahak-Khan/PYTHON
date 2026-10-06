def sumOfDigits(d):
        if d==0:
            return 0
        rem = d % 10
        res = d // 10
        return rem + sumOfDigits(res)

digit = int(input("Enter a number:"))
print(sumOfDigits(digit))
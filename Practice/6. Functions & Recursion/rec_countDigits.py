def countDigits(d):
    if d<10:
        return 1

    return 1 + countDigits(d//10)


digit =int(input("Enter a number:"))
print(countDigits(digit))
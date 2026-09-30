def fact(num):
    f = 1
    while num>0:
        f = f * num
        num = num - 1
    return f

n = fact(5)
print(n)
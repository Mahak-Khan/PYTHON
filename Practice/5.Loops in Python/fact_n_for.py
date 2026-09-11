num = int(input("Enter number:"))
fact = 1

for i in range(num):
    fact = fact*(num-i)
    print(i)

print(fact)

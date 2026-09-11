number = int(input("Enter number:"))
isPrime = True
if number <= 1:
    isPrime = False
else:
    for i in range(2, number):
        if number%i == 0:
            isPrime = False
            break

if isPrime:
    print("Prime!")
else:
    print("Not a prime number!")

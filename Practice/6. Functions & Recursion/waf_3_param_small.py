def small(n1, n2, n3):
    if (n1<n2 and n1<n3):
        print("Smallest is:", n1)
    elif (n2<n1 and n2<n3):
        print("Smallest is:", n2)
    else:
        print("Smallest is:", n3)


num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
num3 = int(input("Enter third number:"))

small(num1, num2, num3)
def checkDiv(n):
    if(n%5 == 0 and n%7 == 0):
        print("Yes")
    else:
        print("No")

num = int(input("Enter a number:"))
checkDiv(num)
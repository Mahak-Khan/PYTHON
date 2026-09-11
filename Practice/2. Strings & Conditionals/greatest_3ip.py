number1= int(input("Enter 1st number:"))
number2= int(input("Enter 2nd number:"))
number3= int(input("Enter 3rd number:"))
if(number1 >= number2 and number1 >= number3):
    print("1st number is greatest !")
elif(number2 >= number1 and number2 >= number3):
    print("2nd number is greatest !")
else:
    print("3rd number is greatest !")
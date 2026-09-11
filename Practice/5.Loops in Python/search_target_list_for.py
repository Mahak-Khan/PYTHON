li = [1,4,9,16,25,36,49,64,81,100]
target = int(input("Enter number:"))
for i in li:
    if(i == target):
        print("Target Found!")
        break
else:
    print("Target Not Found!") 
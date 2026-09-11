li = [1,4,9,16,25,36,49,64,81,100]
target = int(input("Enter number you want to search:"))
i = 0
while i<len(li):
    if li[i] == target:
        print("Target Found!") 
        break
    i+=1
else:
    print("Target Not Found!")
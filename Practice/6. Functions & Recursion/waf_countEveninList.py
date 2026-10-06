def countEvenInList(l):
    countEven = 0
    for i in l:
        if i%2==0:
            countEven  +=1
    print(countEven)

li = [1,2,3,4,5,6,7,8,9,10]
countEvenInList(li)
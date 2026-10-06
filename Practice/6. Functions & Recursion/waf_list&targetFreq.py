def findTargetFreq(l, t):
    freq = 0
    for i in l:
        if i == t:
            freq +=1
    print(freq)

li = [2,124,43,23,123,2,2,2,41,235,241,14,45,24,67]
target = int(input("Enter target:"))
findTargetFreq(li, target)
def largestInList(li):
    largest = li[0]
    for i in li:
        if largest < i:
            largest = i
    print(largest)


l = [1,232,412,13,1,4,4131,32424,1321,4,141,143]
largestInList(l)
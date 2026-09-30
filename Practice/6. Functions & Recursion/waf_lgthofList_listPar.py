def lengthOfList(li):
    return len(li)

length = lengthOfList([2,32,14,4,14,14,14,534,23,3,132,5,4])
print(length)


#loop

def lengthOfList(li):
    count = 0
    for i in li:
        count = count + 1
    return count

length = lengthOfList([2,32,14,4,14,14,14,534,23,3,132,5,4])
print(length)
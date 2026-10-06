def smallestInList(li):
    smallest = li[0]
    for i in li:
        if smallest > i:
            smallest = i
    print(smallest)

l = [32,351,14,2,14,41,-1,34,14,2,14,14,4368,6763,45,774]
smallestInList(l)
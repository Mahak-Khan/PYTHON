def evenInMids(s, e):
    for i in range(s+1, e):
        if i%2 == 0:
            print(i)


start = int(input("Enter start:"))
end = int(input("Enter end:"))
evenInMids(start, end)
def eleAtEvenIdx(li, idx):
    if idx >= len(li):
        return
    if idx%2==0:
        print(li[idx])
    eleAtEvenIdx(li,idx+1)

lis = [1,31,14,14,413,4,574,764,63,63,6,645,63,2525]
eleAtEvenIdx(lis, 0)
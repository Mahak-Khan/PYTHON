def showEle(li, idx):
    if(idx >= len(li)):
        return
    print(li[idx], end=" ")
    showEle(li, idx+1)

showEle([1,23,314,141,1,3], 0)
def  convertUsdInr(usd):
    inr = usd * 100
    return inr

amt = convertUsdInr(int(input("Enter amount:")))
print(amt)

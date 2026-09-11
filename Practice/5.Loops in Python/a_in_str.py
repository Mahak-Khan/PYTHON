word = input("Enter word:")
count = 0
for letter in word:
    if(letter == "a" or letter == "A"):
        count = count+1
print(count)
secret_num = 18
while True:
    guess_num = int(input("Guess number:"))
    if secret_num == guess_num:
        print("Correct!")
        break
    else:
        print("Try Again!")
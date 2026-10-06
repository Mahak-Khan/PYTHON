#Same while reading from front of back

def palindrome(str):
    if len(str) <= 1:
        return True
    if str[0]!= str[len(str)-1]:
        return False
    return palindrome(str[1:-1])
   


s = input("Enter a string:")
if len(s) == 0:
    print("Empty")
else:
    if palindrome(s) == True:
        print("Palindrome")
    else:
        print("Not a palindrome")
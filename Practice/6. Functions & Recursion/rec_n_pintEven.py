def reverseFromN(n):
   if n <= 0:
      return
   if n%2 == 0:
      print(n)

   reverseFromN(n-1)


num = int(input("Enter number:"))
reverseFromN(num)
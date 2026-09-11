li = [21,211,2111,2,1,34989, 66, 89, 82,43]
count_odd = 0 
count_even = 0
for i in li:
    if i%2 == 0:
        count_even += 1
    else:
        count_odd += 1
print("Count of even numbers is:", count_even)
print("Count of odd numbers is:", count_odd)
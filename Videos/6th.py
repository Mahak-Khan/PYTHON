# # # def calc_sum(n1, n2):
# # #     total = n1 + n2
# # #     return total

# # # add = calc_sum(6,9)
# # # print(add)

# # def calc_sum(n1, n2):
# #     return n1 + n2

# # print(print)


# # # add = calc_sum(1,3)
# # # print(add)


# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n-1)

# show(5)

def fact(n):
    if(n == 0 or n==1):
        return 1
    return fact(n-1)*n

print(fact(5))
def perfect(n):
    sum =0
    temp = n
    for i in range(1,n):
        if n%i == 0:
            sum += i
    if sum == n :
        print(n,"is perfect number")
    else:
        print(n, "is not perfect number")
perfect(24)


# def print_perfect_nums(start, end):
#     for i in range(start, end + 1):
#         sum1 = 0
#         for x in range(1, i):
#             # Check if a divisor, if it is, add to sum
#             if(i % x == 0):
#                 sum1 = sum1 + x
#                 if (sum1 == i):
#                     print(i)
# print_perfect_nums(1, 25)

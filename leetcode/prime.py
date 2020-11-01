# def prime(n):
#     if n>1:
#         if n ==2:
#             print("prime", n)
#         else:
#             if n%2 != 0:
#                 print("prime",n)
#             else:
#                 print("not prime")
# prime(1)

n = int(input("enter the number "))
if n > 1:
    for i in range(2,n):
        if n % i == 0:
            print(n, "is not prime")
            break
    else:
        print(n, "is prime")
else:
    print("neither prime nor composite")


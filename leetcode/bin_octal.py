# def binary_decimal(num):
#     i=0
#     d=0
#     while num !=0:
#         last_digit = num % 10
#         d = d+(last_digit*(pow(2,i)))
#         i+=1
#         num=num//10
#     print(d)
# # binary_decimal(111)

# def bin_octal(num):
#     octal =0
#     i=1
#     while num !=0:
#         last_digit = num % 1000
#         value = binary_decimal(last_digit)
#         octal += value*i
#         i=i*10
#         n=n//1000
# bin_octal(10001000111101)

# # there are some errors in python we have oct() functions that convert decimal to octal
# import math


# def binary_to_octal(binary):
#     octal = 0
#     decimal = 0
#     i = 0

#     while(binary != 0):
#         decimal += (binary % 10) * math.pow(2, i)
#         i = i + 1
#         binary = int(binary/10)

#         i = 1

#     while (decimal != 0):
#         octal += (decimal % 8) * i
#         decimal = int(decimal/8)
#         i *= 10

#     return octal

#     return decimal

# binary = int(11111)
# # binary = int(input(“Enter the binary number: “))
# print(int(binary_to_octal(binary)))

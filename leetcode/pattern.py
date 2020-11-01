# wedge pattern
# rows = 6
# for num in range(rows):
#     for i in range(num):
#         print(1 , end=" ")  # print number
#     # line after each row to display pattern correctly
#     print(" ")


# #pyramid
# print("Print equilateral triangle Pyramid using stars ")
# size = 4
# m = (2 * size) - 2
# for i in range(0, size):#row logic
#     for j in range(0, m):#space logic
#         print(end=" ")
#     m = m - 1  # decrementing m after each loop
#     for j in range(0, i + 1):
#         # printing full Triangle pyramid using stars
#         print("* ", end=' ')
#     print(" ")

#diamond
# rows = 5
# k = 2 * rows - 2
# for i in range(0, rows):
#     for j in range(0, k):
#         print(end=" ")
#     k = k - 1
#     for j in range(0, i + 1):
#         print("* ", end="")
#     print("")
    
# k = rows - 2

# for i in range(rows, -1, -1):
#     for j in range(k, 0, -1):
#         print(end=" ")
#     k = k + 1
#     for j in range(0, i + 1):
#         print("* ", end="")
#     print("")
# using function and built in method
# def larg_small_lis(list1):
#     length = len(list1)
#     list1.sort()
#     print("largest is ", list1[length-1])
#     print("2nd largest is ", list1[length-2])
#     print("smallest is ", list1[0])
#     print("2nd smallest is ", list1[1])

# list1=[12, 45, 2, 41, 31, 10, 8, 6, 4]
# largest = larg_small_lis(list1)

# without using built in methods


def larg_small_lis(list):
    largest = list[0]
    smallest = list[0]
    largest2 = None
    smallest2 = None
    for item in list:
        if item > largest:
            largest2 = largest
            largest = item
        elif largest2 == None or item > largest2:
            largest2 = item
        if item < smallest:
            smallest2 = smallest
            smallest = item
        elif smallest2 == None or item < smallest2:
            smallest2 = item
    print("largest is ", largest)
    print("2nd largest is ", largest2)
    print("smallest is ", smallest)
    print("2nd smallest is ", smallest2)
    
list1=[12, 45, 2, 41, 31, 10, 8, 6, 4]
largest = larg_small_lis(list1)

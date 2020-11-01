def linearSearch(list):
    pos = -1
    key = (input("enter key \n"))
    length = len(list)
    for i in range(length):
        if key == list[i]:
            pos = i
            print("key found in position", i)
            break;
    else:
        print("no such key")
list = ['t','u','t','o','r','i','a','l']
linearSearch(list)
    

# def linearsearch(arr, x):
#    for i in range(len(arr)):
#       if arr[i] == x:
#          return i
#    return -1
# arr = ['t','u','t','o','r','i','a','l']
# x = 'a'
# print("element found at index "+str(linearsearch(arr,x)))
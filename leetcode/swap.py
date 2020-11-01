#swap number only using 2 variables
def swap(a,b):
    a=a+b
    b=a-b
    a=a-b
    print(a,b)
swap(10,12)
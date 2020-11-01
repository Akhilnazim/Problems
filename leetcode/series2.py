# 1, 1, 2, 3, 4, 9, 8, 27, 16, 81, 32, 243,64, 729, 128, 2187 
num = int(input())
if(num%2==0):
    num = num // 2
    print(3**(num-1))
    # print(pow(3,num-1))
else:
    num = num // 2 + 1
    print(2**(num-1))
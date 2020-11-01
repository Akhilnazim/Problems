
#sum of power of digits equal to number 153 = 1^3+5^3+3^3
def armstrongNumber(n):
    #count number of digits
    count = 0
    temp = n
    while n>0:
        n= n//10
        count += 1
    # print (count)
    n=temp
    sum = 0
    while n!=0:
        last_digit = n%10
        #taking power using pow function ie 1^3 (last digit ^ 3)
        sum += pow(last_digit, count)
        n=n//10
    if sum==temp:
        print ("Armstrong")
    else: print("not armstrong")


armstrongNumber(153)

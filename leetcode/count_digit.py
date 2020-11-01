def countDigit(n):
    count = 0
    while n!= 0:
        lastDigit = n%10
        count+=1
        n = n//10
    print(count)
countDigit(110022111511531)
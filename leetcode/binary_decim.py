def binary_decimal(num):
    i=0
    d=0
    while num !=0:
        last_digit = num % 10
        d = d+(last_digit*(pow(2,i)))
        i+=1
        num=num//10
    print(d)
binary_decimal(111)
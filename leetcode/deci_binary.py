def decimaltoBinary(num):
    i=1
    rem=0
    binary = 0
    while num !=0:
        rem = num%2
        num = num//2
        binary = binary+rem*i
        i=i*10
    print (binary)
decimaltoBinary(7)

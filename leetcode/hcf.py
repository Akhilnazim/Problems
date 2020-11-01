def hcf(a,b):
    if a < b:
        low = a
    else:
        low = b
    for i in range(1,low+1):
        if ((a%i == 0)and (b%i == 0)):
            hcf = i
    return hcf
print(hcf(3215,5545))
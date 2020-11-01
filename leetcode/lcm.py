#so here we are finding lowest of numbers and taking mod with the first number and second if it is zero then it is the lcm else we increment low value

def lcm(a,b):
    if a<b:
        low = a
    else: low = b
    while(1):
        if ((low%a == 0) and (low%b == 0)): 
            lcm = low
            break;
        low += 1
    return lcm
print(lcm(12,8))


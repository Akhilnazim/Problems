t1 =0
t2 =0
t3 = 0
count = 1
while count <=9:
    x = int(input("enter the value"))
    if (x>=1 and x<=100):
        if count%3 == 1:
            t1+=x
        elif count%3 == 2:
            t2+=x
        else:
            t3+=x
        count+=1
    else:
        print("invalid")
        count+=1
A1 = (t1//3)
A2 = (t2//3)
A3 = (t3//3)
if (A1 <=70 and A2 <=70 and A3 <=70):
    print("unfit")
if (A1>=A2 and A1>=A3):
    print("trainee1", A1)
if(A2>=A1 and A2>=A3):
    print("trainee2", A2)
if(A3>=A1 and A3>=A2):
    print("trainee3", A3)

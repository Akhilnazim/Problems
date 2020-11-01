def unique_number_count(l,r):
    count = 0
    for i in range(l,r+1):
        num = i
        #declaring array to compare weather number is repeated also if repeated 0 is replaced by 1
        array_list = [0,0,0,0,0,0,0,0,0,0]
        while(num):
            if array_list[num%10] == 1:
                break;
            array_list[num%10] = 1;
            num = (int) (num / 10)
        if num == 0:
            count += 1
    if count>0:
        print(count)
    else:
        print("No unique")
l=10    
r=30
unique_number_count(l,r)
    
        


def palindrome(num):
        rev = 0
        temp = num
        while num>0 :
            last_num = num%10
            num = num//10
            rev =rev*10+last_num
        if(rev == temp) :
            print("palindrome")
        else: print("not palindrome")
palindrome(100)


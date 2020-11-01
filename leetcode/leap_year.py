def leapYear(y):
    if (y%400 == 0) or ((y%4 == 0) and (y%100 != 0))  :
        print("it is a leap year")
    else: print("not a leap year")
leapYear(2004)


# Python program to check if year is a leap year or not

year = 2016

# To get year (integer input) from the user
# year = int(input("Enter a year: "))

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))
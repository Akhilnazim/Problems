import math

def Area_of_Triangle(a, b, c):
    
    # calculate the Perimeter
    Perimeter = a + b + c
    # calculate the semi-perimeter
    s = (a + b + c) / 2

    # calculate the area
    Area = math.sqrt((s*(s-a)*(s-b)*(s-c)))

    print("\n The Perimeter of Traiangle = %.2f" %Perimeter)
    print(" The Semi Perimeter of Traiangle = %.2f" %s)
    print(" The Area of a Triangle is %0.2f" %Area)

Area_of_Triangle(6, 7, 8)
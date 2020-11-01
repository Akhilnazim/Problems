# 1
def Fibonacci(n):
    if n<=0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n==1:
        return 0
    # Second Fibonacci number is 1
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
 
# # Driver Program
 
# print(Fibonacci(4))
# 2
n = int(input("Enter the value of 'n': "))
a = 0
b = 1
sum = 0
count = 1
print("Fibonacci Series: ", end = " ")
while(count <= n):
  print(sum, end = " ")
  count += 1
  a = b
  b = sum
  sum = a + b

# 3
# #Python program to generate Fibonacci series Program using Recursion
# def Fibonacci_series(Number):if(Number == 0):
#     return 0elif(Number == 1):
#     return 1else:
#     return (Fibonacci_series(Number - 2) + Fibonacci_series(Number - 1))

# n = int(input("Enter the value of 'n': "))
# print("Fibonacci Series:", end = ' ')
# for n in range(0, n):
#   print(Fibonacci_series(n), end = ' ')
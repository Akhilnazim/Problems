#laargest number without using conditional operator
# Python3 program to Compute the minimum 
# or maximum of two integers without 
# branching 

# Function to find minimum of x and y 

def min(x, y): 

	return y ^ ((x ^ y) & -(x < y)) 


# Function to find maximum of x and y using xor operation
def max(x, y): 

	return x ^ ((x ^ y) & -(x < y)) 


# Driver program to test above functions 
x = 1
y = 6
print("Minimum of", x, "and", y, "is", end=" ") 
print(min(x, y)) 
print("Maximum of", x, "and", y, "is", end=" ") 
print(max(x, y)) 



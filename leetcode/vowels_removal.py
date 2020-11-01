vowels = ['a','e','i','o','u']


string = input()

inp=string.lower()
for i in range(len(inp)):
    if not inp[i] in vowels:
        print(string[i],end="")

# if len(inp) == 0 :
#     print("INVALID INPUT")

# flag=0

# for i in vowels:
#     if i in inp:
#         flag+=1

# if flag == 0:
#     print("0")
#     exit()
# else:
#     for i in range(5):
#         vowels.append(0)
#     for i in inp:
#         if i in vowels:
#             vowels[vowels.index(i)+5]+=1
# for i in range(5):
#     print(vowels[i],":",vowels[i+5])

# for i in range(len(inp)):
#     if not inp[i] in vowels:
#         print(string[i],end="")

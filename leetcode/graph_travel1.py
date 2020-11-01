n= int (input())
c= 'R'
x=0
y=0
d=10
for i in range(n):
    if c=='R':
        x+=d
        d+=10
        c= 'U'
    elif c=='U':
        y+=d
        d+=10
        c = 'L'
    elif c=='L':
        x-=d
        d+=10
        c= 'D'
    elif c=='D':
        y-=d
        d+=10
        c= 'A'
    elif c=='A':
        x+=d
        d+=10
        c='R'
print(x,y)

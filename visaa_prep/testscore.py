n,x,y=map(int,input().split())
a=n*x
b=n*0
if y<=a and y>=b and (y%x==0):
    print("YES")
else:
    print("NO")

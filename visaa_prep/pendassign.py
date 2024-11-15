x,y,z=map(int,input().split())
a=z*24*60
b=x*y
if b<=a:
    print("YES")
else:
    print("NO")

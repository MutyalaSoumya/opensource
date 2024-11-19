n=int(input())
a=list(map(int,input().split()))
count=0
b=0
for i in a:
    if i==0:
        count+=1
        b=max(count,b)
    else:
        count=0
print(b)        

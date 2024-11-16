t=int(input())
for _ in range(0,t):
    n,m=map(int,input().split())
    if m>=n:
        print("0")
    else:
        a=n-m
        print(a)
        
        

n=int(input())
m=[]
for _ in range(n):
    a=list(map(int,input().split()))
    m.append(a)
b=[a[::-1] for a in m]
for a in b:
    print(" ".join(map(str,a)))
    

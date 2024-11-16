n=int(int(input()))
a=list(map(int,input().split()))
b=list(dict.fromkeys(a))
print(*b)

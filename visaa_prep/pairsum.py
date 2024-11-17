n=int(input())
a=list(map(int,input().split()))
k=int(input().strip())
found=False
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==k:
            found=True
            break
    if found:
        break
print("true" if found else "false")
            

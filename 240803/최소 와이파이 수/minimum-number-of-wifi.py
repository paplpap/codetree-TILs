n,m = map(int,input().split())
arr = list(map(int,input().split()))

cnt = 0
for i in range(m,n-m+1,2*m+1):
    for j in range(i-m,i+m+1):
    
        if arr[j] == 1:
            cnt += 1
            
            break

print(cnt)
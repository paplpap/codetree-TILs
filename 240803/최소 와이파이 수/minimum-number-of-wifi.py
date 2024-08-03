n,m = map(int,input().split())
arr = list(map(int,input().split()))

cnt = 0

if m == 0:
    for i in range(n):
        if arr[i] == 1:
            cnt += 1
    print(cnt)
elif m >= n:
    if 1 in arr:
        print(1)
    else:
        print(0)
else:
    aaa = 0
    for i in range(m,n,2*m+1):
        aaa = i+m
        for j in range(i-m,i+m+1):
            if arr[j] == 1:
                cnt += 1
                
                break
    if 1 in arr[aaa:]:
        print(cnt + 1)
    else:
        print(cnt)
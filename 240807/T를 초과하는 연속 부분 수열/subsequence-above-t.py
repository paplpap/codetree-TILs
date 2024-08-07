n, t = map(int,input().split())
arr = list(map(int, input().split()))

maxcnt = 0
cnt = 0
for i in range(n):
    if arr[i] > t:
        cnt += 1
    else:
        maxcnt = max(cnt, maxcnt)
        cnt = 0
    
print(maxcnt)
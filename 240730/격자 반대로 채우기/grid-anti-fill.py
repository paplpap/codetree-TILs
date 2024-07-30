n = int(input())
arr = []

for _ in range(n):
    arr.append([0]*n)    

cnt = 1
for i in range(n-1,-1,-1):
    if i % 2 != 0:
        for j in range(n-1,-1,-1):
            arr[j][i] = cnt
            cnt += 1
    else:
        for j in range(0,n):
            arr[j][i] = cnt
            cnt += 1



for i in range(n):
    print(*arr[i])
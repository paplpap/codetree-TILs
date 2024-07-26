n = int(input())

arr = []
for _ in range(n):
    a = list(map(int,input().split()))
    arr.append(a)

cnt = 0

for i in range(n):
    for j in range(n-2):
        jz = arr[i][j] + arr[i][j+1] + arr[i][j+2]
        if jz > cnt:
            cnt = jz 

print(cnt)
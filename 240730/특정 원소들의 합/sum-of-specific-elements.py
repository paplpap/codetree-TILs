arr = []
for _ in range(4):
    a = list(map(int,input().split()))
    arr.append(a)

cnt = 0
for i in range(4):
    for j in range(0,i+1):
        cnt += arr[i][j]
        

print(cnt)
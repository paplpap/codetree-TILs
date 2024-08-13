n = int(input())
arr = [[0]*201 for _ in range(201)]

for _ in range(n):
    #x1, y1, x2, y2 = map(int,input().split())
    x1, y1 = map(int,input().split())

    for i in range(100+x1,100+x1+8):
        for j in range(100+y1,100+y1+8):
            arr[i][j] = 1


cnt = 0
for p in arr:
    for j in p:
        if j == 1:
            cnt += 1

print(cnt)
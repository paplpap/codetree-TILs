#n = int(input())
arr = [[0]*2001 for _ in range(2001)]

for _ in range(2):
    x1, y1, x2, y2 = map(int,input().split())

    for i in range(1000+x1,1000+x2):
        for j in range(1000+y1,1000+y2):
            arr[i][j] = 1

x1, y1, x2, y2 = map(int,input().split())

for i in range(1000+x1,1000+x2):
    for j in range(1000+y1,1000+y2):
        arr[i][j] = 2


cnt = 0
for p in arr:
    for j in p:
        if j == 1:
            cnt += 1

print(cnt)
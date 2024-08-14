n = int(input())

arr = []

for i in range(n):
    a = list(map(int, input().split()))
    arr.append(a)

cnt = 0
for i in range(n):
    arr[0][i] = arr[0][i] + cnt
    cnt = arr[0][i]

cnt = 0
for i in range(n):
    arr[i][0] = arr[i][0] + cnt
    cnt = arr[i][0]

#cnt = 0
for i in range(1,n):
    for j in range(1,n):
        arr[i][j] += max(arr[i-1][j], arr[i][j-1])


        #cnt += arr[i][j]
        #arr[i][j] = cnt

print(arr[n-1][n-1])
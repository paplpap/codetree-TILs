n,m = map(int,input().split())

arr = []
arr1 = []

for _ in range(n):
    a = list(map(int,input().split()))
    arr.append(a)
    
for _ in range(n):
    a = list(map(int,input().split()))
    arr1.append(a)

for i in range(n):
    for j in range(m):
        if arr[i][j] == arr1[i][j]:
            arr1[i][j] = 0
        else:
            arr1[i][j] = 1

for i in range(n):
    print(*arr1[i])
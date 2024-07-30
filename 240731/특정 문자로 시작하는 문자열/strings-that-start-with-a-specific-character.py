n = int(input())

arr = []
for i in range(n+1):
    arr.append(input())

cnt = 0
result = 0
for j in range(n-1):
    if arr[-1] == arr[j][0]:
        cnt += 1
        result += len(arr[j])

print(cnt,f'{result/cnt:0.2f}')
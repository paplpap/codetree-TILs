n = int(input())

arr = list(map(int,input().split()))

cnt = 101
for i in range(n-1):
    cnt = min(cnt,(arr[i+1] - arr[i]))

print(cnt)
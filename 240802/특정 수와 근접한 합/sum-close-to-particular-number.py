n,s = map(int,input().split())

arr = list(map(int,input().split()))

cnt = sum(arr)
result = []

for i in range(n-1):
    for j in range(i+1,n):
        asd = cnt - (arr[i] + arr[j])
        asd -= s
        if asd < 0:
            asd = -asd
        result.append(asd)

print(min(result))
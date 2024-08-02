n, k = map(int,input().split())

arr = list(map(int,input().split()))

result = []

for i in range(n-2):
    aaa = sum(arr[i:k+i])
    result.append(aaa)

print(max(result))
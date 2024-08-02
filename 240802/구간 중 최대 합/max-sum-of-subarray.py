n, k = map(int,input().split())

arr = list(map(int,input().split()))

result = []

for i in range(n-2):
    aaa = arr[i] + arr[i+1] + arr[i+2]
    result.append(aaa)

print(max(result))
a,b = map(int,input().split())

arr = [a,b]
for i in range(2,10):
    a = arr[i-1] + arr[i-2]*2
    arr.append(a)

print(*arr)
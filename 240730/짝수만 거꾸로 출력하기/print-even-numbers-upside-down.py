n = int(input())

arr = list(map(int,input().split()))
arr1 = []

for i in range(len(arr)):
    if arr[i] % 2 == 0:
        arr1.append(arr[i])        

arr1 = arr1[::-1]
print(*arr1)
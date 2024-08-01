n = int(input())
arr = list(map(int,input().split()))

def aa(n,arr):
    for i in range(n):
        if arr[i] < 0:
            arr[i] = -arr[i]
        print(arr[i], end = ' ')


aa(n,arr)
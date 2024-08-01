n = int(input())

arr = list(map(int,input().split()))

def aa(n,arr):
    for i in range(n):
        if arr[i]%2 == 0:
            arr[i] = arr[i]//2
        print(arr[i], end = ' ')
        
    

aa(n,arr)
n = int(input())

arr = []
for _ in range(n):
    a = list(map(int,input().split()))
    arr.append(a)


result = []
ex = []
for i in range(1,n-1):
    ex = arr[i]
    del(arr[i])
    
    dx = arr[0][0]
    dy = arr[0][1]
    
    cnt = 0
    for j in arr:
        a = dx - j[0]
        b = dy - j[1]

        if a < 0:
            a = -a
        if b < 0:
            b = -b

        
        cnt += a+b

        dx = j[0]
        dy = j[1]

    result.append(cnt)

    arr.insert(i,ex)

print(min(result))
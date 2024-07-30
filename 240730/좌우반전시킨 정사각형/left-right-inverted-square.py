n = int(input())

for i in range(1,n+1):
    a = []
    for j in range(n,0,-1):
        a.append(j*i)
    print(*a)
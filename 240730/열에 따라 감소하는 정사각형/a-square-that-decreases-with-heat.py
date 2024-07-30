n = int(input())

for i in range(n):
    a = []
    for j in range(n,0,-1):
        a.append(j)
    print(*a)
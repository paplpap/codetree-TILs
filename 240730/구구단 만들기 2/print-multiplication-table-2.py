n,m = map(int,input().split())

for i in range(2,9,2):
    for j in range(m,n-1,-1):
        if j == n:
            print(f'{j} * {i} = {i*j}',end='')
        else:
            print(f'{j} * {i} = {i*j} / ',end='')
    print()
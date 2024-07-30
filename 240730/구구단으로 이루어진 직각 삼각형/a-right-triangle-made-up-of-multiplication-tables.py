n = int(input())

for i in range(1,n+1):
    for j in range(n,i-1,-1):
        if j == i:
            print(f'{i} * {n-j+1} = {i*(n-j+1)}',end = ' ')
        else:
            print(f'{i} * {n-j+1} = {i*(n-j+1)} /',end = ' ')
    print()
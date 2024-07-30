n = int(input())

dx,dy = 0,0
arr = []
for i in range(n):
    ww = list(input().split())
    a = ww[0]
    b = int(ww[1])
    if a == 'N':
        dy += b
    elif a == 'E':
        dx += b
    elif a == 'W':
        dx -= b
    elif a == 'S':
        dy -= b

print(dx,dy)
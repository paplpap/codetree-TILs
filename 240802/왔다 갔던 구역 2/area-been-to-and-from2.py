n = int(input())

rr = 0
ll = 0
for i in range(n):
    a,b = input().split()
    if b == 'R':
        rr += int(a)
    else:
        ll += int(a)

print(min(rr,ll))
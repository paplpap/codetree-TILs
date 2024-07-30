n = int(input())

aw = '* '
for i in range(n-1,0,-1):
    print(' '*i,end = '')
    print(aw*(n-i))

for i in range(0,n):
    print(' '*i,end = '')
    print(aw*(n-i))
n = int(input())

aw = '* '
print(aw*n)
for i in range(n-1):
    print(aw*(i+1),end = '')
    print('  '*(n-i-2),end = '')
    print(aw)
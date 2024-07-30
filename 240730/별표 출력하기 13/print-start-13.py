n = int(input())

aw = '* '

for i in range(1,n+1):
    print(aw*(n-i+1))
    print(aw*i)
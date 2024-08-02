a, b = map(int,input().split())
n = int(input(),a)


a = ''
while n > 0:
    n,m = divmod(n,b)
    a += str(m)

print(a[::-1])
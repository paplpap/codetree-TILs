n,m = map(int,input().split())

#n = int(input())

if n == 0:
    print(0)
else:
    a = ''
    while n > 0:
        n,b = divmod(n,m)
        a += str(b)

    print(a[::-1])
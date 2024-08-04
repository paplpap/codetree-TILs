a,b,c,d = map(int, input().split())

if a <= c <= b:
    print('intersecting')
elif c <= a <= d:
    print('intersecting')
elif a <= d <= b:
    print('intersecting')
elif c <= b <= d:
    print('intersecting')
else:
    print('nonintersecting')
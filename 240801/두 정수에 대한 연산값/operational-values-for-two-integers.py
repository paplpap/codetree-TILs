a,b = map(int,input().split())


def aa(a,b):
    if a > b:
        return a+25,b*2
    else:
        return a*2,b+25

print(*aa(a,b))
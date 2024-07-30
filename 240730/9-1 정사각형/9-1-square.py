n = int(input())

a = 9
for i in range(n):
    for j in range(n):
        if a == 0:
            a = 9
        print(a,end = '')
        a -= 1
    print()
a,b = map(int,input().split())

cnt = 0
for i in range(a,b+1):
    if i % 6 == 0:
        if i % 8 != 0:
            cnt += i

print(cnt)
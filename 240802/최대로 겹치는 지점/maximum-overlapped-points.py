li = [0]*203

n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    for j in range(a-1,b+1):
        li[100+j] += 1

print(max(li))
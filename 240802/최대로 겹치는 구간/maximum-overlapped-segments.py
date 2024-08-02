li = [0]*201

n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    for j in range(a,b):
        li[100+j] += 1

print(max(li))
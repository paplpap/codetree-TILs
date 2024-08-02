arr = []

n = int(input())
for i in range(n):
    a,b,c,d = input().split()
    b = int(b)
    c = int(c)
    d = int(d)
    arr.append([a,b,c,d])

arr.sort(key = lambda x : (x[1],x[2],x[3]), reverse=True)

for j in range(n):
    print(*arr[j])
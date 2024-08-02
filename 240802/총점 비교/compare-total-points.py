arr = []

n = int(input())
for i in range(n):
    a,b,c,d = input().split()
    b = int(b)
    c = int(c)
    d = int(d)
    plus = b+c+d
    arr.append([a,b,c,d,plus])



arr.sort(key = lambda x : x[4])

for j in range(n):
    print(*arr[j][:-1])
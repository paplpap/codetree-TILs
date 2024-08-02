arr = []

n = 5
for i in range(n):
    a,b,c = input().split()
    
    b = int(b)
    c = float(c)
    
    arr.append([a,b,c])

#arr.sort(key = lambda x : (x[2]))
arr.sort(key = lambda x : (x[0]))

print('name')
for j in range(n):
    print(*arr[j])

arr.sort(key = lambda x : (x[1]), reverse=True)

print()
print('height')
for j in range(n):
    print(*arr[j])
arr = []

n = int(input())
for i in range(n):
    a,b,c = input().split()
    
    b = int(b)
    c = int(c)
    
    arr.append([a,b,c])

arr.sort(key = lambda x : (x[2]), reverse=True)
arr.sort(key = lambda x : (x[1]))

#print('name')
for j in range(n):
    print(*arr[j])
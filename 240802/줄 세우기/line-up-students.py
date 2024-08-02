arr = []

n = int(input())
for i in range(n):
    a,b = input().split()
    
    a = int(a)
    b = int(b)
    
    arr.append([a,b,i+1])

arr.sort(key = lambda x : (x[2]))
arr.sort(key = lambda x : (x[0],x[1]), reverse=True)

for j in range(n):
    print(*arr[j])
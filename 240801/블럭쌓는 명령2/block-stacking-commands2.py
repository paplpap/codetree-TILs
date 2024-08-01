n,k = map(int,input().split())

list_ = [0]*n

for i in range(k):
    a,b = map(int,input().split())
    for j in range(a-1,b):
        list_[j] += 1
    
    
print(max(list_))
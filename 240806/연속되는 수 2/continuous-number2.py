n= int(input())

now = -1
maxc = 1
cnt = 1
for i in range(n):
    
    a = int(input())
    
    if now != a:
        now = a
        maxc = max(cnt,maxc)
        cnt = 1
    else:
        cnt += 1
    
maxc = max(cnt,maxc)

print(maxc)
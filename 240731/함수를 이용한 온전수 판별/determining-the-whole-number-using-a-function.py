a, b = map(int,input().split())

cnt = 0
for i in range(a,b+1):
    if i % 2 == 0:
        continue
    if i%10 == 5:
        continue        
    if i%3 == 0:
        if i%9 != 0:
            continue
    cnt += 1
    
                

print(cnt)
a,b = map(int,input().split())

cnt = 0
for i in range(a,b+1):
    flag = 0
    for j in range(2,int(i**(1/2)+1)):
        if i%j == 0:
            flag = 1
            break
    
    if flag == 0:
        i = str(i)
        i = [int(q) for q in i]
        if sum(i) % 2 == 0:
            cnt += 1
            

print(cnt)
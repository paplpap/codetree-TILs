a = list(input())

cnt = 0
for i in range(len(a)):
    if a[i] =='(':
        for j in range(i,len(a)):
            if a[j] == ')':
                cnt += 1
        
print(cnt)
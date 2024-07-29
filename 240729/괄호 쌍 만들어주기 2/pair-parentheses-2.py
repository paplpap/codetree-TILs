a = list(input())
la = len(a)

cnt = 0
for i in range(la-1):
    if a[i]+a[i+1] =='((':
        for j in range(i,la-1):
            if a[j]+a[j+1] =='))':
                cnt += 1

print(cnt)
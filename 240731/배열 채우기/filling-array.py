arr=list(map(int,input().split()))

a=''
for i in arr[::-1]:
    if i == 0:
        a = ''
        continue
        
    else:
        i = str(i)
        a += ' '+i

print(a[1:])
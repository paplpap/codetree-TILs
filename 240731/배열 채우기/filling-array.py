arr=list(map(int,input().split()))

a=''
for i in arr[::-1]:
    if i == 0:
        break
    else:
        a += str(i)
        print(a,end=' ')
    a = ''
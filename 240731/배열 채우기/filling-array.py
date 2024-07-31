arr=list(map(int,input().split()))

a=''
for i in arr[::-1]:
    if i != 0:
        a += str(i)
        print(a,end=' ')
    else:
        break
    a = ''
# arr = []
# for _ in range(4):
#     a = list(map(int,input().split()))
#     arr.append(a)

# cnt = 0
# for i in range(4):
#     for j in range(0,i+1):
#         cnt += arr[i][j]
        

# print(cnt)

a=[]
b=[]
c=[]
d=[]


for i in range(4):
    arr=list(map(int, input().split()))
    if i==0:
        a.append(arr)
    if i==1:
        b.append(arr)
    if i==2:
        c.append(arr)
    if i==3:
        d.append(arr)


print(sum(a[0][:1])+sum(b[0][:2])+sum(c[0][:3])+sum(d[0][:4]))
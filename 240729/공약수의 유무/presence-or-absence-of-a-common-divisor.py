arr = []
arr_1 = []
for i in range(1, int(1920**1/2)):
    if 1920 % i == 0:
        arr.append(i)
        arr.append(1920//i)

for i in range(1,int(2880**1/2)):
    if 2880 % i == 0:
        arr_1.append(i)
        arr_1.append(2880//i)

arr = set(arr)
arr_1 = set(arr_1)

result = arr & arr_1


a,b = map(int,input().split())

for i in range(a,b+1):
    if i in result:
        print(1)
        
        exit(0)

print(0)
arr = []

for i in range(1, int(1920**1/2)):
    if 1920 % i == 0:
        arr.append(i)
        arr.append(1920//i)

for i in range(1,int(2880**1/2)):
    if 2880 % i == 0:
        arr.append(i)
        arr.append(2880//i)

arr = set(arr)

a,b = map(int,input().split())

for i in range(a,b):
    if i in arr:
        print(1)
        exit(0)

print(0)
a = int(input())

arr = []

for i in range(1,a+1):
    if i % 2 == 0:
        if i % 4 != 0:
            #arr.append(i)
            continue

    if (i // 8)%2 == 0:
        #arr.append(i)
        continue

    if i%7 < 4:
        #arr.append(i)
        continue
    arr.append(i)
print(*arr)
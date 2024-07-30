arr = map(int,input().split())

first = 0
for i in arr:
    if i % 3 == 0:
        break
    first = i
print(first)
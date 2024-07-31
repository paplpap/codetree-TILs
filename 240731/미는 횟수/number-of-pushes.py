a = input()
b = input()

cnt = 1
for i in range(len(a)):
    a = a[-1] + a[:-1]
    if a == b:
        break
    cnt += 1

if cnt == len(a)+1:
    cnt = -1

print(cnt)